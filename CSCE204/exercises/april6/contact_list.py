from person import Person

"""
friend1 = Person("Mason", "Luckiewicz", "724-610-7221")
friend1.display()

friend2 = Person("Sloane", "Luckiewicz", "724-610-7222")
friend2.display()
"""

people = (
    Person("Mason", "Luckiewicz", "724-610-7221"),
    Person("Sloane", "Luckiewicz", "724-610-7222"),
    Person("Kaden", "Luckiewicz", "724-771-1973"),
    Person("Remi", "Luckiewicz", "724-493-9544")
)

for person in people:
    person.display()