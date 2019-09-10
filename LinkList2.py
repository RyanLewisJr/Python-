class LNode:
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next = next_


class LinkList:
    def __init__(self):
        self.head = LNode()
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length is 0

    def status(self):
        if self.is_empty():
            print("The list is empty.")
        else:
            print("The list is not empty.")

    def clear(self):
        self.tail = None
        self.head.next= None
        self.length = 0

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
            self.tail.next = node
            self.tail = node
        self.length += 1

    def insert(self, elem, index):
        if index <= 0 or index > self.length+1:
            return
        elif index is 1:
            self.prepend(elem)
        elif index is self.length+1:
            self.append(elem)
        else:
            node = LNode(elem)
            p = self.head
            for i in range(index):
                p = p.next
            node.next = p.next
            p.next = node
            self.length += 1

    def pop(self):
        if self.is_empty():
            return
        else:
            p = self.head.next
            pre = self.head
            while p is not self.tail:
                pre, p = p, p.next
            self.tail = pre
            pre.next = None
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

    def delete(self, index):
        if index <=0 or index > self.length:
            return
        else:
            p = self.head.next
            pre = self.head
            for i in range(index-1):
                pre, p = p, p.next
            pre.next = p.next
            self.length -= 1

    def print_all(self):
        if self.is_empty():
            return
        p = self.head.next
        while p is not None:
            print(p.elem)
            p = p.next

    def iter(self, proc):
        if self.is_empty():
            return
        p =self.head.next
        while p is not None:
            proc(p.elem)
            p = p.next

    def find_max(self):
        if self.is_empty():
            return
        else:
            p = self.head.next
            pmax = self.head.next
            while p is not None:
                if p.elem > pmax.elem:
                    pmax = p
                p = p.next
            return pmax.elem

    def find_min(self):
        if self.is_empty():
            return
        else:
            p = self.head.next
            pmin = self.head.next
            while p is not None:
                if p.elem < pmin.elem:
                    pmin = p
                p = p.next
        return pmin.elem

    def find(self, index):
        if index <= 0 or index > self.length:
            return
        p = self.head
        for i in range(index):
            p = p.next
        return p.elem

    def locate(self, elem):
        if self.is_empty():
            return
        p = self.head.next
        i = 1
        while p is not None:
            if p.elem is elem:
                return i
            p = p.next
            i += 1
        return

    def reverse(self):
        if self.is_empty():
            return
        p = self.head
        q = self.head.next
        while q:
            temp = q.next
            q.next = p
            p = q
            q = temp

    def sort(self):
        if self.is_empty():
            return
        a = []
        p = self.head.next
        while p is not None:
            a.append(p.elem)
            p = p.next
        a.sort()
        p = self.head.next
        for i in range(len(a)):
            p.elem = a[i]
            p = p.next


L = LinkList()
L.status()
for i in range(10):
    L.append(i)
print(len(L))
for i in range(10, 20):
    L.prepend(i)
print(len(L))
L.status()
L.insert(33, 12)
L.print_all()
L.delete(8)
print(len(L))
print(L.find_max())
print(L.find_min())
print(L.locate(17))
print(L.find(9))
for i in range(5):
    L.pop()
print(len(L))
for i in range(5):
    L.pop_left()
print(len(L))
L.print_all()
L.iter(print)
L.reverse()
L.sort()
L.clear()
L.clear()
print("The list has been cleared.")
