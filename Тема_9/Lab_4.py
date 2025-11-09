class Mammal:
    className = "Mammal"

class Dog(Mammal):
    species = "canine"
    sounds = "wow"

class Cat(Mammal):
    species = "feline"
    sounds = "meow"

dog = Dog()
print(f"Dog is {dog.className}, byt they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, byt they say {cat.sounds}")