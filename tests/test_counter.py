from lib.counter import Counter

def test_initial_count_is_zero():
    counter = Counter()
    assert counter.count == 0

def test_counter_works():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5
    counter.add(3)
    assert counter.count == 8

def test_report_returns_correct_string():
    counter = Counter()
    counter.add(6)
    result = counter.report()
    assert result == "Counted to 6 so far."