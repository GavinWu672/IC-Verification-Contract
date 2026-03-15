# Decisions

## 2026-03-15

- Start with one `IC-Verification-Contract` repo rather than separate Cocotb /
  golden-model / toolchain repos.
- Use a narrow Cocotb signal-map slice first.
- Promote the first machine-readable validator into a hard-stop candidate once
  the signal map is available in JSON form.
- Add a second advisory validator for explicit clock/reset declaration before
  expanding into protocol timing or golden-model validation.
- Add a fact-intake workflow before expanding the domain again, so the next
  improvement is grounded in real DUT facts rather than more synthetic examples.

## 2026-03-15 - Enforcement Update

- `ICV-001` is now recorded as a `hard_stop_rule` in `contract.yaml`.
- Unknown DUT signal access now routes through `violations` instead of
  reviewer-only warnings because the signal-map facts are already
  machine-readable.
- Clock/reset declaration checks remain advisory until real project facts make
  their enforcement surface less heuristic.
