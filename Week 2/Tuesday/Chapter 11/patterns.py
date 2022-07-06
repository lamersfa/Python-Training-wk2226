from collections import Counter


class FruitCount:
    """Uses a counter to keep track of the fruit. Contains 3 fruits: Apple, Pear and Banana"""
    def __init__(self, fcount):
        self.fcount = fcount

    def apply_changes(self, changecount):
        """Expects a counter"""
        self.fcount += changecount

    def set_count(self, count):
        self.fcount = count

    def return_count(self):
        return self.fcount


class FruitList:
    """Uses a list to keep track of the fruit. Contains 3 fruits: Apple, Pear and Banana"""
    def __init__(self, flist):
        self.flist = flist

    def apply_changes(self, changelist):
        for i, item in enumerate(changelist):
            self.flist[i] += item

    def setlist(self, flist):
        self.flist = flist

    def return_list(self):
        return self.flist


class FruitAdapter:
    def __init__(self):
        self.namelist = ['apple', 'pear', 'banana']
        self.c = Counter()

    def list_to_count(self, flist):

        for i, item in enumerate(flist):
            self.c[self.namelist[i]] = item
        return self.c

    def count_to_list(self, count):
        return [count[self.namelist[0]], count[self.namelist[1]], count[self.namelist[2]]]


class Actions:
    def __init__(self, variable):
        self.variable = variable

    def action1(self):
        print("We're doing action 1")

    def action2(self):
        print(f"Here's the variable: {self.variable}")


class Command:
    def __init__(self, action):
        self.action = action

    def __call__(self, number):
        if number == 1:
            self.action.action1()

        elif number == 2:
            self.action.action2()


class KeyboardPress:
    def keypress(self, number):
        self.command(number)


def main():
    fa = FruitAdapter()
    fc = FruitCount(Counter({'apple': 5, 'pear': 2, 'banana': 3}))
    print(fc.return_count())
    fl = FruitList(fa.count_to_list(fc.return_count()))
    print(fl.return_list())
    fl.apply_changes([-3, 5, -1])
    fc.set_count(fa.list_to_count(fl.return_list()))
    print(fc.return_count())

    action = Actions("Banana")
    keybpress = KeyboardPress()
    command = Command(action)
    keybpress.command = command
    keybpress.keypress(1)
    keybpress.keypress(2)


if __name__ == "__main__":
    main()
