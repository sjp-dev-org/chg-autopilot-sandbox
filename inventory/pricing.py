"""Order pricing: line totals, discounts and averages."""


def line_total(unit_price_cents: int, qty: int) -> int:
    return unit_price_cents * qty


def apply_discount(total_cents: int, percent: int) -> int:
    """Apply a percentage discount between 0 and 100."""
    return total_cents - total_cents * percent // 100


def average_price(prices_cents: list[int]) -> float:
    """Mean of the given prices."""
    return sum(prices_cents) / len(prices_cents)


def parse_qty(text: str) -> int:
    """Parse a user-entered quantity such as ' 3 '."""
    return int(text)
