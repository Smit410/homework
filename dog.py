class Dog:
    animal = "dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour


dog1 = Dog("Pug", "Black")
dog2 = Dog("Labrador", "Golden")
print(dog1.animal, dog1.breed, dog1.colour)
print(dog2.animal, dog2.breed, dog2.colour)
