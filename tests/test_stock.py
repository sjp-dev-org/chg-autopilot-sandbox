from inventory.stock import Item, Ledger


def test_reserve_within_available():
    ledger = Ledger()
    ledger.add(Item("a", on_hand=5))
    assert ledger.reserve("a", 3)
    assert ledger.available("a") == 2


def test_reserve_one_more_than_available_is_refused():
    ledger = Ledger()
    ledger.add(Item("a", on_hand=5))
    assert not ledger.reserve("a", 6)
    assert ledger.available("a") == 5


def test_reserve_exactly_available():
    ledger = Ledger()
    ledger.add(Item("a", on_hand=5))
    assert ledger.reserve("a", 5)
    assert ledger.available("a") == 0
    assert not ledger.reserve("a", 1)
    assert ledger.available("a") == 0


def test_reserve_unknown_sku():
    assert not Ledger().reserve("missing", 1)
