# def add(*args):
#     return sum(args)

def calculate(n,**kwargs):
    n += kwargs.get("add")
    if kwargs.get("multiply"):
        n *= kwargs.get("multiply")
    print(n)


calculate(2,add=5)

class Car:
    def __init__(self,**kwargs):
        self.model = kwargs.get("model")
        self.brand = kwargs.get("brand")
    
car = Car(brand="bmw")
print(car.model)