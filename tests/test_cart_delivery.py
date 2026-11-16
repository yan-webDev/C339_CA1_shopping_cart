import pytest
from src.cart_delivery import qualifies_free_delivery

@pytest.mark.parametrize(
    "total_cents, expected",
    [
        (0, False),
        (4999, False),
        (5000, True),
        (5001, True),

    ],
)
def test_qualifies_free_delivery_with_valid_total_returns_expected_result(total_cents, expected):
    #Act
    result = qualifies_free_delivery(total_cents)
    #Assert
    assert result is expected

def test_qualifies_free_delivery_with_negative_total_raises_value_error():
    #Arrange
    total_cents = -1
    #Act and Assert
    with pytest.raises(ValueError, match="total must be nonnegative"):
        qualifies_free_delivery(total_cents)

@pytest.mark.parametrize(
    "total_cents",
    [
        5000.0,
        "5000",
        True,
    ],
)
def test_qualifies_free_delivery_with_invalid_type_raises_type_error(total_cents):
    #Act and Assert
    with pytest.raises(TypeError, match="total must be an integer"):
        qualifies_free_delivery(total_cents)