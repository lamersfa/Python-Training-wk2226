
def combining(func):
    def wrapper(*args, **kwargs):
        returnvalue = func(*args, **kwargs)
        name = func.__name__
        print(f"Got answer '{returnvalue}' from function '{name}'")
        return returnvalue
    return wrapper


@combining
def three_ints(a, b, c):
    return a + b + c


@combining
def rev_4_string(a, b, c, d):
    value = "" + d + " " + c + " " + b + " " + a
    return value


class FruitSales:
    def __init__(self):
        self.observers = []
        self.stock = 20
        self.funds = 30

    def attach(self, observer):
        self.observers.append(observer)

    def transaction(self, stock_change, funds_change):
        self.stock += stock_change
        self.funds += funds_change
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()


class StockObserver:
    def __init__(self, fruitsales):
        self.fruitsales = fruitsales

    def __call__(self):
        if self.fruitsales.stock <= 10:
            print(f"It is time to buy more fruit, we only have {self.fruitsales.stock} pieces left.")

        elif self.fruitsales.stock >= 30:
            print(f"We have more than enough fruit, we still have {self.fruitsales.stock} pieces.")

        else:
            print(f"We have {self.fruitsales.stock} pieces of fruit left.")


class FundsObserver:
    def __init__(self, fruitsales):
        self.fruitsales = fruitsales

    def __call__(self):
        if self.fruitsales.funds <= 10:
            print(f"It is time to sell more fruit, we only have ${self.fruitsales.funds} left.")

        elif self.fruitsales.funds >= 50:
            print(f"We have money to spare, we have ${self.fruitsales.funds}.")

        else:
            print(f"We have ${self.fruitsales.funds}.")


def main():
    three_ints(1, 2, 3)
    rev_4_string("This", "is", "a", "sentence")

    fruit = FruitSales()
    s_ob = StockObserver(fruit)
    f_ob = FundsObserver(fruit)
    fruit.attach(s_ob)
    fruit.attach(f_ob)
    fruit.transaction(-10, 20)
    fruit.transaction(10, -20)
    fruit.transaction(10, -20)


if __name__ == "__main__":
    main()
