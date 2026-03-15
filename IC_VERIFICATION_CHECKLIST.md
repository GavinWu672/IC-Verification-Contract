# IC Verification Checklist

## Required Facts

- [ ] DUT_NAME
- [ ] TOP_MODULE
- [ ] CLOCK_SIGNAL
- [ ] RESET_SIGNAL
- [ ] RESET_POLARITY
- [ ] SIGNAL_MAP_FILE
- [ ] TESTBENCH_STYLE
- [ ] SCOREBOARD_MODEL

## Current Phase-1 Assumptions

- Focus on Cocotb-style signal mapping
- Use machine-readable facts from `facts/signal_map.json`
- Treat validator results as advisory until domain confidence grows
