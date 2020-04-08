class Animal:
    # pass #<- Pass does nothing...use this when you need a block but don't need it yet
    # This is a type of an object that makes an animal
    # This is not an animal, it is a BLUEPRINT for an animal
    def __init__(self):  # Constructor
        print("Constructor called!")
        self.leg_count = 4
    # def get_leg_count(self): # getter
        # return self.leg_count
    # def set_leg_count(self, leg_count): # setter
        #self.leg_count = leg_count


cat = Animal()  # Construct a new Animal, Instantiate a new Animal
dog = Animal()  # Construct a new Animal
# ^^
# Object
# A new instance of an animal
# "cat" is an animal
rabbits = [
    Animal(),
    Animal(),
    Animal(),
]


print(f"Cat's leg count: {cat.leg_count}")
cat.leg_count = 3  # Leg count is an "attribbute" on the object
print(f"Cat's leg count: {cat.leg_count}")

print(f"Rabbit 0's leg count: {rabbits[0].leg_count}")
print(f"Rabbit 1's leg count: {rabbits[1].leg_count}")
print(f"Rabbit 2's leg count: {rabbits[2].leg_count}")

rabbits[1].leg_count = 3
print(f"Rabbit 1's leg count: {rabbits[1].leg_count}")

# You can also make it so you enter count as a parameter like so:
# Class Animal:
# def __init__(self, leg_count):
# self.leg_count = leg_count
# centipede = Animal(100)

# You can also mix hard coded vs pass arguments in like so:


class Animal2:
    def __init__(self, leg_count):
        self.leg_count = leg_count
        self.likes_food = True


centipede = Animal2(100)
print(f"Centipede leg count: {centipede.leg_count}, {centipede.likes_food}")

#l = cat.get_leg_count()
# print(l)

# cat.set_leg_count(3)
# print(l)
