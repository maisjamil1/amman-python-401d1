from pets_world.pets import Pet, Dog, Cat
import pytest

# you can skip test cases using this decorator
# @pytest.mark.skip(reason='Testing Count')
def test_cat_greet(prep_data):
    # prep_data fixture is passed to provide this test case with needed data
    # prep_data return a dictionary of all instances
    expected = 'Meooow, my nick name is Shosho'
    actual = prep_data['sherry'].speak()
    assert actual == expected

# @pytest.mark.skip(reason='Testing Count')
def test_greet(prep_data):
    expected = f"Hello, my name is {prep_data['oscar'].name}"
    actual = prep_data['oscar'].greet()
    assert actual == expected

# A fixture is a way to provide test cases with some initial data
@pytest.fixture
def prep_data():
    sherry = Cat('Sherry R', 'Shosho') # preparing data
    oscar = Dog("Oscar D") #preparing data
    d1 = Dog('D')
    c = Cat('C', 'CN')
    d2 = Dog('Another D')
    return {'oscar':oscar, 'sherry':sherry, 'd1':d1, 'c':c, 'd2':d2}

def test_count(prep_data):
    assert Pet.count == 15 # because we called prep_data 3 times

