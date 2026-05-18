from abc import ABC, abstractmethod


#ABSTRACTION
class CoffeeMachine(ABC):

    @abstractmethod
    def recipe(self):
        pass

    @abstractmethod
    def make_drink(self):
        pass


#ENCAPSULATION
class Ingredients:

    def __init__(self):
        self.__coffee_beans = "Coffee Beans"
        self.__hot_water = "Hot Water"
        self.__milk = "Milk"
        self.__froth = "Froth Maker"
        self.__green_tea = "Green Tea Leafs"

    def get_coffee_beans(self):
        return self.__coffee_beans

    def get_hot_water(self):
        return self.__hot_water

    def get_milk(self):
        return self.__milk

    def get_froth(self):
        return self.__froth

    def get_green_tea(self):
        return self.__green_tea


# INHERITANCE
class Espresso(CoffeeMachine):

    def __init__(self):
        self.items = Ingredients()

    def recipe(self):
        return [
            self.items.get_coffee_beans(),
            self.items.get_hot_water()
        ]

    def make_drink(self):
        print("Espresso is prepared using:")
        print(self.recipe())



class Americano(Espresso):

    # OVERRIDING
    def recipe(self):
        return [
            self.items.get_coffee_beans(),
            self.items.get_hot_water(),
            "Extra Hot Water"
        ]

    def make_drink(self):
        print("Americano is prepared using:")
        print(self.recipe())



class Latte(Americano):

    def recipe(self):
        return [
            self.items.get_coffee_beans(),
            self.items.get_hot_water(),
            self.items.get_milk(),
            self.items.get_froth()
        ]

    def make_drink(self):
        print("Latte is prepared using:")
        print(self.recipe())



class Cappuccino(Latte):

    def recipe(self):
        return [
            self.items.get_coffee_beans(),
            self.items.get_hot_water(),
            self.items.get_milk(),
            self.items.get_froth()
        ]

    def make_drink(self):
        print("Cappuccino is prepared using:")
        print(self.recipe())



class Matcha(CoffeeMachine):

    def __init__(self):
        self.items = Ingredients()

    def recipe(self):
        return [
            self.items.get_green_tea(),
            self.items.get_hot_water(),
            self.items.get_froth()
        ]

    def make_drink(self):
        print("Matcha is prepared using:")
        print(self.recipe())



class GreenTea(Matcha):

    def recipe(self):
        return [
            self.items.get_green_tea(),
            self.items.get_hot_water()
        ]

    def make_drink(self):
        print("Green Tea is prepared using:")
        print(self.recipe())



class Mocha(Latte):

    def recipe(self):
        return [
            self.items.get_coffee_beans(),
            self.items.get_hot_water(),
            self.items.get_milk(),
            self.items.get_froth(),
            self.items.get_green_tea()
        ]

    def make_drink(self):
        print("Mocha is prepared using:")
        print(self.recipe())


#POLYMORPHISM
def serve_drink(drink):
    drink.make_drink()


# OVERLOADING
class Quantity:

    def add_quantity(self, a=None, b=None, c=None):

        if a and b and c:
            return a + b + c

        elif a and b:
            return a + b

        elif a:
            return a

        else:
            return 0



espresso = Espresso()
americano = Americano()
latte = Latte()
cappuccino = Cappuccino()
matcha = Matcha()
green_tea = GreenTea()
mocha = Mocha()


# Polymorphism
serve_drink(espresso)
print()

serve_drink(americano)
print()

serve_drink(latte)
print()

serve_drink(cappuccino)
print()

serve_drink(matcha)
print()

serve_drink(green_tea)
print()

serve_drink(mocha)
print()


# Overloading Example
q = Quantity()

print("Quantity with 1 value:", q.add_quantity(1))
print("Quantity with 2 values:", q.add_quantity(1, 2))
print("Quantity with 3 values:", q.add_quantity(1, 2, 3))