#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="$ROOT_DIR/outputs/run_manifest.csv"
LOG_DIR="$ROOT_DIR/outputs/raw_agent_logs/pilot"
TMP_DIR="$ROOT_DIR/outputs/.tmp_openclaw"
AGENT_ID="${AGENT_ID:-benchmark}"
AGENT_NAME="openclaw"
CHANNEL="cli"
VARIANT_ID="level2"
LEVEL="level2"
THINKING="${THINKING:-high}"
TIMEOUT_SECONDS="${TIMEOUT_SECONDS:-1200}"
OPENCLAW_VERSION="$(openclaw --version | awk '{print $2}')"

mkdir -p "$LOG_DIR" "$TMP_DIR"

CASES=(
  "C001 benchmark/cases/C001_charitable_giving/agent_task_level2.md"
  "C002 benchmark/cases/C002_consumer_credit/agent_task_level2.md"
  "C005 benchmark/cases/C005_online_ad_measurement/agent_task_level2.md"
  "C008 benchmark/cases/C008_retail_tax_salience/agent_task_level2.md"
  "C014 benchmark/cases/C014_corruption_monitoring/agent_task_level2.md"
)

extract_json() {
  local input_file="$1"
  awk 'BEGIN{printing=0} /^\{/{printing=1} printing{print}' "$input_file"
}

append_manifest_row() {
  local csv_row="$1"
  printf '%s\n' "$csv_row" >> "$MANIFEST"
}

for case_entry in "${CASES[@]}"; do
  case_id="${case_entry%% *}"
  input_file="${case_entry#* }"
  timestamp_local="$(date '+%Y-%m-%dT%H:%M:%S%z')"
  run_stamp="$(date '+%Y%m%d_%H%M%S')"
  run_id="RUN_${run_stamp}_${AGENT_NAME}_deepseekv4pro"
  output_file="$LOG_DIR/${case_id}_${VARIANT_ID}_${AGENT_NAME}_${run_id}.md"
  cli_capture="$TMP_DIR/${run_id}.stdout"
  json_capture="$TMP_DIR/${run_id}.json"
  session_capture="$TMP_DIR/${run_id}.session.jsonl"

  echo "Running ${case_id} ${VARIANT_ID} -> ${run_id}"

  openclaw agent \
    --agent "$AGENT_ID" \
    --local \
    --json \
    --thinking "$THINKING" \
    --timeout "$TIMEOUT_SECONDS" \
    --message "$(cat "$ROOT_DIR/$input_file")" \
    > "$cli_capture"

  extract_json "$cli_capture" > "$json_capture"

  status="success"
  model="$(jq -r '.meta.agentMeta.model' "$json_capture")"
  model_provider="$(jq -r '.meta.agentMeta.provider' "$json_capture")"
  session_file="$(jq -r '.meta.agentMeta.sessionFile' "$json_capture")"
  cp "$session_file" "$session_capture"

  final_output="$(jq -r '.finalAssistantRawText // .finalAssistantVisibleText // (.payloads | map(.text // "") | join("\n"))' "$json_capture")"
  system_prompt_summary="$(jq -r '"workspace=" + .meta.systemPromptReport.workspaceDir + "; thinking=" + .meta.requestShaping.thinking + "; tools=" + ((.meta.systemPromptReport.tools.entries // []) | map(.name) | join(", "))' "$json_capture")"
  tool_log_summary="$(jq -r 'if (.meta.systemPromptReport.tools.entries // []) | length == 0 then "none" else ((.meta.systemPromptReport.tools.entries // []) | map(.name) | join(", ")) end' "$json_capture")"
  duration_ms="$(jq -r '.meta.durationMs // "not_available"' "$json_capture")"
  usage_summary="$(jq -r '"input=" + ((.meta.agentMeta.usage.input // "na") | tostring) + ", output=" + ((.meta.agentMeta.usage.output // "na") | tostring) + ", total=" + ((.meta.agentMeta.usage.total // "na") | tostring)' "$json_capture")"

  cat > "$output_file" <<EOF
# Raw Agent Run Log

- \`run_id\`: $run_id
- \`case_id\`: $case_id
- \`variant_id\`: $VARIANT_ID
- \`level\`: $LEVEL
- \`agent_name\`: $AGENT_NAME
- \`model\`: $model
- \`model_provider\`: $model_provider
- \`openclaw_build_or_version\`: $OPENCLAW_VERSION
- \`channel\`: $CHANNEL
- \`temperature\`: not_supported
- \`top_p\`: not_supported
- \`max_tokens\`: not_supported
- \`seed\`: not_supported
- \`tools_enabled\`: packet_grounded_with_tools
- \`closed_book\`: false
- \`timestamp\`: $timestamp_local
- \`input_file\`: $input_file
- \`system_prompt_summary\`: $system_prompt_summary
- \`contamination_status\`: unknown
- \`contamination_reason\`: pending pilot review
- \`status\`: $status

## Raw Agent Output

$final_output

## Tool Log Summary

$tool_log_summary

## Operator Notes

- CLI timeout seconds: $TIMEOUT_SECONDS
- Thinking: $THINKING
- Duration ms: $duration_ms
- Usage: $usage_summary
- Session log snapshot: outputs/.tmp_openclaw/$(basename "$session_capture")
EOF

  notes="pilot batch level2; timeout=${TIMEOUT_SECONDS}; thinking=${THINKING}; pending review"
  csv_row="$run_id,$case_id,$VARIANT_ID,$LEVEL,$AGENT_NAME,$model,$model_provider,$OPENCLAW_VERSION,not_supported,not_supported,not_supported,not_supported,packet_grounded_with_tools,false,$CHANNEL,$timestamp_local,$input_file,outputs/raw_agent_logs/pilot/$(basename "$output_file"),$status,unknown,pending pilot review,$notes"
  append_manifest_row "$csv_row"
done

echo "Pilot Level 2 batch completed."
