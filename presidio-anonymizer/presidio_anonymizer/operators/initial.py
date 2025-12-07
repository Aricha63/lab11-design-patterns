"""Replaces the PII text entity with the PII's initials"""

from typing import Dict

from presidio_anonymizer.operators import Operator, OperatorType

class Initial(Operator):
    """Shortens the string to initials"""

    def operate(self, text: str, params: Dict = None) -> str:
        """:return: the acronymized text."""

        # splits the given text into multiple words
        initials_parts = text.split()

        # Goes through each word in the list
        for i in range(len(initials_parts)):
            part = initials_parts[i] # the current word to acronymize

            first_alnum=0 # location of first alphanumeric char; this is an initialization and a guess
            
            # loops until it finds first alphanumeric character, breaks when it does
            while not part[first_alnum].isalnum():
                first_alnum+=1

            # slices the correct portion of the current word, adds a period, and rewrites to the list
            initials_parts[i] = part[0:first_alnum+1].upper() + "."
            
        # creates a new list to join each acronymized part
        initials_final = " ".join(initials_parts)

        #returns the final result
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