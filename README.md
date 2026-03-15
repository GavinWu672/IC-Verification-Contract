# IC-Verification-Contract

This repository is the first `IC / verification` domain contract for
`ai-governance-framework`.

The initial slice is intentionally narrow:

- Cocotb-style signal mapping
- startup fact injection
- one machine-readable signal-map validator

It is not trying to solve the full IC verification stack in one step.

## Scope

This contract is meant to reduce a very specific Way B failure mode:

- AI knows Python syntax well
- AI does not know the DUT signal names, directions, reset policy, or local
  verification assumptions unless they are explicitly supplied

## Current Contents

- `contract.yaml`
- `AGENTS.md`
- `IC_VERIFICATION_CHECKLIST.md`
- `IC_VERIFICATION_ARCHITECTURE.md`
- `FACT_INTAKE.md`
- `SOURCE_INVENTORY.md`
- `FACT_INTAKE_WORKSHEET.md`
- `WORKFLOW.md`
- `VALIDATION_REQUIREMENTS.md`
- `facts/signal_map.json`
- `rules/ic-verification/safety.md`
- `validators/signal_map_validator.py`
- `validators/clock_reset_validator.py`
- `fixtures/`

## Minimal Verification Flow

From the framework repo:

```bash
python governance_tools/domain_contract_loader.py --contract D:/IC-Verification-Contract/contract.yaml --format human
python runtime_hooks/core/session_start.py --contract D:/IC-Verification-Contract/contract.yaml --format human
python runtime_hooks/core/pre_task_check.py --project-root D:/IC-Verification-Contract --contract D:/IC-Verification-Contract/contract.yaml --format human
python runtime_hooks/core/post_task_check.py --contract D:/IC-Verification-Contract/contract.yaml --checks-file D:/IC-Verification-Contract/fixtures/unknown_signal.checks.json --file D:/IC-Verification-Contract/fixtures/post_task_response.txt --format json
```

## Current Position

This is a prototype contract repo.

The first milestone is not full protocol correctness. It is:

- contract load works
- domain documents inject correctly
- external rules activate
- multiple validators can review both DUT signal access and clock/reset declarations

The repo now includes:

- an unknown-signal advisory baseline
- a missing clock/reset declaration advisory baseline
- a clean baseline where both validators return `ok=True`

The current fixture flow uses `LANG = Python` in its governance contract so the
repo reflects real Cocotb-style outputs instead of relying on a workaround
language label.

## Next Practical Step

Use the new fact-intake documents to replace the demo DUT facts with a real
signal map from your RTL or interface specification.
