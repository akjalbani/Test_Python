# this is a unit test file for our math_func.py file, first we need to import the file which contains the functions
# add test keyword begining of the methods/ units needs to be tested
import math_func

def test_add():
    assert math_func.add(7,3)==10
    assert math_func.add(7)==9
    assert math_func.add(5)==7
    

def test_product():
    assert math_func.product(5,5) == 25
    assert math_func.product(5) ==10
    assert math_func.product(7) == 14
