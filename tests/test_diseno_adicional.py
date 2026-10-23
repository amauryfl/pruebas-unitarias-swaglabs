"""Casos añadidos al revisar transiciones, prioridad de errores y datos postales."""

from decimal import Decimal

import pytest

from swaglab.checkout import Customer, validate_checkout


@pytest.mark.cu01
def test_C11_remove_from_empty_cart(cart):
    """Retirar de un carrito vacío mantiene el estado inicial."""
    assert cart.remove("backpack") is False
    assert cart.items == ()
    assert cart.count == 0
    assert cart.subtotal == Decimal("0.00")


@pytest.mark.cu01
def test_C12_readd_after_removal(cart):
    """Un producto retirado puede volver a agregarse sin duplicados residuales."""
    cart.add("backpack")
    cart.remove("backpack")
    assert cart.add("backpack") is True
    assert [item.id for item in cart.items] == ["backpack"]
    assert cart.count == 1
    assert cart.subtotal == Decimal("29.99")


@pytest.mark.cu02
def test_Q23_quantity_error_has_priority():
    """La cantidad se valida antes de los tres campos vacíos."""
    with pytest.raises(ValueError) as caught:
        validate_checkout("", "", "", 0)
    assert str(caught.value) == "Cart must contain at least one product"


@pytest.mark.cu02
def test_Q24_postal_leading_zeros_are_preserved():
    """El código postal sigue siendo texto y conserva sus ceros iniciales."""
    result = validate_checkout("Ana", "Pérez", "00100", 1)
    assert result == Customer("Ana", "Pérez", "00100")
