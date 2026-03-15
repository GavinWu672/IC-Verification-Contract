# Validation Log

## 2026-03-15

- `domain_contract_loader.py --contract D:/IC-Verification-Contract/contract.yaml --format human`
  - `ok`: load successful
- `session_start.py --contract D:/IC-Verification-Contract/contract.yaml --format human`
  - validator preflight passed
  - validator count: `2`
  - domain documents and behavior override previews were injected
- `pre_task_check.py --project-root D:/IC-Verification-Contract --contract D:/IC-Verification-Contract/contract.yaml --rules common,ic-verification --risk medium --oversight review-required --format human`
  - `ok=True`
  - `contract=ic-verification/medium`
- `post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/unknown_signal.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --risk medium --oversight review-required --format json`
  - `ok=True`
  - advisory validator warning: `ICV-SIG-001: unknown DUT signal 'phantom_debug_o'`
- `post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/known_signal.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --risk medium --oversight review-required --format json`
  - `ok=True`
  - `signal_map_validator` returned `ok=True` with no warnings
  - `clock_reset_validator` returned `ok=True` with no warnings
- `post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/clock_reset_missing.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --risk medium --oversight review-required --format json`
  - `ok=True`
  - advisory validator warnings:
    - `ICV-CLKRST-001`
    - `ICV-CLKRST-003`
    - `ICV-CLKRST-005`
