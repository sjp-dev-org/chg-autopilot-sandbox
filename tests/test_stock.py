from inventory.stock import Item, Ledger


def test_reserve_within_available():
    ledger = Ledger()
    ledger.add(Item("a", on_hand=5))
    assert ledger.reserve("a", 3)
    assert ledger.available("a") == 2


def test_reserve_unknown_sku():
    assert not Ledger().reserve("missing", 1)
