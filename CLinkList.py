class LNode:
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next = next_


class CLinkList:
    def __init__(self):
        self.head = LNode()
        self.head.next = self.head
        self.tail = self.head
        self.length = 0

    def is_empty(self):
        return self.length is 0

    def __len__(self):
        return self.length

    def status(self):
        if self.is_empty():
            print("The list is empty.")
        else:
            print("The list is not empty.")

    def clear(self):
        self.head.next = self.head
        self.tail = self.head
        self.length = 0

    def destroy(self):
        self.head.next = None
        self.tail = None
        self.length = 0
        print("The list has been successfully destroyed.")

    def prepend(self, elem):
        node = LNode(elem)
        if self.is_empty():
            node.next = self.head.next
            self.head.next = node
            self.tail = node
        else:
            node.next = self.head.next
            self.head.next = node
        self.length += 1

    def append(self, elem):
        node = LNode(elem)
        if self.is_empty():
            node.next = self.head.next
            self.head.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
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
            pre.next = p.next
        self.length -= 1

    def pop_left(self):
        if self.is_empty():
            return
        elif self.length is 1:
            self.clear()
        else:
            q = self.head.next
            self.head.next = q.next
        self.length -= 1

    def print_all(self):
        if self.is_empty():
            return
        p = self.head.next
        while p is not self.head:
            print(p.elem)
            p = p.next

    def for_each(self, func):
        if self.is_empty():
            return
        p = self.head.next
        while p is not self.head:
            func(p.elem)
            p = p.next

    def locate(self, elem):
        if self.is_empty():
            return
        p = self.head.next
        i = 1
        while p is not self.head:
            if p.elem is elem:
                return i
            else:
                p = p.next
                i += 1
        return

    def find(self, index):
        if index <=0 or index > self.length:
            return
        p = self.head.next
        for i in range(1, index):
            p = p.next
        return p.elem


L = CLinkList()
L.status()
for i in range(10):
    L.append(i)
print(len(L))
for i in range(10, 20):
    L.prepend(i)
print(len(L))
L.print_all()
L.for_each(print)
L.status()
print(L.locate(17))
print(L.find(7))
for i in range(10):
    L.pop()
print(len(L))
L.status()
L.clear()
L.status()
L.destroy()
