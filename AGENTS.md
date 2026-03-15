# AGENTS

## IC Verification Guardrails

AI must not assume DUT signal names, widths, or directions.

AI must not invent clock or reset behavior when the contract facts do not define
them.

AI must not claim a Cocotb testbench is valid unless the signal mapping aligns
with the machine-readable facts in `facts/signal_map.json`.

AI must surface uncertainty when:

- the DUT interface is incomplete
- the timing assumption is unclear
- the reset sequence is not explicitly defined

AI should prefer reviewer-assist outputs over false certainty.
