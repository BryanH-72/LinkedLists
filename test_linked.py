from singly_linked_list import LinkedList

def main():
    print("--- Build a forward list ---")
    lst = LinkedList()
    lst.build_forward([10, 20, 30, 40, 50])
    print(lst)
    
    lst.delete_first()
    print("Delete the first node:", lst)
    
    lst.delete_last()
    print("Delete the last node:", lst)
    
    lst.delete(30)
    print("Delete the interior node:", lst)
    
    print("\n--- Build a backward list ---")
    lst = LinkedList()
    lst.build_backward([10, 20, 30, 40, 50])
    print(lst)
    
    lst.delete_first()
    print("Delete the first node:", lst)
    
    lst.delete_last()
    print("Delete the last node:", lst)
    
    lst.delete(30)
    print("Delete the interior node:", lst)
    
    print("\n--- Non-recursive reverse print test ---")
    lst = LinkedList()
    lst.build_forward([10, 20, 30, 40, 50])
    print("Insertion order:", lst)
    print("Reverse order (non-recursive):", lst.reverse_display())
    
    print("\n--- Remove all test ---")
    lst = LinkedList()
    for x in [1, 2, 4, 6, 1, 3, 6]:
        lst.build_forward([x])
    print(lst)
    
    lst.remove_all(1)
    print("Removing 1 and all duplicates:", lst)
    
    lst.remove_all(6)
    print("Removing 6 and all duplicates:", lst)

if __name__ == "__main__":
    main()