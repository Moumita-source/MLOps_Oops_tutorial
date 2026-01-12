class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound") 

class Dog(Animal):

    def __init__(self, name, behaviour):
        super().__init__(name)
        self.behaviour = behaviour

    def speak(self):
        print(f"{self.name} barks. His behaviour is very {self.behaviour}")


animal = Animal("Generic Animal")
animal.speak()

dog = Dog("Buddy", "rude")
dog.speak()