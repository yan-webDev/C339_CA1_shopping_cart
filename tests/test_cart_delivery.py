import pytest

from src.cart_delivery import qualifies_free_delivery


@pytest.mark.parametrize(
    "total_cents, expected",
    [
        (0, False),  # empty cart does not qualify
        (4999, False),  # one cent below S$50.00 does not qualify
        (5000, True),  # exactly S$50.00 qualifies
        (5001, True),  # one cent above S$50.00 qualifies
    ],
)
def test_qualifies_free_delivery_with_valid_total_returns_expected_result(
    total_cents, expected
):
    # Act
    result = qualifies_free_delivery(total_cents)
    # Assert
    assert result is expected


def test_qualifies_free_delivery_with_negative_total_raises_value_error():
    # Arrange
    total_cents = -1
    # Act and Assert
    with pytest.raises(ValueError, match="total must be nonnegative"):
        qualifies_free_delivery(total_cents)


@pytest.mark.parametrize(
    "total_cents",
    [
        5000.0,  # total is a float
        "5000",  # total is a string
        True,  # total is a Boolean
    ],
)
def test_qualifies_free_delivery_with_invalid_type_raises_type_error(total_cents):
    # Act and Assert
    with pytest.raises(TypeError, match="total must be an integer"):
        qualifies_free_delivery(total_cents)