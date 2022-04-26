
import app

def test_square():
    sq = app.Square(6)
    assert sq.area() == 31


if __name__ == '__main__':
    print(test_square())