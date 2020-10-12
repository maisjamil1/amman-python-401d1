class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

class LinkedList:

    def __init__(self, collection=None):
        self.head = None
        # if collection:
        #     for item in reversed(collection): # [a,b,c] => [a] -> [b] -> [c] -> None
        #         self.insert(item)
        if collection:
            for item in collection:
                self.append(item)


    def __str__(self):

        out = ""
        for value in self:
            out += f"[ {value} ] -> "
        return out + "None"

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
    nums = LinkedList([1,2,3,4,5,6,7,8])
    print(nums)
