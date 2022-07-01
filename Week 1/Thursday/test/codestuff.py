

class CodeStuff:

    def plus3(self,number):
        return number + 3

    def alwaysTrue(self):
        return True

    def format_fruit(self, fruitlist):
        returnlist = []
        for fruit in fruitlist:
            fruitstring = f"{fruit['quantity']} {fruit['fruit']}s, which cost ${fruit['price']} each."
            returnlist.append(fruitstring)
            print(fruitstring)
        return returnlist

    def price_fruit(self, fruitlist):
        returnlist = []
        for fruit in fruitlist:
            totalprice = fruit['quantity']*fruit['price']
            returnlist.append(totalprice)
        return returnlist


def main():
    code_stuff = CodeStuff()
    print(code_stuff.price_fruit([
        {
            "fruit": "apple",
            "quantity": 50,
            "price": 0.5,
        },
        {
            "fruit": "banana",
            "quantity": 10,
            "price": 0.8,
        }
    ]))


if __name__ == "__main__":
    main()
