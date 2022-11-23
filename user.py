class User:                         #creación de la clase usuario
    firstname = ""                  #declaración de propiedad "firstname"
    lastname = ""                   #declaración de la propiedad "apellido"
    def get_fullname (self):              #declaración del método, lleva el self para que se hagan a si mismo
        return self.firstname+self.lastname

