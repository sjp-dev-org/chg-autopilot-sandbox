"""A tiny stock ledger: items, reservations and reorder checks."""

from dataclasses import dataclass, field


@dataclass
class Item:
    sku: str
    on_hand: int
    reserved: int = 0
    reorder_at: int = 0


@dataclass
class Ledger:
    items: dict[str, Item] = field(default_factory=dict)

    def add(self, item: Item) -> None:
        self.items[item.sku] = item

    def available(self, sku: str) -> int:
        item = self.items[sku]
        return item.on_hand - item.reserved

    def reserve(self, sku: str, qty: int) -> bool:
        """Reserve qty units if that many are available; returns whether it did."""
        item = self.items.get(sku)
        if item is None:
            return False
        if qty > self.available(sku):
            return False
        item.reserved += qty
        return True

    def release(self, sku: str, qty: int) -> None:
        """Release up to qty reserved units."""
        item = self.items[sku]
        item.reserved -= min(qty, item.reserved)

    def needs_reorder(self) -> list[str]:
        """SKUs whose available stock is at or below their reorder point."""
        return [s for s, i in self.items.items() if self.available(s) <= i.reorder_at]
