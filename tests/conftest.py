"""Cada prueba recibe un carrito nuevo para evitar dependencia del orden."""

import pytest

from swaglab.cart import Cart


@pytest.fixture
def cart():
    return Cart()
