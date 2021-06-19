from stacks_and_queues import __version__
from stacks_and_queues.stacks_and_queues import (
    Node,
    Stack,
    Queue,

)
import pytest

# @pytest.mark.skip("todo")
def test_push(stack_3_vals):
    # Can successfully push multiple values onto a stack
    actual = stack_3_vals.top.value
    expected = 'd'
    assert actual == expected

# @pytest.mark.skip("todo")
def test_pop(stack_3_vals):
    # Can successfully pop off the stack
    actual = stack_3_vals.pop()
    expected = 'd'
    assert actual == expected
    assert stack_3_vals.top.value == -7

# @pytest.mark.skip("todo")
def test_is_empty_true(stack_3_vals):
    stack_3_vals.pop()
    stack_3_vals.pop()
    stack_3_vals.pop()
    assert stack_3_vals.isEmpty() == True


# @pytest.mark.skip("todo")
def test_peek_stack(stack_3_vals):
    # Can successfully peek the next item on the stack
    actual = stack_3_vals.peek()
    expected = 'd'
    assert actual == expected
    assert stack_3_vals.top.value == 'd'

# @pytest.mark.skip("todo")
def test_is_empty_stack(stack_3_vals):
    assert stack_3_vals.isEmpty() == False

def test_stack_exception(stack_3_vals):
# Calling pop or peek on empty stack raises exception
    stack_3_vals.pop()
    stack_3_vals.pop()
    stack_3_vals.pop()
    assert stack_3_vals.pop()=='The Stack is empty'
    assert stack_3_vals.peek()=='The Stack is empty'


# Decorator
@pytest.fixture
def stack_3_vals():
    stack = Stack()
    stack.push(3)
    stack.push(-7)
    stack.push('d')
    return stack

# ------------------------------------------------------------------------

# @pytest.mark.skip("todo")
def test_enqueue(queue_vals):
    # Can successfully enqueue multiple values into a queue
    assert queue_vals.rear.value == 6
    assert queue_vals.front.value == 8

# @pytest.mark.skip("todo")
def test_dequeue(queue_vals):
    # Can successfully dequeue out of a queue the expected value
    data = queue_vals.dequeue()
    assert data == 8
    assert queue_vals.front.value == 'hi'

# @pytest.mark.skip("todo")
def test_peek_queue(queue_vals):
    # Can successfully peek into a queue, seeing the expected value
    assert queue_vals.peek()==8

def test_is_empty_true(queue_vals):
    # Can successfully empty a queue after multiple dequeues
    data = queue_vals.dequeue()
    data = queue_vals.dequeue()
    data = queue_vals.dequeue()
    data = queue_vals.dequeue()
    assert queue_vals.isEmpty()==True


def test_queue_exception(queue_vals):
    queue_vals.dequeue()
    queue_vals.dequeue()
    queue_vals.dequeue()
    queue_vals.dequeue()
    assert queue_vals.dequeue()=='The Queue is empty'
    assert queue_vals.peek()=='The Queue is empty'



# @pytest.mark.skip("todo")
def test_is_empty_Queue(queue_vals):

    assert queue_vals.isEmpty()==False



@pytest.fixture
def queue_vals():
    queue = Queue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue

# ------------------------------------------------------------------------
def test_version():
    assert __version__ == '0.1.0'
