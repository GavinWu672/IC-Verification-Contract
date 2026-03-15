# Fact Intake

This document defines the minimum path for turning real DUT/interface material
into contract facts that AI sessions can safely consume.

## Goal

Move from:

- prose-only DUT knowledge
- hand-waved clock/reset assumptions
- implicit signal naming

to:

- machine-readable `facts/signal_map.json`
- explicit checklist facts
- reviewer-traceable source references

## Phase-1 Intake Scope

For the current Cocotb-oriented slice, fact intake only needs to answer:

1. What is the top module?
2. What are the real clock and reset signals?
3. What signals may the testbench legally access?
4. What reset polarity is expected?

## Recommended Source Order

1. RTL top module or interface file
2. block-level verification plan
3. integration or bring-up notes
4. signal table exported from spec or spreadsheet

## Update Path

1. Record source files in `SOURCE_INVENTORY.md`
2. Fill missing fields in `FACT_INTAKE_WORKSHEET.md`
3. Update `facts/signal_map.json`
4. Reflect confirmed facts in:
   - `IC_VERIFICATION_CHECKLIST.md`
   - `memory/02_project_facts.md`
   - `memory/03_decisions.md` when assumptions are needed

## Do Not Do This Yet

- Do not expand immediately into full protocol timing semantics
- Do not build a huge register-map or waveform platform first
- Do not create more validators until real fact intake reveals a repeated need
