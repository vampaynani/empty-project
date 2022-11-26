from user import User

user = User()
user.firstname = "John"
user.lastname = "Doe"
print(user.get_fullname())
user.birth_year = 2000
print(user.get_age())
# John Doe