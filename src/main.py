class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.active = True

    def viewProduct(self):
        print(f"Nombre: {self.name}\nPrecio: {self.price}\nActivo: {self.active}")

    def __str__(self):
        return f"Nombre: {self.name}, Precio: {self.price}, Activo: {self.active}"

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_price(self):
        return self.price

    def set_price(self, value):
        self.price = value

    def get_active(self):
        return self.active

    def set_active(self, value):
        self.active = value


class ProductPerecedero(Product):
    def __init__(self, name: str, price: float, expiration_date: str):
        super().__init__(name, price)
        self.expiration_date = expiration_date

    def viewProduct(self):
        super().viewProduct()
        print(f"Fecha de caducidad: {self.expiration_date}")

    def get_expiration_date(self):
        return self.expiration_date

    def set_expiration_date(self, value):
        self.expiration_date = value

    def __str__(self):
        return f"{super().__str__()}, Fecha de caducidad: {self.expiration_date}"

fabas = Product("Fabas", 2.5)
cabrales = Product("Cabral", 3.5)
fabas.viewProduct()
cabrales.viewProduct()
fabas.price = 3.0
salmon = ProductPerecedero("Salmón", 5.0, "2023-10-31")
salmon.viewProduct()

print(fabas)
print(salmon)
