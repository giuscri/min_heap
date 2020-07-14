from .main import extract_min, insert

def test_insert():
    h = []
    insert(h, 1)
    assert h[0] == 1
    insert(h, -1)
    assert h[0] == -1
    insert(h, 3)
    assert h[0] == -1

def test_extract_min():
    h = [10, 15, 30, 40, 50, 100, 40]
    assert extract_min(h) == 10
    assert extract_min(h) == 15
    assert extract_min(h) == 30
    assert extract_min(h) == 40
    assert extract_min(h) == 40
    assert extract_min(h) == 50
    assert extract_min(h) == 100
    assert len(h) == 0
