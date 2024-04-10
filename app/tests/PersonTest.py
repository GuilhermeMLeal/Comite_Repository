import pytest
from app.PersonEntity import Person, ValidInformation

class TestPerson:

    def test_person_equal():
        # Given
        varTest = Person("Guilherme", 19, "(15) 98130-9032")

        # When
        result = Person("Guilherme", 19, "(15) 98130-9032")

        # Then
        assert result == varTest

    def test_peson_validate():
        # Given
        varTest = Person("Joao", 80, "(15) 98130-9032")

        # When 
        is_valid = ValidInformation.validate_person(varTest)

        # Then
        assert is_valid == True
