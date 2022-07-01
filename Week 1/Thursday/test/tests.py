from code import CodeStuff


def test_plus3():
    code_stuff = CodeStuff()
    assert code_stuff.plus3(2) == 5
    print("all ok")


def main():
    test_plus3()


if __name__ == "__main__":
    main()
