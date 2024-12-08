from quiztest import *
file = open("Textfile.txt","r")
def test01():
    assert ShowEditedData(file) == ''