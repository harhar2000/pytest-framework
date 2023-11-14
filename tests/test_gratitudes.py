from lib.gratitudes import Gratitudes

def add():
    gratitudes = gratitudes()
    gratitudes.add("food")
    gratitudes.add("family")
    assert "food" in gratitudes.gratitudes
    assert "family" in gratitudes.gratitudes
    assert len(gratitudes.gratitudes) == 2


def format():
    gratitudes = gratitudes()
    gratitudes.add("food")
    gratitudes.add("family")
    expected_output = "Be grateful for: health, family"
    assert gratitudes.format() == expected_output
  