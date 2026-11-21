from inventory.pricing import apply_discount, line_total


def test_line_total():
    assert line_total(250, 4) == 1000


def test_apply_discount():
    assert apply_discount(1000, 10) == 900
