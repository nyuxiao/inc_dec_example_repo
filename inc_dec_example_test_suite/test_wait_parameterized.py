import pytest
import time


@pytest.mark.parametrize("num", range(1, 10))
def test_num(num):
    time.sleep(0.3)
    assert True
