from pprint import pp
import csv
import os
import random

csv_file = "data/movies.csv"

# 🧪 Ejercicios – Consola + Buenas Prácticas (KISS, DRY, Excepciones)

# Ejercicio 1: Sistema de votaciones
# -----------------------------------
# Crea un programa en consola con las siguientes opciones:
# 1. Añadir película
# 2. Votar por una película
# 3. Mostrar resultados
# 4. Salir
# Si se intenta votar por una película no registrada,
# muestra error (usa try/except con KeyError).
# Usa funciones separadas por funcionalidad.
# (Bonus: guardar votos en un fichero CSV)

print("--------------------------------------")
print("✨ Ejercicio 1: Sistema de votaciones:")
print("--------------------------------------")

def loadMovies():
    movies = {}
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) == 2:
                    movies[row[0]] = int(row[1])
    else:
        movies = {
            "El Padrino": 0,
            "El Señor de los Anillos": 0,
            "La Vida es Bella": 0,
            "Pulp Fiction": 0,
            "El Club de la Lucha": 0,
        }
    return movies


def saveMovies(movies):
    os.makedirs("data", exist_ok=True)
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Título", "Votos"])
        for titulo, votos in movies.items():
            writer.writerow([titulo, votos])


def addMovie(movies):
    try:
        name = input("Introduce el nombre de la película: ")
        if name in movies:
            print("La película ya existe.")
        else:
            movies[name] = 0
            saveMovies(movies)
            print(f"\nPelícula '{name}' añadida.\n")
    except Exception as e:
        print(f"Error: {e}")


def voteMovies(movies):
    try:
        name = input("Introduce el nombe de la película a botar:")
        if name in movies:
            movies[name] += 1
            saveMovies(movies)
            print(f"\nHas votado a {name}.")
        else:
            raise KeyError(f"La película {name} no existe.")
    except KeyError as e:
        print(f"Error: {e}")


def showResults(movies):
    pp(movies)


def main():

    movies = loadMovies()

    menu = {
        1: addMovie,
        2: voteMovies,
        3: showResults,
    }

    while True:
        print("=====================\n1. Agregar película\n2. Votar por película\n3. Ver resultados\n4. Salír\n\
=====================\n")
        try:
            index = int(input("Selecciona una índice: "))
            if index in menu:
                menu[index](movies)
            elif index == 4:
                print("Saliendo del programa...")
                break
            else:
                print("❌ Opción no válida. Por favor, elige una opción del menú.")
        except ValueError as e:
            print(f"Error: {e}\n")

main()

# Ejercicio 2: Limpieza de datos crudos
# -------------------------------------
# Dada una lista de nombres con errores (espacios, mayúsculas, duplicados),
# crea una función que la limpie
# devolviendo una lista ordenada y sin duplicados.
# Todos los nombres deben tener solo la primera letra en mayúscula.
# Muestra cuántos nombres únicos hay.
# 💡 Añade manejo de errores si algún
# elemento no es una cadena (TypeError o AttributeError)

print("-----------------------------------------")
print("✨ Ejercicio 2: Limpieza de datos crudos:")
print("-----------------------------------------")

names = ["  ana", "Javier", "javier", "JAVIER", "Ana", " ", "josé"]
namesWhitNumber = ["  ana", "Javier", "javier", "JAVIER", "Ana", 3, " ", "josé"]
def cleanNames(names):
    try:
        cleaned_names = set()
        for name in names:
            if not isinstance(name, str):
                raise TypeError(f"Este elemento no es una cadena: {name}")
            cleaned_name = name.strip().capitalize()
            if cleaned_name:
                cleaned_names.add(cleaned_name)
        return sorted(cleaned_names)
    except Exception as e:
        print(f"Error: {e}")

pp(cleanNames(names))
pp(cleanNames(namesWhitNumber))

# Ejercicio 3: Analizador de texto
# --------------------------------
# Pide al usuario un párrafo.
# Luego:
# - Cuenta cuántas palabras contiene
# - Muestra cuántas veces aparece cada palabra
# - Muestra la palabra más repetida
# 💡 Controla que el texto no esté vacío. Usa ValueError.

print("------------------------------------")
print("✨ Ejercicio 3: Analizador de texto:")
print("------------------------------------")


try:
    text = input("Introduce un párrafo:")
    words = text.split()
    print(f"El párrafo contiene {len(words)} palabras.")
    if len(words) == 0:
        raise ValueError("El texto no puede estar vacío.")
    wordCount = {}
    for word in words:
        word = word.lower()
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    mostWord = max(wordCount, key=wordCount.get)
    print(f"Palabra más repetida: {mostWord} ({wordCount[mostWord]} veces)")
except Exception as e:
    print(f"Error: {e}")

# Ejercicio 4: Simulador de inventario
# -------------------------------------
# Crea un sistema que permita gestionar productos en un inventario.
# Cada producto tiene nombre, stock y precio.
# Opciones:
# 1. Añadir producto
# 2. Actualizar stock
# 3. Eliminar producto
# 4. Ver inventario
# 💡 Usa try/except para validar entradas numéricas
# y para controlar si el producto no existe.

print("----------------------------------------")
print("✨ Ejercicio 4: Simulador de inventario:")
print("----------------------------------------")

class Product:

    def __init__(self, name: str, stock: int, price: float):
        self.name = name
        self.stock = stock
        self.price = price

    def __str__(self):
        return f"Nombre: {self.name}, Stock: {self.stock}, Precio: {self.price}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, name: str, stock: int, price: float):
        if name in self.products:
            print("El producto ya existe.")
        else:
            self.products[name] = Product(name, stock, price)
            print(f"Producto '{name}' añadido.")

    def update_stock(self, name: str, stock: int):
        if name in self.products:
            self.products[name].stock += stock
            print(f"Stock de '{name}' actualizado a {self.products[name].stock}.")
        else:
            raise KeyError(f"El producto '{name}' no existe.")

    def delete_product(self, name: str):
        if name in self.products:
            del self.products[name]
            print(f"Producto '{name}' eliminado.")
        else:
            raise KeyError(f"El producto '{name}' no existe.")

    def view_inventory(self):
        if not self.products:
            print("El inventario está vacío.")
            return
        print("Inventario:")
        for product in self.products.values():
            print(product)

def menu():
    inventory = Inventory()
    while True:
        print("=====================\n1. Añadir producto\n2. Actualizar stock\n3. Eliminar producto\n\
4. Ver inventario\n5. Salir\n=====================\n")
        try:
            index = int(input("Selecciona una índice: "))
            if index == 1:
                name = input("Introduce el nombre del producto: ")
                stock = int(input("Introduce el stock del producto: "))
                price = float(input("Introduce el precio del producto: "))
                inventory.add_product(name, stock, price)
            elif index == 2:
                name = input("Introduce el nombre del producto a actualizar: ")
                stock = int(input("Introduce la cantidad a añadir al stock: "))
                inventory.update_stock(name, stock)
            elif index == 3:
                name = input("Introduce el nombre del producto a eliminar: ")
                inventory.delete_product(name)
            elif index == 4:
                inventory.view_inventory()
            elif index == 5:
                print("Saliendo del programa...")
                break
            else:
                print("❌ Opción no válida. Por favor, elige una opción del menú.")
        except ValueError as e:
            print(f"Error: {e}")

menu()

# Ejercicio 5: Generador de alias seguro
# ---------------------------------------
# Pide al usuario nombre y apellido, y genera un alias así:
# - 3 letras del apellido (mayúsculas)
# - 2 letras del nombre (minúsculas)
# - número aleatorio del 10 al 99
# - símbolo especial aleatorio
# 💡 Valida que el nombre y apellido tengan longitud suficiente (ValueError)

print("------------------------------------------")
print("✨ Ejercicio 5: Generador de alias seguro:")
print("------------------------------------------")

while True:
    try:
        name = input("Introduce tu nombre: ")
        lastname = input("Introduce tu apellido: ")
        if len(name) < 2 or len(lastname) < 3:
            raise ValueError("El nombre debe tener al menos 2 letras y el apellido al menos 3 letras.")
        special_characters = "!@#$%^&*()_+"
        alias = f"{lastname[:3].upper()}{name[:2].lower()}{random.randint(10, 99)}{random.choice(special_characters)}"
        print(f"Tu alias seguro es: {alias}")
        break
    except Exception as e:
        print(f"Error: {e}")

# Ejercicio 6: Comprobador de contraseñas seguras
# ------------------------------------------------
# Pide una contraseña al usuario.
# Valida que:
# - Tiene al menos 8 caracteres
# - Contiene mayúsculas, minúsculas y números
# 💡 Usa raise y excepciones personalizadas con mensajes explicativos.

print("---------------------------------------------------")
print("✨ Ejercicio 6: Comprobador de contraseñas seguras:")
print("---------------------------------------------------")

class PasswordError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def checkPassword(password):
    if len(password) < 8:
        raise PasswordError("La contraseña debe tener al menos 8 caracteres.")
    if not any(char.isupper() for char in password):
        raise PasswordError("La contraseña debe contener al menos una mayúscula.")
    if not any(char.islower() for char in password):
        raise PasswordError("La contraseña debe contener al menos una minúscula.")
    if not any(char.isdigit() for char in password):
        raise PasswordError("La contraseña debe contener al menos un número.")
    print("Contraseña segura.")


while True:
    try:
        password = input("Introduce una contraseña: ")
        checkPassword(password)
        break
    except PasswordError as e:
        print(f"Contraseña insegura: {e.message}\n")

# 🌟 Reto Extra: Simulador de reservas de hotel
# ----------------------------------------------
# Habitaciones del 101 al 110. El usuario puede:
# 1. Ver habitaciones disponibles
# 2. Reservar habitación (introduciendo su nombre)
# 3. Cancelar reserva
# 4. Ver reservas confirmadas
# 5. Salir
# Las reservas se almacenan en un diccionario {habitacion: nombre}
# Usa funciones y control de errores con KeyError si la habitación no existe.
# (Bonus: mostrar mapa visual, reservas múltiples, carga inicial aleatoria)

print("----------------------------------------------")
print("✨ Reto Extra: Simulador de reservas de hotel:")
print("----------------------------------------------")

class Hotel:
    def __init__(self):
        self.rooms = {i: None for i in range(101, 111)}
        names = ["Juan", "Ana", "Pedro", "María", "Luis"]
        for i in range(3):
            room = random.choice(list(self.rooms.keys()))
            if self.rooms[room] is None:
                self.rooms[room] = random.choice(names)

    def viewAvailableRooms(self):
        available_rooms = [room for room, name in self.rooms.items() if name is None]
        if available_rooms:
            print("Habitaciones disponibles:", available_rooms)
        else:
            print("No hay habitaciones disponibles.")

    def reserveRoom(self, nums, name):
        for num in nums:
            if num not in self.rooms:
                raise KeyError(f"La habitación {num} no existe.")
            if self.rooms[num] is not None:
                print(f"La habitación {num} ya está reservada.")
            else:
                self.rooms[num] = name
                print(f"Reserva confirmada para la habitación {num} a nombre de {name}.")

    def cancelReservation(self, num, name):
        if num not in self.rooms:
            raise KeyError(f"La habitación {num} no existe.")
        if self.rooms[num] is None:
            print(f"La habitación {num} no está reservada.")
        else:
            if self.rooms[num] == name:
                self.rooms[num] = None
                print(f"Reserva cancelada para la habitación {num}.")
            else:
                print(f"La habitación {num} está reservada a nombre de otra persona.")

    def viewReservations(self):
        print("Reservas confirmadas:")
        for room, name in self.rooms.items():
            if name is not None:
                print(f"Habitación {room}: {name}")
def menu():
    hotel = Hotel()
    while True:
        print("=====================\n1. Ver habitaciones disponibles\n2. Reservar habitación\n\
3. Cancelar reserva\n4. Ver reservas confirmadas\n5. Salir\n=====================\n")
        try:
            index = int(input("Selecciona una índice: "))
            if index == 1:
                hotel.viewAvailableRooms()
            elif index == 2:
                rooms = [int(x) for x in input("Introduce los números de habitación\
                                                a reservar (separados por comas): ").split(",")]
                name = input("Introduce tu nombre: ")
                hotel.reserveRoom(rooms, name)
            elif index == 3:
                room = int(input("Introduce el número de habitación a cancelar: "))
                name = input("Introduce tu nombre: ")
                hotel.cancelReservation(room, name)
            elif index == 4:
                hotel.viewReservations()
            elif index == 5:
                print("Saliendo del programa...")
                break
            else:
                print("❌ Opción no válida. Por favor, elige una opción del menú.")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyError as e:
            print(f"Error: {e}")
menu()
