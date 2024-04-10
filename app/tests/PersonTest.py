import pytest
from app.PersonEntity import Person, ValidInformation

class TestPerson:

    def test_person_equal(self):
        # Given
        varTest = Person("Guilherme", 19, "(15) 98130-9032")

        # When
        result = Person("Guilherme", 19, "(15) 98130-9032")

        # Then
        assert result == varTest

    def test_peson_validate(self):
        # Given
        varTest = Person("Joao", 80, "(15) 98130-9032")

        # When 
        valid_data = ValidInformation.validate_person(varTest)

        # Then
        assert valid_data == True
