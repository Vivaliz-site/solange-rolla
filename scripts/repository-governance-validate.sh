#!/usr/bin/env bash
set -Eeuo pipefail
root="$(git rev-parse --show-toplevel)"
cd "$root"

# Guard CODEOWNERS without requiring the human to approve ordinary PRs.
python3 scripts/check_pr_review_routing.py
python3 -m unittest tests/test_pr_review_routing.py -v
bash scripts/absolute-audit-governance-validate.sh "${1:-manual}"
