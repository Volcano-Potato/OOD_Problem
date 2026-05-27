#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 <batch_spec_csv> [timeout_seconds]" >&2
  exit 1
fi

SPEC_CSV="$1"
TIMEOUT_SECONDS="${2:-86400}"
REPO_ROOT="/Users/jiangcanxiang/Documents/OOD_Problem"
TMP_DIR="$REPO_ROOT/outputs/raw_agent_logs/tmp_json"
THINKING_LEVEL="${THINKING_LEVEL:-high}"
MODEL_OVERRIDE="${MODEL_OVERRIDE:-}"
MODEL_SHORT="${MODEL_SHORT:-}"
DRY_RUN="${DRY_RUN:-false}"

if [[ ! -f "$SPEC_CSV" ]]; then
  echo "Spec CSV not found: $SPEC_CSV" >&2
  exit 1
fi

mkdir -p "$TMP_DIR"

if [[ -z "$MODEL_SHORT" ]]; then
  if [[ -n "$MODEL_OVERRIDE" ]]; then
    model_basename="${MODEL_OVERRIDE##*/}"
    MODEL_SHORT="$(printf '%s' "$model_basename" | tr '[:upper:]' '[:lower:]' | tr -cd '[:alnum:]')"
  else
    MODEL_SHORT="deepseekv4pro"
  fi
fi

run_index=0

while IFS=, read -r case_id variant_id input_file split enabled notes; do
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
  run_id="RUN_${run_stamp}_openclaw_${MODEL_SHORT}_isolated"
  session_id="isolated_${stamp}_$$_${run_index}"
  level="$variant_id"

  json_path_rel="outputs/raw_agent_logs/tmp_json/${case_id}_${variant_id}_${run_id}.json"
  stderr_path_rel="outputs/raw_agent_logs/tmp_json/${case_id}_${variant_id}_${run_id}.stderr.log"
  json_path_abs="$REPO_ROOT/$json_path_rel"
  stderr_path_abs="$REPO_ROOT/$stderr_path_rel"
  mkdir -p "$(dirname "$json_path_abs")"

  timestamp_human="$(date '+%Y-%m-%dT%H:%M:%S%z')"

  echo "==> [$run_index] case=$case_id variant=$variant_id split=$split run_id=$run_id"

  if [[ "$DRY_RUN" == "true" ]]; then
    echo "DRY_RUN: would execute $input_file with session_id=$session_id"
    continue
  fi

  set +e
  SESSION_ID_OVERRIDE="$session_id" \
  MODEL_OVERRIDE="$MODEL_OVERRIDE" \
  THINKING_LEVEL="$THINKING_LEVEL" \
  "$REPO_ROOT/scripts/run_isolated_packet.sh" "$input_file" "$TIMEOUT_SECONDS" >"$json_path_abs" 2>"$stderr_path_abs"
  run_exit_code=$?
  set -e

  OPENCLAW_RUN_EXIT_CODE="$run_exit_code" \
  "$REPO_ROOT/scripts/postprocess_openclaw_run.py" \
    --repo-root "$REPO_ROOT" \
    --json-path "$json_path_rel" \
    --stderr-path "$stderr_path_rel" \
    --run-id "$run_id" \
    --case-id "$case_id" \
    --variant-id "$variant_id" \
    --level "$level" \
    --split "$split" \
    --input-file "$input_file" \
    --session-id "$session_id" \
    --timestamp "$timestamp_human" \
    --timeout-seconds "$TIMEOUT_SECONDS" \
    --thinking-level "$THINKING_LEVEL"
done < "$SPEC_CSV"
