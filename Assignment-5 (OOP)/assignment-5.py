class Smartphone:
    def __init__(self, model, manufacturer, price, operating_system):
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.operating_system = operating_system

    def purchase(self):
        print(f"Congratulations! You have purchased a {self.manufacturer} {self.model} with {self.operating_system} for {self.price}.")

    def sell(self):
        print(f"You have sold your {self.manufacturer} {self.model} with {self.operating_system} for {self.price}.")

    def swap(self):
        print(f"You have swapped your {self.manufacturer} {self.model} with {self.operating_system} for {self.price}.")

phone_1 = Smartphone("Galaxy S21", "Samsung", 799, "Android")
phone_2 = Smartphone("iPhone 12", "Apple", 799, "iOS")
phone_3 = Smartphone("OnePlus 9", "OnePlus", 729, "Android")

phone_1.purchase()
phone_2.sell()
phone_3.swap()