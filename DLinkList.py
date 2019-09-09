class DNode:
    def __init__(self, elem=None, next_=None, prev=None):
        self.elem = elem
        self.next = next_
        self.prev = prev


class DLinkList:
    def __init__(self):
        self.head = DNode()
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length is 0

    def clear(self):
        self.tail = None
        self.head.next.prev = None
        self.head.next = None
        self.length = 0

    def status(self):
        if self.is_empty():
            print("The double list is empty.")
        else:
            print("The double list is not empty.")

    def prepend(self, elem):
        dnode = DNode(elem)
        if self.is_empty():
            self.head.next = dnode
            dnode.prev = self.head
            self.tail = dnode
        else:
            dnode.next = self.head.next
            self.head.next = dnode
            dnode.next.prev = dnode
            dnode.prev = self.head
        self.length += 1

    def append(self, elem):
        dnode = DNode(elem)
        if self.is_empty():
            self.head.next = dnode
            dnode.prev = self.head
            self.tail = dnode
        else:
            self.tail.next = dnode
            dnode.prev = self.tail
            self.tail = dnode
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        elif self.length is 1:
            self.clear()
        else:
            p = self.head.next
            pre = self.head
            while p is not self.tail:
                pre, p = p, p.next
            self.tail = pre
            p.prev = None
            pre.next = None
            self.length -= 1

    def pop_left(self):
        if self.is_empty():
            return
        elif self.length is 1:
            self.clear()
        else:
            p = self.head.next
            p.next.prev = p.prev
            self.head.next = p.next
            self.length -= 1

    def print_all(self):
        if self.is_empty():
            return
        p = self.head.next
        while p is not None:
            print(p.elem)
            p = p.next

    def for_each(self, proc):
        if self.is_empty():
            return
        p = self.head.next
        while p is not None:
            proc(p.elem)
            p = p.next

    def find(self, elem):
        if self.is_empty():
            return
        p = self.head.next
        i = 1
        while p is not None:
            if p.elem is elem:
                return i
            else:
                p = p.next
        return

    def locate(self, index):
        if self.is_empty():
            return
        if index <= 0 or index > self.length:
            return
        p = self.head.next
        for i in range(index):
            p = p.next
        return p.elem

    def insert(self, elem, index):
        if index <=0 or index > self.length+1:
            return
        elif index is 1:
            self.prepend(elem)
        elif index is self.length+1:
            self.append(elem)
        else:
            p = self.head.next
            for i in range(1, index):
                p = p.next
                dnode = DNode(elem)
                dnode.next = p.next
                dnode.next.prev = dnode
                p.next = dnode
                dnode.prev = p
            self.length += 1

    def delete(self , index):
        if index <=0 or index > self.length:
            return
        p = self.head.next
        pre = self.head
        for i in range(index):
            pre, p = p, p.next
        p.next.prev = p.prev
        pre.next = p.next
        self.length -= 1

    def destroy(self):
        self.clear()
        self.head = None
        print("The double list has been successfully destroyed.")

DL = DLinkList()
DL.status()
for i in range(10):
    DL.append(i)
print(len(DL))
for i in range(10, 20):
    DL.prepend(i)
DL.print_all()
DL.for_each(print)
print(len(DL))
DL.status()
DL.insert(33,12)
print(len(DL))
DL.delete(16)
print(DL.locate(14))
print(DL.find(33))
for i in range(15):
    DL.pop()
print(len(DL))
DL.print_all()
DL.for_each(print)
DL.clear()
DL.status()
DL.destroy()
