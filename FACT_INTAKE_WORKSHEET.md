# Fact Intake Worksheet

Use this worksheet before updating `facts/signal_map.json`.

## Required Fields

| Field | Current Value | Source | Status |
| --- | --- | --- | --- |
| DUT_NAME | `demo_stream_dut` | demo contract fact | placeholder |
| TOP_MODULE | `demo_stream_top` | demo contract fact | placeholder |
| CLOCK_SIGNAL | `clk` | demo contract fact | placeholder |
| RESET_SIGNAL | `rst_n` | demo contract fact | placeholder |
| RESET_POLARITY | `active_low` | demo contract fact | placeholder |
| TESTBENCH_STYLE | `cocotb` | contract scope | confirmed |
| SCOREBOARD_MODEL | _unset_ | _unset_ | pending |

## Signal Map Checklist

- [ ] all externally referenced DUT signals are present in `facts/signal_map.json`
- [ ] each signal has a direction
- [ ] clock signal is explicitly tagged
- [ ] reset signal is explicitly tagged
- [ ] payload / handshake roles are not guessed

## Ready-To-Update Criteria

The worksheet is ready to promote into confirmed facts when:

- the top module source is identified
- clock/reset names are backed by a real source
- placeholder values are replaced or explicitly marked as temporary
