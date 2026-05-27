#!/usr/bin/env bash

set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $0 <agent_task_file> [timeout_seconds]" >&2
  exit 1
fi

INPUT_FILE="$1"
TIMEOUT_SECONDS="${2:-86400}"
AGENT_ID="benchmark_isolated"
THINKING_LEVEL="${THINKING_LEVEL:-high}"
MODEL_OVERRIDE="${MODEL_OVERRIDE:-}"
WORKDIR="/Users/jiangcanxiang/Documents/OOD_Problem"

if [[ ! -f "$INPUT_FILE" ]]; then
  echo "Input file not found: $INPUT_FILE" >&2
  exit 1
fi

SESSION_ID="${SESSION_ID_OVERRIDE:-isolated_$(date '+%Y%m%d_%H%M%S')_$$}"
MESSAGE_TEXT="$(cat "$INPUT_FILE")"

CMD=(
  openclaw agent
  --agent "$AGENT_ID"
  --local
  --json
  --thinking "$THINKING_LEVEL"
  --timeout "$TIMEOUT_SECONDS"
  --session-id "$SESSION_ID"
  --message "$MESSAGE_TEXT"
)

if [[ -n "$MODEL_OVERRIDE" ]]; then
  CMD+=(--model "$MODEL_OVERRIDE")
fi

"${CMD[@]}"
