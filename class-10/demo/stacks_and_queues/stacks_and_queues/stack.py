from stacks_and_queues.node import Node

class Stack:
    def __init__(self):
        self.max = 10000
        self.top = None

    def push(self, value):
        """
        - Create a node with vlaue
        - Add the node to the top of the stack
        - check if top is None:
            - True point top to new node
            - else:
                - save top in temp (temporary)
                - top = the new node
                - reassign top.next to temp
        """
        node = Node(value)
        temp = self.top # temp = None
        self.top = node # top = node(5)
        self.top.next = temp # node(5).next = None

    def pop(self):
        pass

    def peek(self):
        try:
            return self.top.value
        except AttributeError as e:
            return "Stack is empty"

    def is_empty(self):
        pass

# pushing 3
# top -> 4 -> 5 -> None

if __name__ == '__main__':
    fruits = Stack()
    print(fruits.peek())
