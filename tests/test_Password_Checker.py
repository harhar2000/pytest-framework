import pytest
from lib.Password_Checker import Password_Checker

def test_valid_password():
    password_checker = Password_Checker()
    assert password_checker.check("password13") == True


def test_invalid_password():
    password_checker = Password_Checker()
    with pytest.raises(Exception) as e:
        password_checker.check("Book")
    assert str(e.value) == "Invalid password, must be 8+ characters."