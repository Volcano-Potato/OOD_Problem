#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 <batch_spec_csv> [timeout_seconds]" >&2
  exit 1
fi

SPEC_CSV="$1"
TIMEOUT_SECONDS="${2:-1800}"
REPO_ROOT="/Users/jiangcanxiang/Documents/OOD_Problem"
THINKING_LEVEL="${THINKING_LEVEL:-high}"
DRY_RUN="${DRY_RUN:-false}"

if [[ ! -f "$SPEC_CSV" ]]; then
  echo "Spec CSV not found: $SPEC_CSV" >&2
  exit 1
fi

run_index=0

while IFS=, read -r case_id variant_id input_file enabled notes; do
  if [[ "$case_id" == "case_id" ]]; then
    continue
  fi

  enabled_trimmed="$(printf '%s' "$enabled" | tr '[:upper:]' '[:lower:]' | xargs)"
  if [[ "$enabled_trimmed" != "true" ]]; then
    continue
  fi

  run_index=$((run_index + 1))
  stamp="$(date '+%Y%m%d_%H%M%S')"
  run_stamp="${stamp}_$(printf '%02d' "$run_index")"
  run_id="RUN_${run_stamp}_openclaw_deepseekv4pro_researchagentv2search"

  echo "==> [$run_index] case=$case_id variant=$variant_id run_id=$run_id"

  if [[ "$DRY_RUN" == "true" ]]; then
    echo "DRY_RUN: would run $input_file"
    continue
  fi

  python3 "$REPO_ROOT/scripts/run_research_agent_v2.py" \
    --input-file "$input_file" \
    --timeout-seconds "$TIMEOUT_SECONDS" \
    --thinking-level "$THINKING_LEVEL"

  latest_run_dir="$(find "$REPO_ROOT/outputs/raw_agent_logs/research_agent_v2" -maxdepth 1 -type d -name "${case_id}_${variant_id}_*" | sort | tail -n 1)"
  if [[ -z "$latest_run_dir" ]]; then
    echo "No run directory found for $case_id $variant_id" >&2
    exit 1
  fi

  python3 "$REPO_ROOT/scripts/postprocess_research_agent_v2_run.py" \
    --run-dir "$latest_run_dir" \
    --run-id "$run_id" \
    --input-file "$input_file" \
    --timeout-seconds "$TIMEOUT_SECONDS" \
    --thinking-level "$THINKING_LEVEL"
done < "$SPEC_CSV"
