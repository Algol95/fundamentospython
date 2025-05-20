# 🧪 Fundamentos Python I – Enunciados

# ------------------------------
# TIPOS DE DATOS
# ------------------------------

# ✨ Ejercicio 1: ¿Qué tipo es?
# Declara las siguientes variables y usa type()
# para imprimir qué tipo de dato es cada una:
a = "Hola"
b = 25
c = 3.14
d = True
e = None
print("------------------------------")
print("✨ Ejercicio 1: ¿Qué tipo es?:")
print("------------------------------")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# ✨ Ejercicio 2: Conversión rápida
# Convierte la cadena "42" en número, súmale 8 y muestra el resultado.
# Luego convierte el número 100 en texto y muestra la frase:
# "Tu puntuación final es: 100"

print("----------------------------------")
print("✨ Ejercicio 2: Conversión rápida:")
print("----------------------------------")
num1 = "42"
num1 = int(num1) + 8
print(f"Str a int: {num1}")

num2 = 100
print("Tu puntuación final es: " + str(num2))
# ------------------------------
# VARIABLES
# ------------------------------

# ✨ Ejercicio 3: Nombres y saludos
# Crea una variable nombre y una variable edad.
# Imprime una frase como:
# Hola, me llamo X y tengo Y años.
print("----------------------------------")
print("✨ Ejercicio 3: Nombres y saludos:")
print("----------------------------------")
name = "Ana"
age = 44
print(f"Hola, me llamo {name} y tengo {age} años")
# ✨ Ejercicio 4: Intercambio simple
# Tienes dos variables:
x = "gato"
y = "perro"
# Intercambia sus valores para que x valga "perro" e y valga "gato".
print("-----------------------------------")
print("✨ Ejercicio 4: Intercambio simple:")
print("-----------------------------------")
x, y = y, x
print(f"X: {x} | Y: {y}")
# ------------------------------
# OPERADORES
# ------------------------------

# ✨ Ejercicio 5: Suma de la compra
# Declara tres precios:
pan = 1.50
leche = 1.24
huevos = 2.70
# Calcula el total y muestra: “El total de tu compra es de: 4,25€”
print("----------------------------------")
print("✨ Ejercicio 5: Suma de la compra:")
print("----------------------------------")
total = pan + leche + huevos
print(f"Total: {total}")
# ✨ Ejercicio 6: ¿Par o impar?
# Pide al usuario un número con input() y di si es par o impar.
print("------------------------------")
print("✨ Ejercicio 6: ¿Par o impar?:")
print("------------------------------")
try:
    num = int(input("Introduce un número entero: "))
    if num % 2:
        print(f"• {num} es un número impar")
    else:
        print(f"• {num} es un número par")
except ValueError:
    print("\033[91mNo es un número válido\033[0m")

# ------------------------------
# ESTRUCTURAS DE CONTROL
# ------------------------------

# ✨ Ejercicio 7: ¿Mayor de edad?
# Pide la edad al usuario. Si tiene 18 o más, muestra “Puedes entrar”.
# Si no, muestra “Acceso denegado”.
print("--------------------------------")
print("✨ Ejercicio 7: ¿Mayor de edad?:")
print("--------------------------------")
try:
    age = int(input("Introduce tu edad: "))
    if age >= 18:
        print("✔ Puedes entrar")
    else:
        print("❌ No puedes entrar")
except ValueError:
    print("\033[91mNo es una edad válida\033[0m")
# ✨ Ejercicio 8: Elige una opción
# Pide al usuario que elija una opción:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión
# Y muestra un mensaje distinto para cada caso.

print("---------------------------------")
print("✨ Ejercicio 8: Elige una opción:")
print("---------------------------------")
print("1. Ver perfil\n2. Editar perfil\n3. Cerrar sesión")
try:
    menu = int(input("Introduce índice de menú: "))
    response = {
        1: "Ver perfíl",
        2: "Editar perfil",
        3: "Cerrar sesión"
    }.get(menu, "❌ Opción no contemplada")
    if 1 <= menu <= 3:
        print(f"→ Has elegido la opción: {response}")
    else:
        print(response)
except ValueError:
    print("\033[91mNo es un índice válido\033[0m")
# ------------------------------
# EXTRA: TIPOS + CONDICIONAL
# ------------------------------

# ✨ Ejercicio 9: Detector de tipos raros
# Pide al usuario que escriba cualquier cosa.
# Muestra:
# - Si es un número entero: “Has escrito un número entero”
# - Si es un número decimal: “Has escrito un número decimal”
# - Si es un texto: “Parece que es una cadena de texto”
# - Si no puedes adivinar el tipo: “No sé qué es esto 😵‍💫”
# Usa try/except para intentar convertir a int() o float().

print("----------------------------------------")
print("✨ Ejercicio 9: Detector de tipos raros:")
print("----------------------------------------")

x = input("Escribe cualquier cosa: ")
try:
    if type(int(x)) == int:
        print("► Es un entero")
except ValueError:
    try:
        if type(float(x)) == float:
            print("► Es un decimal")
    except ValueError:
        if type(str(x)) == str:
            print("► Es una cadena")
        else:
            print("No sé qué es esto 😵‍💫")

# ------------------------------
# OPERADORES + CONDICIONALES + VARIABLES
# ------------------------------

# ✨ Ejercicio 10: Calculadora con menú
# Pide dos números y muestra este menú:
# 1. Sumar
# 2. Restar
# 3. Multiplicar
# 4. Dividir
# Según la opción elegida, haz la operación y muestra el resultado.
# Bonus: si elige dividir y el segundo número es 0,
# muestra “No se puede dividir por cero”.

print("--------------------------------------")
print("✨ Ejercicio 10: Calculadora con menú:")
print("--------------------------------------")


def sumar(n1, n2):
    return n1 + n2


def restar(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


try:
    x = float(input("Introdúce el primer número: "))
    y = float(input("Introdúce el segundo número: "))
    print("--------------")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
    print("--------------")
    menu = int(input("Indíque índice de la operación deseada: "))

    result = {
        1: sumar(x, y),
        2: restar(x, y),
        3: mult(x, y),
        4: div(x, y)
    }.get(menu, "❌ Opción no contemplada")

    if 1 <= menu <= 4:
        print(f"Resultado: {result}")
    else:
        print(result)
except Exception as e:
    print(f"\033[91mParámetro no válido: {e}\033[0m")

# ------------------------------
# ESTRUCTURA DE CONTROL CON RANGOS
# ------------------------------

# ✨ Ejercicio 11: Clasificador de edad
# Pide al usuario su edad y clasifícalo:
# - Menor de 3: “Bebé”
# - Entre 3 y 12: “Infancia”
# - Entre 13 y 17: “Adolescencia”
# - Entre 18 y 64: “Adulto”
# - 100 o más: “Senior”

print("--------------------------------------")
print("✨ Ejercicio 11: Clasificador de edad:")
print("--------------------------------------")

ages = {
    range(0, 3): "Bebé",
    range(3, 13): "Infancia",
    range(13, 18): "Adolescencia",
    range(18, 65): "Adulto",
    range(65, 120): "Senior"
}

try:
    x = int(input("Introduce una edad: "))
    for rang, response in ages.items():
        if x in rang:
            print(response)
            break
    else:
        print("❌ Opción no contemplada")
except Exception as e:
    print(f"\033[91mDebe ser un número entero: {e}\033[0m")
