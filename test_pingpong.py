from quiztest import *

def test01():
    assert pingPong(120,90) == 'normal'

def test02():
    assert pingPong(120,120) == 'risk group'

def test03():
    assert pingPong(100,150) == 'stage 1'

def test04():
    assert pingPong(175,135) == 'stage 2'

def test05():
    assert pingPong(180,154) == 'stage 3'