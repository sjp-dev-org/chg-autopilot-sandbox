from inventory.stock import Item, Ledger


def test_reserve_within_available():
    ledger = Ledger()
    ledger.add(Item("a", on_hand=5))
    assert ledger.reserve("a", 3)
    assert ledger.available("a") == 2


def test_reserve_unknown_sku():
    assert not Ledger().reserve("missing", 1)


def test_release_more_than_reserved_clamps_to_zero():
    ledger = Ledger()
    ledger.add(Item("A", on_hand=10, reserved=2))
    ledger.release("A", 5)
    assert ledger.items["A"].reserved == 0
    assert ledger.available("A") == 10


def test_release_partial_and_exact():
    ledger = Ledger()
    ledger.add(Item("A", on_hand=10, reserved=4))
    ledger.release("A", 1)
    assert ledger.items["A"].reserved == 3
    ledger.release("A", 3)
    assert ledger.items["A"].reserved == 0
    ledger.release("A", 0)
    assert ledger.items["A"].reserved == 0
