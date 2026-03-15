# Decisions

## 2026-03-15

- Start with one `IC-Verification-Contract` repo rather than separate Cocotb /
  golden-model / toolchain repos.
- Use a narrow Cocotb signal-map slice first.
- Keep the first validator advisory-only.
- Add a second advisory validator for explicit clock/reset declaration before
  expanding into protocol timing or golden-model validation.
- Add a fact-intake workflow before expanding the domain again, so the next
  improvement is grounded in real DUT facts rather than more synthetic examples.
