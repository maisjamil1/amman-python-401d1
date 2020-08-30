from stacks_and_queues.node import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        # Special case: if empty queue
        # f -> 1 <- r
        if not self.front and not self.rear:
            self.front = node
            self.rear = node

        old_rear = self.rear
        self.rear = node
        old_rear.next = self.rear
        # front -> 1 -> 2 -> 3 <- rear


    def dequeue(self):
        pass

    def peek(self):
        try:
            return self.front.value
        except AttributeError as e:
            return f"Empty Queue!!!\nDevs Details: {e}"
        except Exception as e:
            return f"Some other exception happened!!! {e}"

    def is_empty(self):
        pass


if __name__ == '__main__':
    eaters = Queue()
    # print(eaters.peek())
    assert eaters.peek().startswith('Empty Queue!!!')
    eaters.enqueue("Saed")
    eaters.enqueue("Ahmad")
    # assert eaters.peek().startswith('Empty Queue!!!')
    # print(eaters.dequeue()) # should return Saed
    # print(eaters.front.value) # Saed
    # print(eaters.rear.value) # Ahmad
    # print(eaters.peek()) # Saed
    assert eaters.front.value == 'Saed'
    assert eaters.rear.value == 'Ahmad'
    # assert eaters.dequeue() == 'Saed'
    # assert eaters.dequeue() == 'Ahmad'
    print('Good job! All tests passed')



