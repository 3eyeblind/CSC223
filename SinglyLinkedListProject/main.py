from singly_linked_list import SinglyLinkedList

def section(title: str):
    print(title)

def demo_build_forward_and_deletes():
    section("---- Build a forward list ----")
    sll = SinglyLinkedList()
    sll.build_forward_list([10, 20, 30, 40, 50])  
    sll.display()

    # Delete first
    sll.remove_first()
    print("Delete the first node:", end=" ")
    sll.display()

    # Delete last
    sll.remove_last()
    print("Delete the last node:", end=" ")
    sll.display()

    # Delete interior (remove first occurrence of 30)
    sll.remove(30)
    print("Delete the interior node:", end=" ")
    sll.display()

def demo_build_backward_and_deletes():
    section("---- Build a backward list ----")
    sll = SinglyLinkedList()
    sll.build_backward_list([10, 20, 30, 40, 50])  
    sll.display()

    # Delete first
    sll.remove_first()
    print("Delete the first node:", end=" ")
    sll.display()

    # Delete last
    sll.remove_last()
    print("Delete the last node:", end=" ")
    sll.display()

    # Delete interior (remove first occurrence of 30)
    sll.remove(30)
    print("Delete the interior node:", end=" ")
    sll.display()

def demo_reverse_prints():
    section("---- Non-recursive reverse print test----")
    sll = SinglyLinkedList()
    sll.build_forward_list([10, 20, 30, 40, 50])
    print("Insertion order:", end=" ")
    sll.display()

    print("Reverse order (recursive):", end=" ")
    sll.display_reverse()

    print("Reverse order (non-recursive):", end=" ")
    sll.display_reverse_nr()

def demo_remove_all():
    section("---- Remove all test ----")
    sll = SinglyLinkedList()
    sll.build_forward_list([1, 2, 4, 6, 1, 3, 6])
    sll.display()
    removed = sll.remove_all(1)
    print(f"Removing 1 and all duplicates:", end=" ")
    sll.display()

    removed = sll.remove_all(6)
    print(f"Removing 6 and all duplicates:", end=" ")
    sll.display()

def demo_insert_at_end_variant():
    """
    Optional: repeats the forward build steps using insert_at_end to show parity with instructions
    that mention 'insertAtEnd'. Output is not part of the sample, but useful for verification.
    """
    sll = SinglyLinkedList()
    for x in [10, 20, 30, 40, 50]:
        sll.insert_at_end(x)


if __name__ == "__main__":
    demo_build_forward_and_deletes()
    demo_build_backward_and_deletes()
    demo_reverse_prints()
    demo_remove_all()
