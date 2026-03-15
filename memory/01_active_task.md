# Active Task

- Establish the first minimal `IC-Verification-Contract` slice.
- Keep the scope narrow: Cocotb signal-map governance first.
- Validate contract loading, session-start context, rule activation, and one
  advisory signal-map validator before expanding deeper into IC verification.
- Framework-side validation has now reached:
  - contract load
  - session-start context injection
  - pre-task rule activation
  - post-task advisory validator execution
- The current contract now has two advisory validators:
  - `signal_map_validator`
  - `clock_reset_validator`
- The next useful work is no longer more demo validators.
- The next useful work is replacing placeholder DUT facts with real source-backed
  values through the fact-intake path.
