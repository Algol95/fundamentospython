# 🧪 Fundamentos Python II
# Listas, Tuplas, Diccionarios, Sets

# ------------------------------
# LISTAS
# ------------------------------

# ✨ Ejercicio 1: Lista de la compra
# Crea una lista con al menos 5 elementos.
# Muestra el primero y el último elemento.

print("-----------------------------------")
print("✨ Ejercicio 1: Lista de la compra:")
print("-----------------------------------")

bascket = ["tomate", "patata", "atún", "jamón", "pan"]
print(bascket[0], bascket[-1])

# ✨ Ejercicio 2: Añadir y eliminar
# Añade un nuevo elemento a la lista anterior
# y elimina otro. Imprime la lista actualizada.

print("----------------------------------")
print("✨ Ejercicio 2: Añadir y eliminar:")
print("----------------------------------")
bascket.append("ColaCao")
bascket.remove("pan")
print(bascket)

# ✨ Ejercicio 3: Ordenar números
# Crea una lista de números desordenados y ordénala de menor a mayor.
print("--------------------------------")
print("✨ Ejercicio 3: Ordenar números:")
print("--------------------------------")

nums = [2, 18, 91, 23, 12, 3, 1]
nums.sort()
print(nums)

# ------------------------------
# TUPLAS
# ------------------------------

# ✨ Ejercicio 4: Coordenadas
# Crea una tupla con una coordenada (latitud, longitud) y muéstrala.

print("----------------------------")
print("✨ Ejercicio 4: Coordenadas:")
print("----------------------------")

coord = (43.4028, -4.7522)
print(coord)

# ✨ Ejercicio 5: Elemento fijo
# Crea una tupla de 3 elementos. Intenta cambiar uno y observa qué sucede.
print("------------------------------")
print("✨ Ejercicio 5: Elemento fijo:")
print("------------------------------")

cosas = (1, 2, "3")
try:
    cosas[-1] = 3
except Exception as e:
    print(e)

# ------------------------------
# DICCIONARIOS
# ------------------------------

# ✨ Ejercicio 6: Diccionario de usuario
# Crea un diccionario con las claves: nombre, edad, ciudad.

print("---------------------------------------")
print("✨ Ejercicio 6: Diccionario de usuario:")
print("---------------------------------------")

user = {
    "nombre": "Gerardo",
    "edad": 23,
    "ciudad": "Hell"
}

print(user)
# ✨ Ejercicio 7: Actualizar valores
# Cambia el valor de ciudad y añade una nueva clave llamada email.

print("-----------------------------------")
print("✨ Ejercicio 7: Actualizar valores:")
print("-----------------------------------")

user["ciudad"] = "Kagar"
user["email"] = "gerardokagar@gmail.com"

print(user)

# ✨ Ejercicio 8: Iterar claves y valores
# Imprime cada clave y su valor en una línea distinta.

print("----------------------------------------")
print("✨ Ejercicio 8: Iterar claves y valores:")
print("----------------------------------------")

for k, v in user.items():
    print(f"{k}: {v}")

# ------------------------------
# SETS
# ------------------------------

# ✨ Ejercicio 9: Eliminar duplicados
# A partir de una lista con nombres repetidos,
# crea un set para mostrar solo los nombres únicos.

print("------------------------------------")
print("✨ Ejercicio 9: Eliminar duplicados:")
print("------------------------------------")

lista = [1, 2, 2, 3, 4, 4, 4, 5, "paco", "paco"]
print(list(set(lista)))

# ✨ Ejercicio 10: Operaciones de conjuntos
# Dado dos sets A y B, muestra qué elementos están en A pero no en B.

print("------------------------------------------")
print("✨ Ejercicio 10: Operaciones de conjuntos:")
print("------------------------------------------")

A = {1, 2, 3, 5, 6, 7, 8, 9}
B = {1, 3, 4, 7}

print(A.difference(B))
# ------------------------------
# EXTRA
# ------------------------------

# 🌟 Ejercicio Extra: Mezcla total
# Crea un diccionario donde cada clave sea el nombre de una persona
# y el valor una lista de hobbies.
# Añade un nuevo hobby a una persona y muestra todos los hobbies de otra.

print("---------------------------------")
print("✨ Ejercicio Extra: Mezcla total:")
print("---------------------------------")

hobbies = {
    "Ana": ["Programar", "Ver tele", "Molestar a Marcos"],
    "Paco": ["Jugar", "Tirarse por un puente"],
    "Nerea": ["Bailar", "Dibujar"]
}

hobbies["Nerea"].append("Dormir")
print(hobbies["Nerea"][-1])
print(hobbies["Ana"])
