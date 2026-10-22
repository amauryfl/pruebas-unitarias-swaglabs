"""CU02: validar los datos del comprador antes de continuar la compra."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Customer:
    first_name: str
    last_name: str
    postal_code: str


def _required_text(value: object, label: str) -> str:
    if not isinstance(value, str):
        raise TypeError(f"{label} must be text")
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{label} is required")
    return normalized


def validate_checkout(
    first_name: object,
    last_name: object,
    postal_code: object,
    item_count: object,
) -> Customer:
    """Valida carrito, nombre, apellido y postal en ese orden; no crea una orden."""
    if type(item_count) is not int:
        raise TypeError("Item count must be an integer")
    if item_count <= 0:
        raise ValueError("Cart must contain at least one product")
    first = _required_text(first_name, "First Name")
    last = _required_text(last_name, "Last Name")
    postal = _required_text(postal_code, "Postal Code")
    return Customer(first, last, postal)
