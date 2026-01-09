# x = 7
# i = 0

# while i < x  :
#     print(i)
#     i=i+1

# for x in [3,6,9,23,54]:
#     print("Tru", x)

# l = [('Hi '+ x)for x in ['Anddy', 'Priya','kunal']]
# print(l)

# squ = {x**2 for x in [0,2,5] if x<9}
# print(squ)
# print(sorted(squ))

class Dog:
    species = ["Canis Lupus"]
    def __init__(self, name , color):
        self.name = name
        self.state = 'Sleeping'
        self.color = color
    
    def command(self, x):
        if x == self.name:
            self.bark(2)
        elif x == "Sit":
            self.state = "Sit"
        else:
            self.state = "Wag Tail"
    
    def bark(self, freq):
        for i in range(freq):
            print("[ " + self.name + " ] : Woof!")
    
bello = Dog("Bello","Black")
alice = Dog("Alice","White")

print(bello.name+" is "+bello.color+" in color.")
print(alice.name+" is "+alice.color+" in color.")

bello.bark(3)

alice.command("Sit")
print("[ Alice ] : "+ alice.state)

bello.command = ("no")

print("[ Bello ] : "+ bello.state)

alice.command("Alice")

bello.species +=["Wulf"]
print(len(bello.species)==len(alice.species), bello. species)
