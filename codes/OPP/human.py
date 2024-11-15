class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def __str__(self):
        return "A Human with name " + self.name + "," + " his age is " + str(self.age) + "."
    
h = Human(age=28, name = "Felipe")

print(h)