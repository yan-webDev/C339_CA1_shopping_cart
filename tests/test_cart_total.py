import pytest
from src.cart_total import calculate_total

@pytest.mark.parametrize(
    "unit_price_cents, quantity, expected_total",
    [
        (250, 4, 1000), 
        (1, 1, 1),
        (0, 5, 0),
        (250, 0, 0),
        (0, 0, 0),
    ],
)
def test_calculate_total_with_valid_inputs_returns_total(unit_price_cents, quantity, expected_total):
    #Act
    result = calculate_total(unit_price_cents,quantity)
    #Assert
    assert result == expected_total

@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        (-1, 5),
        (250, -1)
    ],
)
def test_calculate_total_with_negative_value_raises_value_error(unit_price_cents, quantity):
    #Act and Assert
    with pytest.raises(ValueError, match="price and quantity must be nonnegative"):
        calculate_total(unit_price_cents, quantity)

@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        ("250", 4),
        (2.5, 4),
        (True, 4),
        (250, "4"),
        (250, 2.0),
        (250, True),
    ],
)
def test_calculate_total_with_invalid_type_raises_type_error(unit_price_cents, quantity):
    #Act and Assert
    with pytest.raises(TypeError, match="price and quantity must be integers"):
        calculate_total(unit_price_cents, quantity)