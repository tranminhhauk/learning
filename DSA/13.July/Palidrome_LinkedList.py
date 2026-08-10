class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def check_palidrome (head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    curr = slow
    prev = None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True

n5 = LinkedList(1, None)
n4 = LinkedList(2, n5)
n3 = LinkedList(3, n4)
n2 = LinkedList(2, n3)
n1 = LinkedList(1, n2)
print(check_palidrome(n1)) 

node4 = LinkedList(4,None)
node3 = LinkedList(3, node4)
node2 = LinkedList(2, node3)
node1 = LinkedList(1, node2)
print(check_palidrome(node1))