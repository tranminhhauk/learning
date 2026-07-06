class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next
def check_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    else:
        return False

node3 = ListNode(2, None)      
node2 = ListNode(3, node3)   
node1 = ListNode(2, node2)    
head = ListNode(1, node1)
node3.next = node2
print(check_cycle(head))