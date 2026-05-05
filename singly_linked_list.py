class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.n = 0
    
    def build_forward(self, items):
        for x in items:
            node = Node(x)
            if not self.head:
                self.head = self.tail = node
            else:
                self.tail.next = node
                self.tail = node
            self.n += 1
    
    def build_backward(self, items):
        for x in items:
            node = Node(x)
            if not self.head:
                self.head = self.tail = node
            else:
                node.next = self.head
                self.head = node
            self.n += 1
    
    def delete_first(self):
        if not self.head:
            return
        self.head = self.head.next
        if not self.head:
            self.tail = None
        self.n -= 1
    
    def delete_last(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
            self.n -= 1
            return
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        cur.next = None
        self.tail = cur
        self.n -= 1
    
    def delete(self, val):
        if not self.head:
            return
        if self.head.data == val:
            self.delete_first()
            return
        cur = self.head
        while cur.next and cur.next.data != val:
            cur = cur.next
        if cur.next:
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
            self.n -= 1
    
    def remove_all(self, val):
        while self.head and self.head.data == val:
            self.head = self.head.next
            self.n -= 1
        if not self.head:
            self.tail = None
            return
        cur = self.head
        while cur.next:
            if cur.next.data == val:
                cur.next = cur.next.next
                self.n -= 1
                if not cur.next:
                    self.tail = cur
            else:
                cur = cur.next
    
    def reverse_display(self):
        s = []
        cur = self.head
        while cur:
            s.append(cur.data)
            cur = cur.next
        out = []
        while s:
            out.append(str(s.pop()))
        return "None <- " + " <- ".join(out) + " <- Head"
    
    def __str__(self):
        if not self.head:
            return "Head -> None"
        out = ["Head"]
        cur = self.head
        while cur:
            out.append(str(cur.data))
            cur = cur.next
        out.append("None")
        return " -> ".join(out)