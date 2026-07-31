# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Hola Mundo ###


# Print Function
Mostrar información en la pantalla
print('Hello world!')

print('My favorite colors are', 'blue', 'green', 'red')  # Output: My favorite colors are blue green red
# Python agrega automáticamente un espacio entre cada item cuando los separas con comas 

--- Comentarios: para explicar tu código, dejarte recordatorios o aclarar por qué existe una línea.
NO deberían usarse para explicar nombres de variables, estos ya deben ser descriptivos.
  
# Esto es un comentario
x = 56 # Esto también es un comentario → Python ignora todo después del # en esa línea

"""
Este es un
comentario
en varias líneas
"""

'''
Este también es un
comentario
en varias líneas
'''

# Este también es un 
# comentario
# en varias líneas


# Cómo consultar el tipo de dato
- Type
Devuelve el tipo exacto de objeto.
print(type('str'))
print(type(5))
print(type(nombre_variable))

print(is_student, type(is_student)) # print y mostrar el type en una sola función

- isinstance
Verifica si un objeto es de una clase o subclase. Toma tu objeto y tipo que quieres revisar y regres un boolean True/False.

account_balance = '12'
print(isinstance(account_balance, int)) # False

account_balance = 12
print(isinstance(account_balance, (int, float))) # True (revisó si es int or float)


