from singly_linked_list import LinkedList, Node

class Split(LinkedList):
    def split(self):
        if not self.head:
            raise Exception("empty")
        
        evens = Split()
        odds = Split()
        
        cur = self.head
        self.head = None
        self.tail = None
        self.n = 0
        
        while cur:
            nxt = cur.next
            cur.next = None
            
            if cur.data % 2 == 0:
                if not evens.head:
                    evens.head = evens.tail = cur
                else:
                    evens.tail.next = cur
                    evens.tail = cur
                evens.n += 1
            else:
                if not odds.head:
                    odds.head = odds.tail = cur
                else:
                    odds.tail.next = cur
                    odds.tail = cur
                odds.n += 1
            
            cur = nxt
        
        return evens, odds

def main():
    print("--- Split Evens Odds ---")
    lst = Split()
    for x in [1,2,3,4,5,6,7,8,15,14,13,12,11,10,9]:
        lst.build_forward([x])
    
    print(lst)
    evens, odds = lst.split()
    print(evens)
    print(odds)
    print("Original (empty):", lst)

if __name__ == "__main__":
    main()