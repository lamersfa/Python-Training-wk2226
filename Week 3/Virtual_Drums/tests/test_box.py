import pytest

from box import Box


@pytest.fixture
def example_box():
    return [
        'testbox',
        (1, 1),
        (3, 3),
        ['object']
    ]


def test_init(example_box):
    box = Box(example_box[0], example_box[1], example_box[2], example_box[3])
    assert not box._press_status[example_box[3][0]]


@pytest.mark.parametrize('coords, result', [((2, 2), True), ((1, 1), True), ((3, 3), True), ((1, 2), True),
                                            ((2, 3), True), ((0, 0), False), ((4, 4), False)])
def test_press(example_box, coords, result):
    box = Box(example_box[0], example_box[1], example_box[2], example_box[3])
    box.check_bounds(example_box[3][0], coords)  # turn on press
    assert box._press_status[example_box[3][0]] == result


@pytest.mark.parametrize('coords, result', [((4, 4), False), ((0, 0), False), ((1, 4), False), ((4, 1), False),
                                            ((-1, -1), True), ((2, 2), True)])
def test_release(example_box, coords, result):
    box = Box(example_box[0], example_box[1], example_box[2], example_box[3])
    box.check_bounds(example_box[3][0], (2, 2))  # turn on press
    box.check_bounds(example_box[3][0], coords)  # turn off press
    assert box._press_status[example_box[3][0]] == result

