# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc?t=8643

### Strings ###
Secuencia de caracteres envuelta por comillas simples o dobles.
Son immutable data types: puedes reasignar un string distinto a una variable, pero no puedes modificar un string directamente. 

greeting = 'hi'
greeting = 'hello'
print(greeting) # hello

greeting = 'hi'
greeting[0] = 'H' # TypeError: 'str' object does not support item assignment
-

my_string = "Mi String"
my_other_string = 'Mi otro String'

# Indexing. Obtener longitud del string y trabajar con caracteres individuales del string
Index: posición de cada caracter, empezando por 0

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_str = 'Hello world'
print(len(my_str))  # 11

Acceder a un caracter por su index: [#_de_caracter]
my_str = "Hello world"
print(my_str[0])  # H
print(my_str[6])  # w

Negative indexing 
Cuenta de atrás para adelante: -1 es último caracter
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2]) # l

# Multiline strings
my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n escapado"
print(my_scape_string)

# Formateo

Si el str tiene comillas simples o dobles, puedes a) usar el otro tipo de comillas b) usar backslash para escapar las comillas.
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'

msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""

name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo


# Revisar si un string contiene uno o más caracteres
in → regresa boolean diciendo si caracteres existen o no en el string. 

my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False

