class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says Meoew")
    
    def move(self):
        print(f"{self.name} is moving around the house")
    
    def bite(self):
        print(f"{self.name} bit me!")


class Plane:
    def __init__(self, make, model, tail_number):
        self.model = model
        self.make = make
        self.tail_number = tail_number

    def move(self):
        print(f"{self.make} {self.model} with {self.tail_number} is moving")
    
    def fly(self):
        print(f"{self.make} {self.model} with {self.tail_number} is flying")
    
    def land(self):
        print(f"{self.make} {self.model} with {self.tail_number} is landing")


cat_1 = Cat("Whiskers")
cat_2 = Cat("Fluffy")
cat_3 = Cat("Mittens")

plane_1 = Plane("Boeing", "747", "N12345")
plane_2 = Plane("Airbus", "A380", "N54321")
plane_3 = Plane("Cessna", "172", "N98765")

cat_1.move()
plane_1.move()

cat_2.bite()
plane_2.fly()

cat_3.speak()
plane_3.land()