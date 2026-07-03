class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end= " -> ")
        curr = curr.next
    print('None')
Node4 = LinkedList(4 ,None)
Node3 = LinkedList(3, Node4)
Node2 = LinkedList(2, Node3)
head = LinkedList(1, Node2)
reverse_head = reverse_linked_list(head)
print_linked_list(reverse_head)