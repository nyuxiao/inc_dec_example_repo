import inc_dec  # The code to test

# PASS TESTS

def test_many_1p():
    assert inc_dec.increment(4) == 5


# FAIL TESTS

def test_many_2f():
    assert inc_dec.increment(3) == -1


def test_many_3f():
    assert inc_dec.increment(-1) == 2


