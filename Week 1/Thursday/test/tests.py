from codestuff import CodeStuff
import pytest

code_stuff = CodeStuff()


def test_plus3():
    assert code_stuff.plus3(2) == 5
    print("all ok")


def test_True():
    assert code_stuff.alwaysTrue() == True


@pytest.fixture()
def example_data():
    return [
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
    ]


def test_format(example_data):
    assert code_stuff.format_fruit(example_data) == ["50 apples, which cost $0.5 each.",
                                                     "10 bananas, which cost $0.8 each."]


def test_price(example_data):
    assert code_stuff.price_fruit(example_data) == [25, 8]


def main():
    test_format()


if __name__ == "__main__":
    main()
