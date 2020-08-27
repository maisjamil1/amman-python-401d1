from stacks_and_queues.stack import Stack

def test_peek_empty_stack_exception():
    stack = Stack()
    actual = stack.peek()
    expected = "Stack is empty"
    assert actual == expected

def test_push_one_value():
    stack = Stack()
    stack.push(5)
    actual = stack.top.value
    # actual = stack.peek()
    expected = 5
    assert actual == expected

