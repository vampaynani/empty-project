from user import User

user = User()
user.firstname = "John"
user.lastname = "Doe"
print(user.get_fullname())
# John Doe