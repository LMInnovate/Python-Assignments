class Smartphone:
    def __init__(self, brand, model, os):
        self.brand = brand
        self.model = model
        self.os = os

    def specs(self):
        print(f"{self.brand} {self.model} runs on {self.os}.")

    def feature(self):
        print("This smartphone has standard features.")
        
class CameraPhone(Smartphone):
    def feature(self):
        print(f"{self.brand} {self.model} captures stunning photos with high-end cameras 📸")

class GamingPhone(Smartphone):
    def feature(self):
        print(f"{self.brand} {self.model} delivers smooth gameplay with powerful graphics 🎮")

phone1 = CameraPhone("Samsung", "A15", "Android")
phone2 = GamingPhone("Asus", "ROG Phone 8", "Android")

phone1.specs()
phone1.feature()

phone2.specs()
phone2.feature()
