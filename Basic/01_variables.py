# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=2938

### Variables ###
Usar snake_case → texto en minúsculas + separar palabras con guión bajo (underscore). Crearlas cortas.                                                                       
NO está bien en Python usar camel case (unir palabras con letras mayúsculas, e.g. my Variable)
NO usar - @ $
Al ser variable, puede cambiar su valor.

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

# Transformar integer a string (convertir el 5 en un string):
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor:", my_bool_variable)

# Algunas funciones del sistema
len: length → obtener cantidad de elementos o caracteres, devuelve siempre un número entero
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis! Se puede hacer, pero en general no es la mejor práctica porque puedes cometer errores.
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Inputs
Función que detiene la ejecución del programa y espera a que el usuario introduzca datos a través del teclado y esto se guarda como variable tipo string.
Se usa para que un programa sea interactivo y se adapte a lo que el usuario necesita en tiempo real e.g. solicitar username y pasword para inicio de sesión.
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)

# Cambiamos su tipo 
name = 35
age = "Brais"
print(name)
print(age)

# ¿Forzamos el tipo? Type Hints
address: str = "Mi dirección" → ya solo con la scomillas es un str

Esto es un type hint (indicación de tipo) - es una anotación opcional que agregas al código para decir qué tipo de datos debe usar una variable, función o parámetro → para ti en el futuro u otros programadores.
- Python ignora estas notas al ejecutar el código. Si pones un texto en una variable marcada como int, el programa correrá igual sin dar error.
- Tu editor de código puede usar estas pistas para darte un mejor autocomplete y detectar errores mientras escribes

address = True
address = 5      
address = 1.2
print(type(address))
