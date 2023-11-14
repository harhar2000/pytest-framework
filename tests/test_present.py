import pytest
from lib.present import Present

def test_present():
    present = Present()

def wrap():
    present = Present()
    present.wrap("Toy")
    assert present.contents == "Toy"


def test_wrap_when_already_wrapped():
    present = Present()
    present.wrap("Toy")
    with pytest.raises(Exception) as e:
        present.wrap("Book")
    assert str(e.value) == "A contents has already been wrapped."


# def unwrap():
 #   present = Present()
#    with pytest.raises(Exception) as e:
#    pass

