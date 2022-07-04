

def list_comp(input_list):
    print([num for num in input_list if num % 2 == 0])


class Fibonacci:
    def __init__(self, amount):
        """Amount specifies the max length of the fibonacci sequence"""
        self.max_count = amount
        self.current = 0
        self.next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_count == 0:
            raise StopIteration

        self.max_count -= 1

        tempnext = self.current + self.next
        self.current = self.next
        self.next = tempnext

        return self.current



def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_comp(input_list)
    fibo = Fibonacci(8)
    for number in fibo:
        print(number)


if __name__ == "__main__":
    main()
