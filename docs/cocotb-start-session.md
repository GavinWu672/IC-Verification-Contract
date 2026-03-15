# Cocotb Start Session

Use this contract when the task involves:

- Cocotb testbench creation
- signal mapping review
- basic DUT bring-up assumptions

Before trusting generated test code, confirm:

1. every referenced signal exists in `facts/signal_map.json`
2. clock/reset assumptions match the checklist
3. any missing interface detail is called out explicitly
