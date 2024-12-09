from quiztest import *

def test01():
    assert calAge(20) == '2547'
def test02():
    assert calAge("20") == '2547'


def test03():
    assert calRank("A") == 'High Distinction'
def test04():
    assert calRank("B+") == 'Distinction'
def test05():
    assert calRank("B") == 'Distinction'
def test06():
    assert calRank("C+") == 'Good'
def test07():
    assert calRank("C") == 'Good'
def test07():
    assert calRank("D+") == 'Normal'
def test07():
    assert calRank("D") == 'Normal'
def test07():
    assert calRank("F") == 'Failed'