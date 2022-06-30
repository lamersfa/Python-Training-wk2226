

def unpacker1(*lists):
    apple, banana, kiwi, grape = lists
    print(f"""
    All the fruits:
    Apple: {apple}
    Banana: {banana}
    Kiwi: {kiwi}
    Grape: {grape}""")


def unpacker2(apple, banana, kiwi, grape=0):
    print(f"""
    All the fruits:
    Apple: {apple}
    Banana: {banana}
    Kiwi: {kiwi}
    Grape: {grape}""")


class AllTheArgs:
    basic_dict = {
        "apple": 0,
        "banana": 0,
        "milk": 1,
        "beer": 0,
        "cola": 0,
    }

    def __init__(self, *fruit, milk=0, **kwargs):
        apple, banana = fruit
        self.item = {**AllTheArgs.basic_dict, **kwargs, "apple": apple, "banana": banana, "milk": milk}

    def print_stuff(self):
        print(self.item)


def print_func():
    print("I print stuff like this")


def func_func(function):
    print("What does this function do?")
    function()


def rev_printer(sentence):
    print("".join(reversed(sentence)))


class Dummy:
    def printer(self, sentence):
        print(sentence)


def main():
    # Default args, variable args
    unpacker1(1, 3, 5, 2)
    numbers = (2, 5, 7)
    numbers2 = (2, 5, 7, 3)
    unpacker2(*numbers)
    unpacker2(*numbers2)
    all_args = AllTheArgs(1, 2, beer=2, cola=1)
    all_args2 = AllTheArgs(1, 2, milk=3, beer=2, cola=1)
    all_args.print_stuff()
    all_args2.print_stuff()

    # Functions as objects, functions as attributes
    func_func(print_func)
    dummy = Dummy()
    dummy.printer("Normal sentence")
    dummy.printer = rev_printer
    dummy.printer("Normal sentence")


if __name__ == "__main__":
    main()
