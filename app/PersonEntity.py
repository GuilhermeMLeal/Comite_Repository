import re

class Person:
    def __init__(self, name, age, number) :
        if name is None or age is None or number is None:
            raise Exception("The fields can't be none")
        self.name = name
        self.age = age
        self.number = number

    def __eq__(self, other_person: object) -> bool:
        if isinstance(other_person, Person): return self.name == other_person.name and self.age == other_person.age and self.number == other_person.number
        else: return False

class ValidInformation:

    def validate_person(person):
        name_pattern = r'^[A-Za-z\s]+$'
        age_pattern = r'^\d{2}$'
        number_patten = r'\(\d{2}\)\s\d{5}\-\d{4}'

        if re.match(name_pattern, person.name) and re.match(age_pattern, str(person.age)) and re.match(number_patten, person.number):
            return True
        else:
            return False

if __name__ == "__main__":
    person = Person("Guilherme", 20, "(15) 92211-2131")
    if ValidInformation.validate_person(person):
        print("Pessoa válida")
    else:
        print("Pessoa inválida")
