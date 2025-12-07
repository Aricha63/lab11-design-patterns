"""Replaces the PII text entity with the PII's initials"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """Shortens the string to initials"""

    def operate(self, text: str, params: Dict = None) -> str:
        """:return: the acronymized text."""
        initials_parts = text.split()

        for i in range(len(initials_parts)):
            initials_parts[i] = initials_parts[i][0:1] + "."

        initials_final = " ".join(initials_parts)

        return initials_final

    def validate(self, params: Dict = None) -> None:
        """Initial does not require any parameters so no validation is needed."""
        pass

    def operator_name(self) -> str:
        """Return operator name."""
        return "initial"

    def operator_type(self) -> OperatorType:
        """Return operator type."""
        return OperatorType.Anonymize