class Animal:
    def move(self):
        print("This animal moves.")

class Dog(Animal):
    def move(self):
        print("Dog runs on four legs 🐶")

class Bird(Animal):
    def move(self):
        print("Bird flies in the sky 🐦")

class Fish(Animal):
    def move(self):
        print("Fish swims in the water 🐟")

animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
