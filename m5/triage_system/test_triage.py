from .triage import TriageSystem

def test_basic_order():
    TriageSystem._arrival_counter = 0
    t = TriageSystem()
    t.AddPatient("A", 3)
    t.AddPatient("B", 5)
    t.AddPatient("C", 5)  
    assert t.Size() == 3
    assert t.PeekNext() == ("B", 5)
    assert t.ProcessNext() == ("B", 5)
    assert t.ProcessNext() == ("C", 5)
    assert t.ProcessNext() == ("A", 3)
    assert t.ProcessNext() is None

def test_validation():
    t = TriageSystem()
    try:
        t.AddPatient("", 3)
        assert False, "expected ValueError"
    except ValueError:
        pass
    try:
        t.AddPatient("X", 6)
        assert False, "expected ValueError"
    except ValueError:
        pass