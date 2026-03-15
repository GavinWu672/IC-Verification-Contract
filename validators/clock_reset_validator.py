#!/usr/bin/env python3
"""
Advisory validator for explicit clock/reset declarations.
"""

from __future__ import annotations

import json
from pathlib import Path

from governance_tools.validator_interface import DomainValidator, ValidatorResult


class ClockResetValidator(DomainValidator):
    @property
    def rule_ids(self) -> list[str]:
        return ["ic-verification", "ICV-002"]

    def validate(self, payload: dict) -> ValidatorResult:
        checks = payload.get("checks", {}) or {}
        signal_map = self._load_signal_map()
        expected_clock = signal_map.get("clock_signal")
        expected_reset = signal_map.get("reset_signal")
        expected_polarity = signal_map.get("reset_polarity")

        declared_clock = checks.get("declared_clock_signal")
        declared_reset = checks.get("declared_reset_signal")
        declared_polarity = checks.get("declared_reset_polarity")

        warnings: list[str] = []
        if not declared_clock:
            warnings.append("ICV-CLKRST-001: missing declared clock signal")
        elif declared_clock != expected_clock:
            warnings.append(
                f"ICV-CLKRST-002: declared clock '{declared_clock}' does not match contract '{expected_clock}'"
            )

        if not declared_reset:
            warnings.append("ICV-CLKRST-003: missing declared reset signal")
        elif declared_reset != expected_reset:
            warnings.append(
                f"ICV-CLKRST-004: declared reset '{declared_reset}' does not match contract '{expected_reset}'"
            )

        if not declared_polarity:
            warnings.append("ICV-CLKRST-005: missing declared reset polarity")
        elif declared_polarity != expected_polarity:
            warnings.append(
                f"ICV-CLKRST-006: declared reset polarity '{declared_polarity}' does not match contract '{expected_polarity}'"
            )

        return ValidatorResult(
            ok=len(warnings) == 0,
            rule_ids=self.rule_ids,
            warnings=warnings,
            evidence_summary="Checked explicit clock/reset declarations against signal-map facts",
            metadata={
                "mode": "advisory",
                "expected_clock_signal": expected_clock,
                "expected_reset_signal": expected_reset,
                "expected_reset_polarity": expected_polarity,
                "declared_clock_signal": declared_clock,
                "declared_reset_signal": declared_reset,
                "declared_reset_polarity": declared_polarity,
            },
        )

    def _load_signal_map(self) -> dict:
        signal_map_path = Path(__file__).resolve().parent.parent / "facts" / "signal_map.json"
        return json.loads(signal_map_path.read_text(encoding="utf-8"))
