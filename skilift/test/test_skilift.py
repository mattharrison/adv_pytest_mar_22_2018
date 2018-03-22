import skilift as sk

def test_line_take():
    line = sk.Line(5)
    res = line.take(7)
    assert res == 5
    assert line.num_people == 0

def test_lift_one_bench():
    line = sk.Line(5)
    lift = sk.Lift(10, sk.Quad)
    res = lift.one_bench(line)
    assert res == {'loaded': 4, 'num_benches': 1, 'unloaded': 0}
  
