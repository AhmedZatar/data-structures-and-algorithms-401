from linked_list import __version__
from linked_list.linked_list import (
    Node,
    LinkedList,   
)


def test_version():
    assert __version__ == '0.1.0'


def test_instantiate_empty_linked_list():
    # Can successfully instantiate an empty linked list
    ll1 = LinkedList()
    ll1.append()
    actual = ll1.__str__()
    expected='{ None } -> NULL'
    assert actual==expected

def test_insert():
    # Can properly insert into the linked list
    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(6)
    ll2.insert(4)
    actual=ll2.head.value
    expected=4
    assert actual==expected

def test_head_value():
    # The head property will properly point to the first node in the linked list
    ll7 = LinkedList()
    ll7.insert(4)
    actual=ll7.head.value
    expected=4
    assert actual==expected

def test_insert_and_head_value():
    # Can properly insert multiple nodes into the linked list
    ll3 = LinkedList()
    ll3.insert(1)
    ll3.insert('Ahmed')
    ll3.insert()
    actual = ll3.__str__()
    expected='{ None } -> { Ahmed } -> { 1 } -> NULL'
    assert actual==expected

def test_includes_True():
    # Will return true when finding a value within the linked list that exists
    ll4 = LinkedList()
    ll4.append(1)
    ll4.append(2)
    ll4.append(3)
    actual = ll4.includes(1)
    expected=True
    assert actual==expected

def test_includes_False():
    # Will return false when searching for a value in the linked list that does not exist
    ll5 = LinkedList()
    ll5.append(1)
    ll5.append(2)
    ll5.append(3)
    actual = ll5.includes(4)
    expected=False
    assert actual==expected

ll = LinkedList()
def test_return_all_values():
    # Can properly return a collection of all the values that exist in the linked list
    ll6 = LinkedList()
    ll6.append(1)
    ll6.append(2)
    ll6.append(3)
    actual = ll6.__str__()
    expected='{ 1 } -> { 2 } -> { 3 } -> NULL'
    assert actual==expected



    
