# 🌟 Reto: Gestor de contactos

# 🎯 Objetivo:
# Crear una pequeña aplicación en consola que permita al usuario
# almacenar, mostrar y buscar contactos usando listas y diccionarios.

# Instrucciones:

# 1. Añadir un contacto:
#    - Pide al usuario el nombre, edad y ciudad.
#    - Guarda el contacto en una lista como un diccionario.

# 2. Mostrar todos los contactos:
#    - Recorre la lista y muestra los datos en el formato:
#      Nombre: Marta – Edad: 30 – Ciudad: Oviedo

# 3. Buscar por nombre:
#    - Pide un nombre y muestra el contacto si existe.

# 4. Salir:
#    - Si el usuario elige la opción 4, termina el programa.

# 💡 Menú sugerido:
# ¿Qué quieres hacer?
# 1. Añadir contacto
# 2. Ver contactos
# 3. Buscar por nombre
# 4. Salir

contacts = []

def add(name, age, city):
    newContact = {
        "name": name,
        "age": age,
        "city": city
    }
    contacts.append(newContact)
    print(f"-----------------------------------\n✔ El nuevo contacto ha sido agregado:\n{newContact}\n-----------------------------------")

add("Ana",44,"Avilés")
add("Javier",34,"Mieres")

def newContact():
    try:
        name = input("\n→ Introduce un nombre: ")
        age = int(input("\n→ Introduce una edad: "))
        city = input("\n→ Introduce una ciudad: ")
        add(name, age, city)
    except Exception as e:
        print(f"❌ Valor introducido incorrecto: {e}")

def allContacts(): 
    print(f"---------------------\nListado de contactos:\n---------------------")
    for c in contacts:
        print("=============")
        for k, v in c.items():
            print (f"{k}: {v}")
        print("=============")

def findByName():
    try:
        name = input("\n→Indica el nombre a buscar: ")    
        for c in contacts:
            if c["name"] == name:
                return print(f"----------------------\n✔ Contacto encontrado:\n----------------------\n{c}")
        else:
            print("\n❌ Contacto no encontrado")
    except Exception as e:
        print(f"❌ Valor introducido incorrecto: {e}")
print("-----------------------------")
print("✨ Reto: Gestor de contactos:")
print("-----------------------------")
while True:
    print("--------------------\n¿Qué quieres hacer?\n-------------------\n1. Añadir contacto\n2. Ver contactos\n3. Buscar por nombre\n4. Salir\n")
    try:
        index = int(input("► Indíque un índice numérico: "))
        menu = {
            1: newContact,
            2: allContacts,
            3: findByName,
        }
        if index in menu:
            menu[index]()
        elif index == 4:
            print("Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida.")
    except:
        print(f"\033[91m\n‼ Debe ser un número entero\033[0m")