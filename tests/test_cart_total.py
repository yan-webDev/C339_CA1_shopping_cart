import pytest

from src.cart_total import calculate_total


@pytest.mark.parametrize(
    "unit_price_cents, quantity, expected_total",
    [
        (250, 4, 1000),  # normal purchase
        (1, 1, 1),  # smallest positive price and quantity
        (0, 5, 0),  # zero unit price gives zero total
        (250, 0, 0),  # zero quantity gives zero total
        (0, 0, 0),  # zero price and zero quantity give zero total
    ],
)
def test_calculate_total_with_valid_inputs_returns_total(
    unit_price_cents, quantity, expected_total
):
    # Act
    result = calculate_total(unit_price_cents, quantity)
    # Assert
    assert result == expected_total


@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        (-1, 5),  # negative unit price
        (250, -1),  # negative quantity
    ],
)
def test_calculate_total_with_negative_value_raises_value_error(
    unit_price_cents, quantity
):
    # Act and Assert
    with pytest.raises(ValueError, match="price and quantity must be nonnegative"):
        calculate_total(unit_price_cents, quantity)


@pytest.mark.parametrize(
    "unit_price_cents, quantity",
    [
        ("250", 4),  # unit price is a string
        (2.5, 4),  # unit price is a float
        (True, 4),  # unit price is a Boolean
        (250, "4"),  # quantity is a string
        (250, 2.0),  # quantity is a float
        (250, True),  # quantity is a Boolean
    ],
)
def test_calculate_total_with_invalid_type_raises_type_error(
    unit_price_cents, quantity
):
    # Act and Assert
    with pytest.raises(TypeError, match="price and quantity must be integers"):
        calculate_total(unit_price_cents, quantity)