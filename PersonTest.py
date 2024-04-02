import pytest
from PersonEntity import Person, validate_person


class TestPerson:

    def test_person_equal(self):
        varTest = Person("Guilherme", 19)
        assert Person("Guilherme", 19) == varTest

    def test_peson_validate(self):
        varTest = Person("Joao", 80)
        assert validate_person(varTest) == True
