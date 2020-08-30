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

        # x = 7
        # y = 8
        # temp = 7
        # x = y
        # y = 8

    def pop(self):
        # top -> None
        # push(5): top ---> Node(5) -> None
        # push(7): top ---> Node(7) -> Node(5) -> None
        #            ------------------>
        # pop() This will return 7
        # top  Node(7) -> Node(5) -> None
        #  ------------------>
        # pop() This will return 5
        # top  Node(7) -> Node(5) -> None
        #  -------------------------->
        # garbage collection:
        #   a = 4         a -> 4
        #   b = 9         b -> 9
        #   a = 2         a -> 2
        #   c = 4         c -> 4


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
