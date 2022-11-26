from user import User
from dog import Dog
from cat import Cat

user = User()
user.firstname = "John"
user.lastname = "Doe"
print(user.get_fullname())
user.birth_year = 2000
print(user.get_age())
# John Doe
pet = Cat()
print(pet.type, pet.sound) # "dog", "barks"