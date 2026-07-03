class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def cycle_linked_list(head) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    else:
        return False

Node4 = LinkedList(4 ,None)
Node3 = LinkedList(3, Node4)
Node2 = LinkedList(2, Node3)
head = LinkedList(1, Node2)
Node4.next = Node2
print(cycle_linked_list(head))