# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    # 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.
    # @classmethod
    # @staticmethod

    def describe(self):
        print("Name: {}, Kind: {}".format(self.name, self.kind))


# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

class Meat(Food):
    def __init_(self):
        super().__init__(name, "meat")

    def cook(self):
        print("cooking")


class Fruit(Food):
    def __init_(self):
        super().__init__(name, "fruit")

    def clean(self):
        print("cleaning")
    # 4) Overwrite a “dunder” method to be able to print your “Food” class


food = Food("pizza", "cheese")
print(food.describe())
