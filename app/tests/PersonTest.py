import pytest
from app.PersonEntity import Person, ValidInformation

class TestPerson:

    def test_if_person_is_equal(self):
        # Given
        person = Person("Guilherme", 19, "(15) 98130-9032")
        person_test = Person("Guilherme", 19, "(15) 98130-9032")
        
        # When
        result = person.equal(person_test)

        # Then
        assert result == True

    def test_peson_validate(self):
        # Given
        person = Person("Joao", 80, "(15) 98130-9032")

        # When 
        valid_data = ValidInformation.validate_person(varTest)

        # Then
        assert valid_data == True
