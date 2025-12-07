"""Replaces the PII text entity with the PII's initials"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """Shortens the string to initials"""

    def operate(self, text: str = None, params: Dict = None) -> str:
        """:return: the acronymized text."""
        return ""

    def validate(self, params: Dict = None) -> None:
        """Initial needs some parameter validation implementation. TBD."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize