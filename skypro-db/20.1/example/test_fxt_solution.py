import pytest

from app import sum_func


@pytest.fixture()
def positive_number():
    return [1, 1]


@pytest.fixture()
def negative_numbers():
    return [-1, -1]


@pytest.fixture()
def positive_and_negative():
    return [1, -1]


class TestSumFunc:
    def test_sum_positive(self):
        c = sum_func(positive_number[0], positive_number[1])
        assert c > 0
        assert c == 2

    def test_sum_positive_and_negative(self):
        c = sum_func(positive_and_negative[0], positive_and_negative[1])
        assert c == 0

    def test_sum_negative(self):
        c = sum_func(negative_numbers[0], negative_numbers[1])
        assert c < 0
        assert c == -2
