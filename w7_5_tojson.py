import json
class Product():
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    def toJson(self):
        self.person_dict = json.dumps(product.__dict__)
        return self.person_dict
        
class Brand():
    def __init__(self,name,year):
       self.name=name
       self.year=year
brand=Brand("zara",2000)
product=Product("short",brand.name,50)
print(product.toJson())
