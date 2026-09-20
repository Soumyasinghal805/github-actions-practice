import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone


def test_is_valid_email_true():
    """Test a well-formed email."""
    email = "student@lpu.in"
    result = is_valid_email(email)
    assert result is True


def test_is_valid_email_false():
    """Test a malformed email is rejected."""
    assert is_valid_email("not-an-email") is False


def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)


def test_is_valid_phone_true():
    """Test a well-formed phone number with dashes."""
    phone = "555-123-4567"
    result = is_valid_phone(phone)
    assert result is True


def test_is_valid_phone_false():
    """Test an invalid phone number is rejected."""
    assert is_valid_phone("1234") is False


def test_mask_email_basic():
    """Test masking a typical email address."""
    email = "priya@example.com"
    result = mask_email(email)
    assert result == "pr***@example.com"


def test_mask_email_invalid_raises():
    """Test masking an invalid email raises ValueError."""
    with pytest.raises(ValueError):
        mask_email("bad-email")


def test_normalize_phone_true():
    """Test phone normalization strips dashes."""
    assert normalize_phone("555-123-4567") == "5551234567"


def test_normalize_phone_invalid_raises():
    """Test invalid phones raise ValueError."""
    with pytest.raises(ValueError):
        normalize_phone("123")
