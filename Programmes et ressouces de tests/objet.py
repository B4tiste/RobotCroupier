class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
        
    def __str__(aze):
        return str(aze)

    def introduce_self(self):
        print("My name is " + self.name)


class Person:
    def __init__(self, n, p, i, r):
        self.name = n
        self.personality = p
        self.isSitting = i
        self.robot_owned = r
    
    def presentation(self):
        print("My name is " + self.name + " and I own " + self.robot_owned.name)


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)

p1 = Person("Alice", "aggressive", False, r2)
p2 = Person("Becky", "gentle", True, r1)

p1.robot_owned.introduce_self()
p2.presentation()

