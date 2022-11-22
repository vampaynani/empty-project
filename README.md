# Requerimientos

## Usuario
1. Puedo crear una instancia de usuario
```python
user = User()
```

2. Puedo asignar nombre y apellido a ese usuario, así como obtener su nombre completo
```python
user.firstname = "John"
user.lastname = "Doe"
print(user.get_fullname())
# John Doe
```

3. Puedo asignar un año de nacimiento al usuario y obtener su edad
```python
user.birth_year = 2000
print(user.get_age())
# 22
```

## Mascota
1. Puedo crear una instancia de mascota, esta puede ser perro o gato.
Con esta acción le asigno un tipo y un sonido a mi mascota.
```python
pet = Dog()
print(pet.type, pet.sound) # "dog", "barks"
```
```python
pet = Cat()
print(pet.type, pet.sound) # "cat", "meows"
```

2. Puedo asignar un nombre a esa mascota y saber con que sonido saluda
```python
pet.name = "Firulais"
print(pet.greet())
# "Firulais barks"
```

## Interacciones
1. Puedo asignar una mascota a un usuario y saber que es
```python
user.pet = pet
print(user.which_pet())
# "Firulais is a dog"
```

2. El usuario recibe saludos de su mascota 
```python
print(user.pet_greet())
# Firulais barks, when John Doe arrives!
```