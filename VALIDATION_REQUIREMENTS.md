# Validation Requirements

This repo now mixes one hard-stop baseline with one advisory baseline. The
following checks should pass before claiming the contract is healthy.

## Required

- `contract.yaml` loads successfully
- `session_start` validator preflight is green
- `pre_task_check` activates `ic-verification`
- hard-stop baseline works:
  - unknown signal fixture produces blocking `ICV-SIG-001`
- advisory baseline works:
  - missing clock/reset fixture produces `ICV-CLKRST-*`
- clean baseline works:
  - known signal + declared clock/reset fixture returns `ok=True`

## Command Checklist

```bash
python governance_tools/domain_contract_loader.py --contract D:/IC-Verification-Contract/contract.yaml --format human
python runtime_hooks/core/session_start.py --contract D:/IC-Verification-Contract/contract.yaml --format human
python runtime_hooks/core/pre_task_check.py --project-root D:/IC-Verification-Contract --contract D:/IC-Verification-Contract/contract.yaml --rules common,ic-verification --risk medium --oversight review-required --format human
python runtime_hooks/core/post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/unknown_signal.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --risk medium --oversight review-required --format json
python runtime_hooks/core/post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/clock_reset_missing.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --risk medium --oversight review-required --format json
python runtime_hooks/core/post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/known_signal.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --risk medium --oversight review-required --format json
```
