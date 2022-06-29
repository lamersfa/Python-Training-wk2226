from collections import namedtuple, defaultdict, Counter
from dataclasses import make_dataclass, dataclass


def unpack(inventory_tuple):
    apple, banana, pear, grape = inventory_tuple
    print("Inventory counted:\n"
          "Apple: " + str(apple) + "\n" +
          "Banana: " + str(banana) + "\n" +
          "Pear: " + str(pear) + "\n" +
          "Grape: " + str(grape))


@dataclass
class FruitPrices:
    name: str
    apple: float = 0.0
    banana: float = 0.0
    pear: float = 0.0
    grape: float = 0.0


def main():
    # tuple & named tuple
    Inventory = namedtuple("Inventory", ["apple", "banana", "pear", "grape"])
    inv_tuple = Inventory(12, 13, 23, 5)
    unpack(inv_tuple)
    print("You heard it right, a whole " + str(inv_tuple.banana) + " bananas!")

    # Dataclass
    Prices = make_dataclass("Prices", ["apple", "banana", "pear", "grape"])
    prices = Prices(0.5, 0.7, 0.8, 0.3)
    print(prices)
    prices.pear = 1.5
    print(prices)

    # Dataclass with decorators
    fruit_price = FruitPrices("Store_name_1", apple=0.3, pear=5.6)
    print(fruit_price)
    fruit_price.banana = 0.4
    fruit_price.grape = 0.1
    print(fruit_price)

    # Dictionary
    fruits = {
        "apple" : 0.5,
        "banana" : 1.2,
    }
    print("Banana price: " + str(fruits["banana"]))

    # Default dict
    d = defaultdict(float)
    print(d["apple"])
    print(d.keys())
    d["apple"] = 0.5
    print(d["apple"])

    # Counter
    fruit_bought = [
        "apple",
        "apple",
        "banana",
        "apple",
        "banana",
        "pear",
    ]
    print("Fruit in order of popularity:")
    print(Counter(fruit_bought).most_common())
    print("Most sold:")
    print(Counter(fruit_bought).most_common(1)[0][0])

    # Sets
    sold_store1 = {"apple", "pineapple", "banana", "grape"}
    sold_store2 = {"apple", "banana", "mango", "kiwi"}
    sold_store3 = {"apple", "banana"}
    print(sold_store1.union(sold_store2))
    print(sold_store1.intersection(sold_store2))
    print(sold_store1.symmetric_difference(sold_store2))
    print(sold_store1.difference(sold_store2))
    print(sold_store1.issubset(sold_store3))
    print(sold_store1.issuperset(sold_store3))


if __name__ == "__main__":
    main()
