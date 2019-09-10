class DNode:
    def __init__(self, elem=None, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self.next = next_


class CDLinkList:
    def __init__(self):
        self.head = DNode()
        self.head.next = self.head
        self.head.prev = self.head
        self.tail = self.head
        self.length = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.length is 0

    def status(self):
        if self.is_empty():
            print("The double list is empty.")
        else:
            print("The double list is not empty.")

    def prepend(self, elem):
        dnode = DNode(elem)
        if self.is_empty():
            dnode.next = self.head.next
            dnode.prev = self.head
            dnode.next = self.head
            self.head.prev = dnode
            self.tail = dnode
        else:
            dnode.next = self.head.next
            self.head.next = dnode
            dnode.prev = self.head
            dnode.next.prev = dnode
        self.length += 1

    def append(self, elem):
        dnode = DNode(elem)
        if self.is_empty():
            dnode.next = self.head.next
            dnode.prev = self.head.prev
            self.head.next = dnode
            dnode.prev = self.head
            self.tail = dnode
        else:
            dnode.next = self.tail.next
            dnode.prev = self.tail
            self.head.prev = dnode
            self.tail.next = dnode
            self.tail = dnode
        self.length += 1

    def insert(self, index, elem):
        if index <=0 or index > self.length+1:
            return
        p = self.head
        dnode = DNode(elem)
        for i in range(index-1):
            p = p.next
        dnode.next = p.next
        p.next = dnode
        dnode.next.prev = dnode
        dnode.prev = p
        self.length += 1

    def pop(self):
        if self.is_empty():
            return
        p = self.head.next
        pre = self.head
        while p is not self.tail:
            pre, p = p, p.next
        p.prev = p.next.prev
        pre.next = p.next
        self.tail = pre
        self.length -= 1

    def pop_left(self):
        if self.is_empty():
            return
        elif self.length is 1:
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head
            self.length = 0
        else:
            q = self.head.next
            q.next.prev = q.prev
            self.head.next = q.next
            self.length -= 1

    def delete(self, index):
        if index <= 0 or index > self.length:
            return
        elif self.length is 1:
            self.head.next = self.head
            self.head.prev = self.head
            self.tail = self.head
            self.length = 0
        else:
            pre = self.head
            p = self.head.next
            for i in range(index-1):
                pre, p = p, p.next
            p.prev = p.next.prev
            pre.next = p.next
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

    def find(self, index):
        if index <=0 or index > self.length:
            return
        p = self.head.next
        for i in range(index-1):
            p = p.next
        return p.elem

    def locate(self, elem):
        if self.is_empty():
            return
        p = self.head.next
        i = 1
        while p is not self.head:
            if p.elem is elem:
                return i
            p = p.next
        return

    def find_max(self):
        if self.is_empty():
            return
        p = self.head.next
        pmax = self.head.next
        while p is not self.head:
            if p.elem > pmax.elem:
                pmax = p
            p = p.next
        return pmax.elem

    def find_min(self):
        if self.is_empty():
            return
        p = self.head.next
        pmin = self.head.next
        while p is not self.head:
            if p.elem < pmin.elem:
                pmin = p
            p = p.next
        return pmin.elem

    def del_elem(self, elem):
        if self.is_empty():
            return
        p = self.head.next
        pre = self.head
        while p is not self.head:
            if p.elem is elem:
                p.prev = p.next.prev
                pre.next = p.next
                p = pre.next
                self.length -= 1
            else:
                pre, p = p, p.next

    def substitute(self, index, elem):
        if index <= 0 or index > self.length:
            return
        p = self.head.next
        for i in range(index-1):
            p = p.next
        p.elem = elem

    def reverse(self):
        if self.length < 2:
            return
        p = self.head.next
        q = self.head.prev
        while p is not q or p.next is not q.prev:
            tmp = p.elem
            p.elem = q.elem
            q.elem = tmp
            p, q = p.next, q.prev
