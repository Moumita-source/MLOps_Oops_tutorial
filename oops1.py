# initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print(f"Started executing attributes")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print(f"Ending executing attributes")

    def travel(self, destination):
        print(f"Starting executing travel method")
        print(f"Employee is now travelling to {destination}")    

# creating an object of the class
sam = employee()

# printing the attributes
# print(sam.id)
# print(sam.salary)
# print(sam.designation)   

# calling the methods
# sam.travel("Siliguri")   

print(type(sam)) 