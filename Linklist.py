class LNode:
    def __init__(self,elem=None,next_=None):
        self.elem=elem
        self.next=next_


class LinkList:
    def __init__(self):
        self.head=None
        self.length=0

    def is_empty(self):
        return self.length is 0

    def prepend(self,elem):
        self.head=LNode(elem,self.head)
        self.length+=1

    def pop(self):
        if self.is_empty():
            print("The list is empty.")
        self.head = self.head.next


L=LinkList()
for i in range(10):
    L.prepend(i)
for i in range(10):
    L.pop()
