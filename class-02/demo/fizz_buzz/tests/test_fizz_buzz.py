from fizz_buzz import __version__
from fizz_buzz.fizz_buzz import a, fizz_buzz, fizz_buzz_as_list


def test_version():
    assert __version__ == '0.1.0'

def test_six():
    assert a == 6

# 1 2 3       4  5         15
# 1 2 'Fizz'  4  'Buzz'    'FizzBuzz'

def test_one():
    assert fizz_buzz(1) == 1

def test_three():
    expected = 'Fizz'
    actual = fizz_buzz(3)
    assert actual == expected

def test_five():
    expected = 'Buzz'
    actual = fizz_buzz(5)
    assert actual == expected

def test_eleven():
    expected = 11
    actual = fizz_buzz(11)
    assert actual == expected

def test_thirty():
    expected = 'FizzBuzz'
    actual = fizz_buzz(30)
    assert actual == expected

def test_list_of_nums():
    expected = [1,2,'Fizz',4,'Buzz','Fizz',7]
    actual = fizz_buzz_as_list([1,2,3,4,5,6,7])
    assert actual == expected
