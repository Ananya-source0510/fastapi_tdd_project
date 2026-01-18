# utils.py
def is_even(number):
    return number % 2 == 0
# test_utils.py
def test_is_even_returns_true_for_even_number():
    assert is_even(4) is True

def test_is_even_returns_false_for_odd_number():
    assert is_even(3) is False
