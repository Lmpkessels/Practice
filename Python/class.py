class Person():
    """Innitializing attributes to declare a name and age."""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        """Greeting user"""
        print(f"Hello my name is {self.name.title()} and I'm {self.age} "
              "years old.")
        
# Person and his age.
luuk = Person(name="luuk", age=25)

# Greeting person.
luuk.greet()