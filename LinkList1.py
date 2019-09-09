class LNode:
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next = next_


def append(elem):
    node = LNode(elem)


class LinkList:
    def __init__(self):
        self.head = LNode()
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length is 0

    def clear(self):
        self.head.next = None
        self.tail = None
        self.length = 0

    def prepend(self, elem):
        node = LNode(elem)
        if self.is_empty():
            self.head.next = node
            self.tail = node
        else:
            node.next = self.head.next
            self.head.next = node
        self.length += 1

    def append(self, elem):
        node = LNode(elem)
        if self.is_empty():
            self.head.next = node
            self.tail = node
        else:
            node.next = self.tail.next
            self.tail.next = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        elif self.length is 1:
            self.tail = None
            self.head.next = None
        else:
            q = self.head.next
            self.head.next = q.next
        self.length -= 1

    def __len__(self):
        return self.length

    def pop_right(self):
        if self.is_empty():
            return
        elif self.length is 1:
            self.tail = None
            self.head.next = None
        else:
            p = self.head.next
            pre = self.head
            while p is not self.tail:
                pre, p = p, p.next
            self.tail = pre
            self.tail.next = None
        self.length -= 1

    def print_all(self):
        if self.is_empty():
            return
        p = self.head.next
        while p is not None:
            print(p.elem)
            p = p.next

    def locate(self, elem):
        if self.is_empty():
            return None
        p = self.head.next
        i = 1
        while p is not None:
            if p.elem is elem:
                print(i)
                return i
            else:
                p = p.next
                i += 1
        return None

    def find(self, i):
        if i > self.length:
            return None
        p = self.head.next
        for j in range(i):
            p = p.next
        print(p.elem)

    def destroy(self):
        self.head.next = None
        self.tail = None
        self.length = 0
        self.head = None

    def status(self):
        if self.is_empty():
            print("The list is empty")
        else:
            print("The list is not empty")


L = LinkList()
L.status()
for i in range(10):
    L.append(i)
for i in range(10, 20):
    L.append(i)
len(L)
L.status()
L.print_all()
L.locate(17)
L.find(7)
for i in range(10):
    L.pop()
len(L)
L.print_all()
for i in range(10):
    L.pop()
L.status()
L.destroy()
print("The list has successfully destroyed.")
