import random
import string

# 🧪 Fundamentos Python III – Funciones

# ------------------------------
# ✨ Ejercicio 1: Saludo básico
# Objetivo: Aprender a definir y llamar funciones
# Crea una función llamada saludar() que imprima: "¡Hola, bienvenido/a!"
# Luego llama a la función una vez para comprobar que funciona.

print("------------------------------")
print("✨ Ejercicio 1: Saludo básico:")
print("------------------------------")


def saludar():
    print("¡Hola, bienvenido/a!")


saludar()

# ------------------------------
# ✨ Ejercicio 2: Saludo personalizado
# Objetivo: Trabajar con parámetros
# Crea una función llamada saludar_persona(nombre)
# que imprima: "Hola, [nombre]!"
# Llama a la función dos veces con diferentes nombres.

print("-------------------------------------")
print("✨ Ejercicio 2: Saludo personalizado:")
print("-------------------------------------")


def saludar_persona(name):
    print(f"Hola, {name}!")


saludar_persona("Paco")
# ------------------------------
# ✨ Ejercicio 3: Suma fácil
# Objetivo: Usar parámetros y return
# Crea una función llamada sumar(a, b) que devuelva la suma de dos números.
# Guarda el resultado en una variable y muéstralo con print().

print("---------------------------")
print("✨ Ejercicio 3: Suma fácil:")
print("---------------------------")


def sumar(a, b):
    return a + b


result = sumar(2, 3)
print(result)

# ------------------------------
# ✨ Ejercicio 4: ¿Par o impar?
# Objetivo: Usar lógica dentro de una función
# Escribe una función es_par(numero) que devuelva True si el número es par
# y False si es impar.
# Pruébala con varios números y muestra el resultado.

print("-----------------------------")
print("✨ Ejercicio 4: ¿Par o impar?")
print("-----------------------------")


def es_par(n):
    if n % 2:
        return False
    else:
        return True


nums = [0, 1, 2, 3, 4, 99, 100, -7, -8]

for n in nums:
    print(es_par(n))
# ------------------------------
# ✨ Ejercicio 5: Mensaje con formato
# Objetivo: Devolver una cadena con formato
# Crea una función llamada mensaje(nombre, edad) que devuelva una frase como:
# "Me llamo Marta y tengo 30 años."
# Usa return y luego muestra el mensaje con print().

print("-----------------------------------")
print("✨ Ejercicio 5: Mensaje con formato")
print("-----------------------------------")


def message(name, age):
    return f"Me llamo {name} y tengo {age} años"


print(message("Ana", 238))
# ------------------------------
# ✨ Ejercicio 6: Calculadora simple
# Objetivo: Practicar varias funciones juntas
# Crea 4 funciones: sumar(a, b), restar(a, b), multiplicar(a, b), dividir(a, b)
# Llama a cada una con un par de números y muestra los resultados.
# Bonus: en dividir(), si el segundo número es 0,
# devuelve "No se puede dividir por cero"

print("----------------------------------")
print("✨ Ejercicio 6: Calculadora simple")
print("----------------------------------")


def sumar(n1, n2):
    return n1 + n2


def restar(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 == 0:
        return "No se puede dividir por 0"
    else:
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
# ✨ Ejercicio 7: Edad en el futuro
# Objetivo: Usar return con operaciones
# Escribe una función llamada edad_futura(edad_actual, años)
# que calcule la edad que tendrás después de X años.

print("---------------------------------")
print("✨ Ejercicio 7: Edad en el futuro")
print("---------------------------------")


def edad_futura(edad_actual, años):
    return edad_actual + años


print(edad_futura(238, 1000))

# ------------------------------
# ✨ Ejercicio 8: Media de 3 números
# Objetivo: Trabajar con números y return
# Crea una función llamada calcular_media(a, b, c)
# que devuelva la media de tres números.
# Prueba la función y muestra el resultado con print().

print("----------------------------------")
print("✨ Ejercicio 8: Media de 3 números")
print("----------------------------------")


def media(*nums):
    return sum(nums) / len(nums)


print(media(1, 2, 3))

# ------------------------------
# ✨ Ejercicio 9: Mostrar menú (sin lógica)
# Objetivo: Separar la presentación de la lógica
# Escribe una función llamada mostrar_menu() que imprima un pequeño menú como:
# 1. Ver perfil
# 2. Editar perfil
# 3. Cerrar sesión

print("-----------------------------------------")
print("✨ Ejercicio 9: Mostrar menú (sin lógica)")
print("-----------------------------------------")


def mostrar_menu():
    print("1. Ver perfil")
    print("2. Editar perfil")
    print("3. Cerrar sesión")


mostrar_menu()

# ------------------------------
# 🌟 Reto Final: Generador de contraseñas

# Crea una función llamada generar_contraseña(longitud)
# que devuelva una contraseña aleatoria con la longitud especificada.

# La contraseña debe contener una mezcla de:
# - letras minúsculas (a-z)
# - letras mayúsculas (A-Z)
# - números (0-9)
# - símbolos como !, @, #, $, %, &, *

# Ejemplo de uso:
# contraseña = generar_contraseña(12)
# print(contraseña)  # -> A2c$e9#Tq&7L

# Bonus:
# - Usa la librería random
# - Controla que la longitud mínima sea 8 caracteres
# - Añade un mensaje de advertencia si se pide menos de 8

print("---------------------------------------")
print("✨ Reto Final: Generador de contraseñas")
print("---------------------------------------")


def randomNum():
    return str(random.randint(0, 9))


def randomWordLower():
    return random.choice(string.ascii_lowercase)


def randomWordUpper():
    return randomWordLower().upper()


def randomSymbol():
    symbol = ["!", "@", "#", "$", "%", "&", "*"]
    return random.choice(symbol)


def passwordGenerator():
    choices = {
        1: randomNum,
        2: randomWordLower,
        3: randomWordUpper,
        4: randomSymbol
    }
    password = ""
    try:
        longi = 0
        while longi < 8:
            longi = int(input("Introduce la longitud de la contraseña: "))
            if longi < 8:
                print("\033[91mLa longitud debe ser al menos de 8\033[0m")
        for i in range(longi):
            password += choices[random.choice(list(choices.keys()))]()
        print(f"Tu contraseña es: {password}")
    except Exception as e:
        print(f"\033[91mFormato no válido: {e}\033[0m")


passwordGenerator()
