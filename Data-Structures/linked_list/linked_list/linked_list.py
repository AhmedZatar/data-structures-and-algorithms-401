class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.valueList=[]

    def insert(self, value=None):
        """
        Adds a node of a value to the head of LL
        """
        try:
          node = Node(value)
          self.valueList=[node.value]+self.valueList
          if not self.head:
              self.head = node
          else:         
              current = self.head
              self.head= node
              self.head.next=current
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}") 
              

    def append(self, value=None):
        """
        Adds a node of a value to the end of LL
        """
        try:
          node = Node(value)
          self.valueList=self.valueList+[node.value]
          if not self.head:
              self.head = node
            
          else:
              current = self.head
              while current.next != None:
                  current = current.next
              current.next = node
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}") 

    def includes(self,num):
        """
        Return T/F if value is in the linked list or not
        """
        try:
          x=False
          for value in self.valueList:
              if value==num:
                 x=True
                 break
          return x
        except Exception as e:
          raise Exception(f"Something's Going Wrong : {e}") 

               
    def __str__(self):
        """
        Loop over all nodes
        print all values in one line
        { a } -> { b } -> { c } -> NULL
        """
           
        x=''
        for value in self.valueList:
            x=x+'{ '+f'{value}'+' }' + ' -> '
        x=x+'NULL'                
        return x

    


if __name__ == "__main__":

    ll = LinkedList()  
    ll.append(4)
    ll.append(-1)
    ll.append('s')
    ll.insert(5)
    ll.append()
    print(ll.head.value)
    print(ll.head.next.value)
    print(ll.head.next.next.value)
    print(ll.head.next.next.next.value)
    print(ll.__str__())
    ll2 = LinkedList()  
    print(ll2.__str__())
    print(ll.__str__())
    print(ll.includes(-1))
    print(ll.includes('hi'))
    