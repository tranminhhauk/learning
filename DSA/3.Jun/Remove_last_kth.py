class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def remove_last_kth(head, k):
    dummy = LinkedList(0, head)
    slow = dummy
    fast = dummy
    i = 0
    while i < k +1:
        fast = fast.next 
        i += 1
    while fast:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
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
remove = remove_last_kth(head, 2)
print_linked_list(head)