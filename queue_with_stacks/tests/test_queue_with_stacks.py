from queue_with_stacks import __version__
import pytest
from queue_with_stacks.queue_with_stacks import (
    Node,
    Stack,
    PseudoQueue,

)

def test_enqueue_happypath(queue_vals):
    actual = queue_vals.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi ) -> ( 8 )'
    assert actual == expected

def test_enqueue_Expected_failure(queue_vals):
    actual = queue_vals.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi )'
    assert actual != expected

def test_enqueue_edge_case():
    queue2 = PseudoQueue()
    actual = queue2.enqueue()
    expected = 'Please put a value'
    assert actual == expected

def test_dequeue_happypath(queue_vals):
    dequeuevalue=queue_vals.dequeue()
    actual = queue_vals.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi )'
    assert actual == expected
    assert dequeuevalue==8

def test_dequeue_Expected_failure(queue_vals):
    dequeuevalue=queue_vals.dequeue()
    actual = queue_vals.__str__()
    expected = '( 6 ) -> ( -4 ) -> ( hi ) -> ( 8 )'
    assert actual != expected
    assert dequeuevalue != 'hi'

def test_dequeue_edge_case():
    queue2 = PseudoQueue()
    actual = queue2.dequeue()
    expected = 'The Queue is empty'
    assert actual == expected


@pytest.fixture
def queue_vals():
    queue = PseudoQueue()
    queue.enqueue(8)
    queue.enqueue('hi')
    queue.enqueue(-4)
    queue.enqueue(6)
    return queue

def test_version():
    assert __version__ == '0.1.0'
