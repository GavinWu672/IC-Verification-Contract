#!/usr/bin/env python3
"""
Advisory validator for Cocotb-style DUT signal access.
"""

from __future__ import annotations

import json
from pathlib import Path

from governance_tools.validator_interface import DomainValidator, ValidatorResult


class SignalMapValidator(DomainValidator):
    @property
    def rule_ids(self) -> list[str]:
        return ["ic-verification", "ICV-001"]

    def validate(self, payload: dict) -> ValidatorResult:
        checks = payload.get("checks", {}) or {}
        signal_accesses = checks.get("signal_accesses", []) or []
        signal_map = self._load_signal_map()
        known_signals = set(signal_map.get("signals", {}).keys())

        if not signal_accesses:
            return ValidatorResult(
                ok=True,
                rule_ids=self.rule_ids,
                evidence_summary="No machine-readable signal accesses supplied",
                metadata={
                    "mode": "advisory",
                    "known_signal_count": len(known_signals),
                },
            )

        warnings = [
            f"ICV-SIG-001: unknown DUT signal '{signal_name}'"
            for signal_name in signal_accesses
            if signal_name not in known_signals
        ]
        return ValidatorResult(
            ok=len(warnings) == 0,
            rule_ids=self.rule_ids,
            warnings=warnings,
            evidence_summary=f"Checked {len(signal_accesses)} signal references against {len(known_signals)} known DUT signals",
            metadata={
                "mode": "advisory",
                "signal_accesses": signal_accesses,
                "known_signals": sorted(known_signals),
            },
        )

    def _load_signal_map(self) -> dict:
        signal_map_path = Path(__file__).resolve().parent.parent / "facts" / "signal_map.json"
        return json.loads(signal_map_path.read_text(encoding="utf-8"))
