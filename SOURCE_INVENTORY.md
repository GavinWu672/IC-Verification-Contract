# Source Inventory

Use this file to record where each real verification fact came from.

## RTL / Interface Sources

| Fact Area | Current Source | Status | Notes |
| --- | --- | --- | --- |
| TOP_MODULE | demo value in `facts/signal_map.json` | placeholder | replace with real RTL source |
| CLOCK_SIGNAL | demo value in `facts/signal_map.json` | placeholder | replace with real interface definition |
| RESET_SIGNAL | demo value in `facts/signal_map.json` | placeholder | replace with real interface definition |
| RESET_POLARITY | demo value in `facts/signal_map.json` | placeholder | confirm from reset strategy |

## Verification Sources

| Fact Area | Current Source | Status | Notes |
| --- | --- | --- | --- |
| TESTBENCH_STYLE | Cocotb Phase-1 decision | confirmed | current narrow slice |
| SCOREBOARD_MODEL | not yet defined | pending | add once real DUT workflow exists |
| SIGNAL_MAP_FILE | `facts/signal_map.json` | confirmed | machine-readable contract source |

## Future Extensions

Record future source locations here for:

- protocol timing assumptions
- scoreboard/golden-model ownership
- simulator or CI runner assumptions
