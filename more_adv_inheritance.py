class Animal:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(f"Hi !! My name is {self.name}")


class Fish(Animal):

    def swim(self):
        print(f"{self.name} can swim !!") 

    def print_name(self):
        print(f"My name is {self.name}")

class Lion(Animal):

    def walk(self):
        print(f"{self.name} can walk !!")

    def print_name(self):
        print(f"My name is {self.name}")


class Reptile(Fish, Lion):

    def stay(self):
        print(f"I can stay in both Land and Water !!")
        super().print_name()

obj = Reptile("Crocodile")
obj.stay()        

