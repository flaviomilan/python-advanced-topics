from descriptors import number, string


class Person:
    """
    Example class using descriptors 
    for validate and format attributes
    """
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    first_name = string.UpperCase()
    last_name = string.UpperCase()
    age = number.Positive()

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == "__main__":
    """
    Testing
    """
    person = Person(first_name="Nikola", last_name="Tesla", age=50)
    print(f"NAME: {person.name} - AGE: {person.age}")

    try:
        person.age = -1
    except ValueError:
        print(f"Problem when set negative value")
