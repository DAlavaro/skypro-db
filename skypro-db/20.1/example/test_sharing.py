import pytest
from conftest import number_42


def test_ok(number_42):
    assert number_42 == 42



@pytest.mark.xfail()
def test_failed(number_42):
    assert number_42 == 2