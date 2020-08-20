class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def __str__(self):
        current = self.head
        output = ''
        while current:
            output += f"<{current.value}>,"
            current = current.next
        return output
        # <4>,<8>,<15>,<16>,<23>,<42>,


if __name__=="__main__":
    fruits = LinkedList()
    fruits.append('Apple')
    fruits.append('Orange')
    fruits.append('Banana')
    print(fruits)
