class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Child(Parent):

    def __init__(self, name, gift):
        super().__init__(name)
        self.gift = gift
        
    def play(self):
        print(f"{self.name} is playing") 


child = Child("Alice", "Chocolate")
child.play()
