
import app

def test_square():
    sq = app.Square(6)
    assert sq.area() == 31

def test_square2():
    sq = app.Square(6)
    assert sq.area() == 36


if __name__ == '__main__':
    print(test_square())