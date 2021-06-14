
from linked_list import __version__
from linked_list.linked_list import (
    Node,
    LinkedList,   
)


def test_version():
    assert __version__ == '0.1.0'


def test_instantiate_empty_linked_list():
    # Can successfully instantiate an empty linked list
    ll = LinkedList()
    ll.append()
    actual = ll.__str__()
    expected='( null ) -> None'
    assert actual==expected

def test_insert():
    # Can properly insert into the linked list
    ll = LinkedList()
    ll.append(5)
    ll.append(6)
    ll.insert(4)
    actual=ll.head.value
    expected=4
    assert actual==expected

def test_head_value():
    # The head property will properly point to the first node in the linked list
    ll = LinkedList()
    ll.insert(4)
    actual=ll.head.value
    expected=4
    assert actual==expected

def test_insert_and_head_value():
    # Can properly insert multiple nodes into the linked list
    ll = LinkedList()
    ll.insert(1)
    ll.insert('Ahmed')
    ll.insert(5)
    actual = ll.__str__()
    expected='( 5 ) -> ( Ahmed ) -> ( 1 ) -> None'
    assert actual==expected

def test_includes_True():
    # Will return true when finding a value within the linked list that exists
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.includes(1)
    expected=True
    assert actual==expected

def test_includes_False():
    # Will return false when searching for a value in the linked list that does not exist
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.includes(4)
    expected=False
    assert actual==expected

ll = LinkedList()
def test_return_all_values():
    # Can properly return a collection of all the values that exist in the linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual = ll.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> None'
    assert actual==expected

def test_add_node_end():
    # Can successfully add a node to the end of the linked list
    ll=LinkedList()
    ll.insert(1)
    ll.insert('Ahmed')
    ll.append(5)
    actual = ll.__str__()
    expected='( Ahmed ) -> ( 1 ) -> ( 5 ) -> None'
    assert actual==expected

def test_insert_node_before_middle():
    # Can successfully insert a node before a node located i the middle of a linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(4)
    ll.insertBefore(3, 2)
    
    actual = ll.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> None'
    assert actual==expected

def test_insert_node_before_head():
    # Can successfully insert a node before the first node of a linked list
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.insertBefore(2, 1)
    
    actual = ll.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> None'
    assert actual==expected

def test_insert_node_after_middle():
    # Can successfully insert after a node in the middle of the linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    ll.insertAfter(2, 3)
    
    actual = ll.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> None'
    assert actual==expected

def test_insert_node_after_end():
    # Can successfully insert a node after the last node of the linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.insertAfter(3, 4)
    
    actual = ll.__str__()
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> None'
    assert actual==expected

def test_k_greater_than_linked_list():
    # Can successfully handle method where k is greater than the length of the linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    
    actual = ll.kthFromEnd(5)
    expected='Exception'
    assert actual==expected
    
def test_k_same_the_linked_list():
    # Can successfully handle method where k and the length of the list are the same
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    
    actual = ll.kthFromEnd(4)
    expected='Exception'
    assert actual==expected

def test_k_not_postive_intger():
    # Can successfully handle method where k is not a positive integer
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    
    actual = ll.kthFromEnd(-1)
    expected="Can't enter negative input"
    assert actual==expected

def test_k_happy_path():
    # Can successfully handle method “Happy Path” where k is not at the end, but somewhere in the middle of the linked list
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    
    actual = ll.kthFromEnd(2)
    expected=3
    assert actual==expected