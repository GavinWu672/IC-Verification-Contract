# PLAN

> **最後更新**: 2026-03-15
> **Owner**: GavinWu
> **Freshness**: Sprint (7d)

## Goal

Establish the first minimal `IC-Verification-Contract` slice that the
`ai-governance-framework` can load without framework modifications.

## Current Phase

Phase 1: Cocotb-oriented signal-map governance.

## Deliverables

- `contract.yaml`
- machine-readable `facts/signal_map.json`
- first advisory validator for unknown signal access
- minimal startup and reviewer documentation

## Next Step

Validate this repo through:

1. `domain_contract_loader.py --contract contract.yaml`
2. `session_start.py --contract contract.yaml`
3. `pre_task_check.py --contract contract.yaml`
4. `post_task_check.py --contract contract.yaml --checks-file fixtures/unknown_signal.checks.json`
