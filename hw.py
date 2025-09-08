class Dog:
    animal = "Dog"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
    
obj_black = Dog("Max", 3, "Shih Tzu")
obj_white = Dog("Joy", 5, "German Shepherd")

print("Max is a {}".format(obj_black.animal))
print("Joy is a {}".format(obj_white.animal))

print("{} is {} years old.".format(obj_black.name, obj_black.age))
print("{} is {} years old.".format(obj_white.name, obj_white.age))

print("{} is a {}.".format(obj_black.name, obj_black.breed))
print("{} is a {}.".format(obj_white.name, obj_white.breed))