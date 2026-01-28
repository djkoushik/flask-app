from square import square_num

def test_square_num():
    a = 3
    res = square_num(3)
    assert res == 9


def test_square_num2():
    a = 4
    res = square_num(4)
    assert res == 16