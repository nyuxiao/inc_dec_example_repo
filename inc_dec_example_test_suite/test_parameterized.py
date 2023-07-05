import pytest


@pytest.mark.parametrize("num", range(1, 3))
def test_odd_even(num):
    assert True


@pytest.mark.parametrize("num", range(411, 416))
def test_b(num):
    assert True
