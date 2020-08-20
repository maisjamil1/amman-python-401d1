from linked_list import __version__
from linked_list.linked_list import LinkedList


def test_version():
    assert __version__ == '0.1.0'

def test_append_to_empty_ll():
    ll = LinkedList()
    ll.append(5)
    assert ll.head.value == 5

def test_append_two_values():
    ll = LinkedList()
    ll.append(5)
    ll.append(4)
    assert ll.head.value == 5
    assert ll.head.next.value == 4

def test_dender_str():
    ll = LinkedList()
    ll.append(5)
    ll.append(4)
    assert ll.__str__() == '<5>,<4>,'

def test_empty_ll():
    ll = LinkedList()
    assert ll.head == None
