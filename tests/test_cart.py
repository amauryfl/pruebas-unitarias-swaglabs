"""CU01: estado, altas, bajas, importes y aislamiento del carrito."""

from decimal import Decimal

import pytest

from swaglab.cart import Cart, Product

pytestmark = pytest.mark.cu01


def test_C01_new_cart_is_empty(cart):
    """C01: el estado inicial no contiene productos ni importe."""
    assert cart.items == ()
    assert cart.count == 0
    assert cart.subtotal == Decimal("0.00")


def test_C02_add_known_product(cart):
    """C02: agregar una mochila actualiza producto, contador e importe."""
    added = cart.add("backpack")
    assert added is True
    assert cart.items == (Product("backpack", "Sauce Labs Backpack", Decimal("29.99")),)
    assert cart.count == 1
    assert cart.subtotal == Decimal("29.99")


def test_C03_duplicate_add_is_idempotent(cart):
    """C03: agregar de nuevo no duplica la línea ni comunica una nueva alta."""
    cart.add("backpack")
    added = cart.add("backpack")
    assert added is False
    assert cart.count == 1
    assert cart.subtotal == Decimal("29.99")


def test_C04_add_two_distinct_products(cart):
    """C04: dos productos distintos generan dos líneas y suman 79.98."""
    cart.add("backpack")
    cart.add("jacket")
    assert {item.id for item in cart.items} == {"backpack", "jacket"}
    assert cart.count == 2
    assert cart.subtotal == Decimal("79.98")


def test_C05_remove_last_product(cart):
    """C05: retirar el último producto deja contador y subtotal en cero."""
    cart.add("backpack")
    removed = cart.remove("backpack")
    assert removed is True
    assert cart.items == ()
    assert cart.count == 0
    assert cart.subtotal == Decimal("0.00")


def test_C06_remove_preserves_other_product(cart):
    """C06: retirar la mochila conserva la chaqueta y su importe."""
    cart.add("backpack")
    cart.add("jacket")
    cart.remove("backpack")
    assert [item.id for item in cart.items] == ["jacket"]
    assert cart.count == 1
    assert cart.subtotal == Decimal("49.99")


def test_C07_remove_missing_product_preserves_state(cart):
    """C07: retirar un identificador ausente no altera el contenido."""
    cart.add("backpack")
    before = (cart.items, cart.count, cart.subtotal)
    assert cart.remove("missing") is False
    assert (cart.items, cart.count, cart.subtotal) == before


def test_C08_unknown_product_is_rejected(cart):
    """C08: un producto fuera del catálogo falla sin modificar el carrito."""
    cart.add("backpack")
    before = (cart.items, cart.count, cart.subtotal)
    with pytest.raises(KeyError, match="Unknown product: missing"):
        cart.add("missing")
    assert (cart.items, cart.count, cart.subtotal) == before


def test_C09_cart_instances_are_isolated(cart):
    """C09: modificar un carrito no cambia el de otro comprador."""
    second = Cart()
    cart.add("backpack")
    assert second.items == ()
    assert second.count == 0
    assert second.subtotal == Decimal("0.00")


def test_C10_money_uses_exact_decimal_arithmetic():
    """C10: 0.10 más 0.20 debe dar exactamente 0.30."""
    cart = Cart({
        "a": Product("a", "Producto A", Decimal("0.10")),
        "b": Product("b", "Producto B", Decimal("0.20")),
    })
    cart.add("a")
    cart.add("b")
    assert isinstance(cart.subtotal, Decimal)
    assert cart.subtotal == Decimal("0.30")
