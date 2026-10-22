"""CU01: administrar un carrito con una unidad de cada producto."""

from dataclasses import dataclass
from decimal import Decimal
from typing import Mapping


@dataclass(frozen=True)
class Product:
    id: str
    name: str
    price: Decimal


CATALOG = {
    "backpack": Product("backpack", "Sauce Labs Backpack", Decimal("29.99")),
    "jacket": Product("jacket", "Sauce Labs Fleece Jacket", Decimal("49.99")),
}


class Cart:
    """Mantiene productos únicos; agregar o retirar de nuevo es idempotente."""

    def __init__(self, catalog: Mapping[str, Product] = CATALOG) -> None:
        self._catalog = dict(catalog)
        self._items: dict[str, Product] = {}

    def add(self, product_id: str) -> bool:
        """Devuelve True si agrega; rechaza un identificador fuera del catálogo."""
        if product_id not in self._catalog:
            raise KeyError(f"Unknown product: {product_id}")
        if product_id in self._items:
            return False
        self._items[product_id] = self._catalog[product_id]
        return True

    def remove(self, product_id: str) -> bool:
        """Devuelve False si el producto no está; preserva los demás artículos."""
        if product_id not in self._items:
            return False
        del self._items[product_id]
        return True

    @property
    def items(self) -> tuple[Product, ...]:
        return tuple(self._items.values())

    @property
    def count(self) -> int:
        return len(self._items)

    @property
    def subtotal(self) -> Decimal:
        return sum((item.price for item in self._items.values()), Decimal("0.00"))
