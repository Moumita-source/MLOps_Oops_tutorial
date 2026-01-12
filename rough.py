lst = [1, 2, 3]
my_str = "mlops playlist"
my_int = 155

# print(type(lst))
# print(type(my_str))
# print(type(my_int))

from oops_proj import chatbook
user1 = chatbook()
# print(user1._chatbook__name)

## getter and setter
# print(user1.get_name())
# user1.set_name("Moumita")
# print(user1.get_name())

## using class to call the static method directly
print(user1.id)
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)
user3 = chatbook()
print(user3.id)