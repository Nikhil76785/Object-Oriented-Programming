class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
obj_blue = Parrot("Blue", 10)
obj_red = Parrot("Red", 12)

print("Blue is a {}".format(obj_blue.species))
print("Red is a {}".format(obj_red.species))

print("{} is {} years old.".format(obj_blue.name, obj_blue.age))
print("{} is {} years old.".format(obj_red.name, obj_red.age))