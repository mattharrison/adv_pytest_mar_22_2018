import skilift as sk

import pytest


@pytest.fixture
def line_n(request):
    size = request.node.get_marker(
        'line_size').args[0]
    line = sk.Line(size)
    return line


@pytest.fixture
def BenchN(request):
    _size = request.node.get_marker(
        'bench_size').args[0]
    class BSize(sk._Bench):
        size = _size
    return BSize
        

@pytest.fixture
def line_5():
    line = sk.Line(5)
    return line

@pytest.fixture
def quad_10():
    lift = sk.Lift(10, sk.Quad)
    return lift

@pytest.mark.bench_size(6)
def test_bench6(line_5, BenchN):
    lift = sk.Lift(10, BenchN)
    res = lift.one_bench(line_5)
    assert res == {'loaded': 5, 'num_benches': 1, 'unloaded': 0}

@pytest.mark.line_size(6)
def test_line6(line_n):
    res = line_n.take(7)
    assert res == 6
    


def test_line_take(line_5):
    res = line_5.take(7)
    assert res == 5 
    assert line_5.num_people == 0

def test_lift_one_bench(line_5, quad_10):
    #lift = sk.Lift(10, sk.Quad)
    res = quad_10.one_bench(line_5)
    assert res == {'loaded': 4, 'num_benches': 1, 'unloaded': 0}
  

@pytest.mark.parametrize('size', [[], None, '10'])
def test_lines_bad(size):
    with pytest.raises(TypeError):
        line = sk.Line(size)
        line.take(1)

@pytest.mark.parametrize('size,amt,answer',
    [(0, 5, 0), (5, 2, 3), (10, 0, 10)])
def test_line_sizes(size, amt, answer):
    line = sk.Line(size)
    res = line.take(amt)
    assert line.num_people == answer


def test_half_take(monkeypatch):
    def half_take(self, amount):
        amount = int(amount/2)
        if amount > self.num_people:
            amount = self.num_people
        self.num_people -= amount
        return amount

    monkeypatch.setattr(sk.Line, 'take', half_take)
    line = sk.Line(10)
    res = line.take(5)
    assert res == 2
    assert line.num_people == 8

    
