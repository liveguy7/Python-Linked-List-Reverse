
class Node:

  def __init__(self, data=None):
    self.data = data
    self.next = None

class Head:

  def __init__(self):
    self.head = None

  def print(self):
    v = self.head
    while v is not None:
      print(v.data)
      v = v.next

  def reverse(self):
    prev = None
    curr = self.head
    while(curr is not None):
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    self.head = prev


pointer = Head()
pointer.head = Node('1')
p2 = Node('2')
p3 = Node('3')

pointer.head.next = p2
p2.next = p3

pointer.print()
pointer.reverse()
pointer.print()



















