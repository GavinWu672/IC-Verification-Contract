# IC Verification Safety

## ICV-001 - signal-map-must-match-contract

- Cocotb or verification code must reference only DUT signals present in the
  contract signal map
- Required evidence: `signal_map_review`

## ICV-002 - clock-reset-must-be-explicit

- Clock and reset assumptions must be stated explicitly in review notes or
  machine-readable facts
- Required evidence: `clock_reset_review`
