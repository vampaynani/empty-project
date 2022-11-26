from datetime import datetime

class User:
    firstname=""
    lastname=""
    birth_year=0
    pet=None

    def get_fullname(self):
        return self.firstname+" "+self.lastname
    
    def get_age(self):
        return datetime.now().year - self.birth_year

    def which_pet(self):
        return self.pet.name+" is a "+self.pet.type
