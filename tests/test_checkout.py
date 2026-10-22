"""CU02: camino válido, tabla de decisión, frontera mínima y entradas inválidas."""

import pytest

from swaglab.checkout import Customer, validate_checkout

pytestmark = pytest.mark.cu02


def test_Q01_complete_data_are_accepted():
    """Q01: la combinación con los tres campos presentes permite continuar."""
    result = validate_checkout("Amaury", "Leonardo", "10000", 1)
    assert result == Customer("Amaury", "Leonardo", "10000")


def test_Q02_one_character_is_accepted():
    """Q02: un carácter no vacío cumple el límite inferior de este módulo."""
    assert validate_checkout("A", "L", "1", 1) == Customer("A", "L", "1")


def test_Q03_surrounding_spaces_are_trimmed():
    """Q03: se normalizan espacios laterales sin alterar el texto interno."""
    assert validate_checkout("  Ana María  ", " Pérez ", " 10000 ", 1) == Customer(
        "Ana María", "Pérez", "10000"
    )


@pytest.mark.parametrize(
    "first,last,postal,message",
    [
        pytest.param("", "Leonardo", "10000", "First Name is required", id="Q04_011"),
        pytest.param("Amaury", "", "10000", "Last Name is required", id="Q05_101"),
        pytest.param("Amaury", "Leonardo", "", "Postal Code is required", id="Q06_110"),
        pytest.param("", "", "10000", "First Name is required", id="Q07_001"),
        pytest.param("", "Leonardo", "", "First Name is required", id="Q08_010"),
        pytest.param("Amaury", "", "", "Last Name is required", id="Q09_100"),
        pytest.param("", "", "", "First Name is required", id="Q10_000"),
    ],
)
def test_required_fields_decision_table(first, last, postal, message):
    """Q04-Q10: se cubren las siete combinaciones inválidas y el orden del error."""
    with pytest.raises(ValueError) as caught:
        validate_checkout(first, last, postal, 1)
    assert str(caught.value) == message


@pytest.mark.parametrize(
    "first,last,postal,message",
    [
        pytest.param("  ", "Leonardo", "10000", "First Name is required", id="Q11_spaces_first"),
        pytest.param("Amaury", "\t", "10000", "Last Name is required", id="Q12_spaces_last"),
        pytest.param("Amaury", "Leonardo", "\n ", "Postal Code is required", id="Q13_spaces_postal"),
    ],
)
def test_whitespace_only_is_rejected(first, last, postal, message):
    """Q11-Q13: espacios, tabulaciones y saltos de línea no satisfacen obligatoriedad."""
    with pytest.raises(ValueError) as caught:
        validate_checkout(first, last, postal, 1)
    assert str(caught.value) == message


@pytest.mark.parametrize(
    "first,last,postal,message",
    [
        pytest.param(None, "Leonardo", "10000", "First Name must be text", id="Q14_type_first"),
        pytest.param("Amaury", [], "10000", "Last Name must be text", id="Q15_type_last"),
        pytest.param("Amaury", "Leonardo", 10000, "Postal Code must be text", id="Q16_type_postal"),
    ],
)
def test_non_text_fields_are_rejected(first, last, postal, message):
    """Q14-Q16: entradas de tipo incorrecto producen un error controlado."""
    with pytest.raises(TypeError) as caught:
        validate_checkout(first, last, postal, 1)
    assert str(caught.value) == message


@pytest.mark.parametrize(
    "count,error,message",
    [
        pytest.param(0, ValueError, "Cart must contain at least one product", id="Q17_zero"),
        pytest.param(-1, ValueError, "Cart must contain at least one product", id="Q18_negative"),
        pytest.param(True, TypeError, "Item count must be an integer", id="Q19_boolean"),
        pytest.param("1", TypeError, "Item count must be an integer", id="Q20_text"),
        pytest.param(1.0, TypeError, "Item count must be an integer", id="Q21_float"),
    ],
)
def test_invalid_item_count_is_rejected(count, error, message):
    """Q17-Q21: se rechazan carrito vacío, cantidad negativa y tipos no enteros."""
    with pytest.raises(error) as caught:
        validate_checkout("Amaury", "Leonardo", "10000", count)
    assert str(caught.value) == message


def test_Q22_multiple_products_are_accepted():
    """Q22: dos artículos también satisfacen la precondición de compra."""
    assert validate_checkout("Amaury", "Leonardo", "10000", 2) == Customer(
        "Amaury", "Leonardo", "10000"
    )
