from ll_zip import __version__

from ll_zip.ll_zip import *


def test_happy_path():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    actual=zipLists(ll1, ll2)
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> ( 5 ) -> ( 6 ) -> None'
    
    assert actual==expected

def test_expected_failure(): 
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)
    actual=zipLists(ll1, ll2)
    expected='there empty Linked List'
    
    assert actual==expected

def test_edge_case():
    ll1 = LinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)
    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(4)
    actual=zipLists(ll1, ll2)
    expected='( 1 ) -> ( 2 ) -> ( 3 ) -> ( 4 ) -> ( 5 ) -> None'
    
    assert actual==expected



def test_version():
    assert __version__ == '0.1.0'
