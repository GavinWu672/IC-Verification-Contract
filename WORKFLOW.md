# Workflow

This file describes the minimal working flow for the current contract.

## Current Flow

1. `session_start`
   - injects IC verification documents
   - preflights external validators
2. `pre_task_check`
   - activates `common,ic-verification`
3. `post_task_check`
   - runs advisory validators:
     - `signal_map_validator`
     - `clock_reset_validator`

## Minimal Commands

From `ai-governance-framework`:

```bash
python governance_tools/domain_contract_loader.py --contract D:/IC-Verification-Contract/contract.yaml --format human
python runtime_hooks/core/session_start.py --contract D:/IC-Verification-Contract/contract.yaml --format human
python runtime_hooks/core/pre_task_check.py --project-root D:/IC-Verification-Contract --contract D:/IC-Verification-Contract/contract.yaml --rules common,ic-verification --risk medium --oversight review-required --format human
python runtime_hooks/core/post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/unknown_signal.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --risk medium --oversight review-required --format json
```

## What Reviewers Should Look For

- unknown DUT signal references
- missing or inconsistent clock/reset declarations
- any place where the AI claims certainty without contract facts
