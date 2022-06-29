

class CacheSystem:
    """Dummy cache system for property with decorators. Datasource is a list with 3 items.
    3rd item will be retrieved as cached data."""
    def __init__(self, datasource):
        self._datasource = datasource
        self._cache = None

    @property
    def data(self):
        if self._cache:
            print("Already cached")
            return self._cache
        print("Retrieving data")
        self._cache = self._datasource[2]
        return self._cache

    @data.setter
    def data(self, source):
        print("New source set")
        self._datasource = source
        self._cache = None

    @data.deleter
    def data(self):
        print("Emptied cache")
        self._cache = None


class AppleCounter:
    """Used to count amount of apples in a barrel. Barrels need to be unlocked to be counted and
    barrels need to be locked and counted to be sold. Class would do better if it raised exceptions
    for the checks."""
    def __init__(self, amount):
        self.amount = amount
        self.locked = True
        self.counted = False
        self.price = 0.5

    def manager(self):
        self.unlock()
        self.count()
        self.lock()
        self.sell()

    def unlock(self):
        if self.locked:
            self.locked = False
            print("Unlocked the barrel")
        else:
            print("Barrel is already unlocked!")

    def count(self):
        if self.locked:
            print("Barrel is still locked")
        else:
            print("Counted a total of " + str(self.amount) + " apples")
            self.counted = True

    def lock(self):
        if self.locked:
            print("Barrel is already locked!")
        else:
            self.locked = True
            print("Locked the barrel")

    def sell(self):
        if self.locked and self.counted:
            print("Sold " + str(self.amount) + " apples for a total of $" + str(self.price*self.amount))
            self.amount = 0
        else:
            if not self.locked:
                print("Barrel is not locked")
            if not self.counted:
                print("Apples are not counted")


def main():
    cache_sys = CacheSystem([1, 2, 3])
    print(cache_sys.data)
    print(cache_sys.data)
    del cache_sys.data
    print(cache_sys.data)
    cache_sys.data = [4, 5, 6]
    print(cache_sys.data)
    apple_counter = AppleCounter(34)
    apple_counter.manager()


if __name__ == "__main__":
    main()
