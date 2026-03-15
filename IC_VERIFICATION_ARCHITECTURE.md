# IC Verification Architecture

## Current Boundary

This contract currently covers:

- startup context injection for DUT interface facts
- external rule activation for IC verification review
- post-task advisory validation for unknown signal access

It does not yet cover:

- full protocol timing validation
- waveform semantic analysis
- golden-model numerical equivalence
- internal EDA toolchain orchestration

## Phase-1 Cocotb Boundary

The first slice is intentionally narrow.

The framework should help reviewers answer:

1. Did the AI reference real DUT signals?
2. Did it preserve the declared clock/reset assumptions?
3. Did it avoid inventing an interface that is not in the facts?
