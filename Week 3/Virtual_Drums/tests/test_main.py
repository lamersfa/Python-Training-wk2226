import pytest

from main import int_check, color_check, length_check


@pytest.mark.parametrize('test_input, output', [(['1', '2', '3'], [1, 2, 3]), (['2'], [2]), (['11', '1'], [11, 1])])
def test_int_check_pass(test_input, output):
    result = int_check(test_input)
    assert result == output


@pytest.mark.parametrize('test_input', [['1', 'ab', '3'], ['a'], ['11', 'c']])
def test_int_check_fail(test_input):
    with pytest.raises(Exception):
        int_check(input)


@pytest.mark.parametrize('test_input', [[1, 2, 3], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8, 9]])
def test_color_check_pass(test_input):
    assert color_check(test_input)


@pytest.mark.parametrize('test_input', [[1], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4, 5]])
def test_color_check_fail(test_input):
    with pytest.raises(Exception):
        color_check(test_input)


@pytest.mark.parametrize('test_input, number', [([1, 2, 3], 3), ([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4, 5, 6, 7, 8], 8)])
def test_length_check_pass(test_input, number):
    assert length_check(test_input, number)


@pytest.mark.parametrize('test_input, number', [([1, 2, 3], 2), ([1, 2, 3, 4, 5], 1), ([1, 2, 3, 4, 5, 6, 7, 8], -1)])
def test_length_check_fail(test_input, number):
    with pytest.raises(Exception):
        length_check(test_input, number)
