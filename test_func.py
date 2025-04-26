from typing import Union    
def add(a: Union[int, float], b:Union[int, float]) -> Union[int, float]:
    return a + b


def test1():
    assert 3 == add(1,1.1)


def test2():
    assert 2 == add(1, 1)


def test3():
    pass