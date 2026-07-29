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
print(type("Soy un dato str"))  # Tipo 'str'
print(type(5))  # Tipo 'int'
print(type(1.5))  # Tipo 'float'
print(type(3 + 1j))  # Tipo 'complex'
print(type(True))  # Tipo 'bool'
print(type(print("Mi cadena de texto")))  # Tipo 'NoneType' → print es una función del sistema que realiza una acción, no devuelve ningún valor (su valor de retorno es None)
