
from linked_list import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.map = [None]*size
        self.size = size

    def hash(self, key):
        hashed_total = 0
        for char in key:
            hashed_total += ord(char)
        return hashed_total*19 % self.size

    def set(self, key, value):
        hashed_key = self.hash(key)

        if self.map[hashed_key] == None:
            self.map[hashed_key] = LinkedList()

        # If duplicate key, replace the old value with new value
        # Part of your code challenge

        self.map[hashed_key].add((key, value))


    def get(self, key):
        pass

    def contains(self, key):
        pass






# index: 157
# 'silent': 'something funny'
# 'listen': True
# 'islent': 123

# Data = [0 , , , ..... ,157 , , , 1023]


# Data[157] = ('silent', 'something funny') --> ('listen', True) --> ('islent', 123)


# hashtable.get('listen')   => True


# hash('listen')   =>  157
# Data[157]     => ('silent', 'something funny') --> ('listen', True) --> ('islent', 123)
# walk throug the linkedlist and find my key
# Return value of 'listen'  => True









