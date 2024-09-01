class Dog:
    def __init__(self, name, favorite_toy="Iron-man toy"):
        self.name = name
        self.favorite_toy = favorite_toy
    
    def bark(self):
        print("Woof!")
    def get_adopted(self, owner_name):
        self.owner = owner_name

mojo = Dog("Mojo")
mojo.get_adopted("Mildred Gichuki")
print(mojo.owner + "" + " has adopted Mojo.")
print(mojo.favorite_toy)
print(mojo.owner + "" + " bought an " + mojo.favorite_toy)

snoopy = Dog("Snoopy", "Baby frog")
snoopy.get_adopted("Zahra Wangari")
print(snoopy.owner + "" + " has bought Snoopy a " + snoopy.favorite_toy)
print(snoopy.name)
snoopy.bark()
