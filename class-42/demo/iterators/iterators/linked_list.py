class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None

        # reversed: O(n)
        # loop: O(n*1)
        if collection:
            for item in reversed(collection): # [a,b,c] => [a] -> [b] -> [c] -> None
                self.insert(item) #O(1)

        # Old way
        # # O(n*n)
        # if collection:
        #     for item in collection:
        #         self.append(item) # O(n)

    def __iter__(self):
        def values_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next
        return values_generator()

    def __str__(self):
        out = ""
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"

    def __len__(self):
        return len(list(iter(self)))

    def __eq__(self, other):
        return list(iter(self)) == list(iter(other))

    def __getitem__(self, index):
        if index < 0:
            index = len(self) + index

        for i, item in enumerate(self):
            if i == index:
                return item
        raise IndexError

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = node



if __name__ == "__main__":
    letters = LinkedList(['a', 'b', 'c', 'd', 'e'])
    other_letters = LinkedList(['a', 'r', 'c', 'd', 'e'])

    print(letters == other_letters)
    # print(nums)
    # for item in nums:
    #     print(item)
    print(letters[-1])
    print(len(letters))
    # a = [4,7,2]
    # print(a[6])

    nums = LinkedList([1,2,3,4,5,6,7,8])
    print(LinkedList([num for num in nums if num%2==0]))
