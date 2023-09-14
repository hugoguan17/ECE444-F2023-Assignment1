from utils import utils

def test_reverse_int():
    assert utils.reversed(123) == 321
    assert utils.reversed(-123) == -321

def test_reverse_float():
    try:
        utils.reversed(1.23)
    except TypeError as e:
        assert str(e) == "Input must be an integer"


def test_reverse_string():
    try:
        utils.reversed("1.23")
    except TypeError as e:
        assert str(e) == "Input must be an integer"

def test_formatter_int():
    output = utils.formater(123)

    assert output[0] == 1111011
    assert output[1] == 173

    output = utils.formater(-123)
    assert output[0] == -1111011
    assert output[1] == -173

def test_formatter_float():
    try:
        utils.formater(1.23)
    except TypeError as e:
        assert str(e) == "Input must be an integer"

def test_formatter_string():
    try:
        utils.formater("1.23")
    except TypeError as e:
        assert str(e) == "Input must be an integer"




test_reverse_int()
test_reverse_float()
test_reverse_string()
test_formatter_int()
test_formatter_float()
test_formatter_string()

print("All tests passed!")