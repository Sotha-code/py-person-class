class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }

    for person in people:
        instance = persons[person["name"]]

        if "wife" in person and person["wife"]:
            instance.wife = persons.get(person["wife"])
        if "husband" in person and person["husband"]:
            instance.husband = persons.get(person["husband"])

    return list(persons.values())
