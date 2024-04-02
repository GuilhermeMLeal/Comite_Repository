import re

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Person): return self.name == other.name and self.age == other.age
        else: return False

def validate_person(person):
    name_pattern = r'^[A-Za-z\s]+$'
    age_pattern = r'^\d{2}$'

    if re.match(name_pattern, person.name) and re.match(age_pattern, str(person.age)):
        return True
    else:
        return False

if __name__ == "__main__":
    person = Person("Guilherme Martins", 20)
    if validate_person(person):
        print("Person válido")
    else:
        print("Person inválido")
