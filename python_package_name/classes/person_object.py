"""
Example Class. All files should have comments to start them
"""

class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        """
        Initializer for a class
        :param name: Name of person
        :param age: Age of person
        """
        self.name = name
        self.age = age

    def __eq__(self, other: "Person") -> bool:
        """
        See if two Person objects are the same
        :param other: Other Person object
        """
        return self.name == other.name and self.age == other.age

    def __repr__(self) -> str:
        """
        If a developer were to iterate a Person() object, what should it print?
        :return string representation
        """
        return f"{self.__class__.__name__}@{hex(id(self))}"
