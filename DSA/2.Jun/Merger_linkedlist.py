class LinkedList:
    def __init__(self, val= 0, next = None):
        self.val = val
        self.next = next
Node3 = LinkedList(7, None)
Node2= LinkedList(5, next = Node3)
Node1 = LinkedList(3, next = Node2)
l_list1 = LinkedList(1, next = Node1)

Node_4 = LinkedList(8, None)
Node_3 = LinkedList(6, next = Node_4)
Node_2 = LinkedList(4, next= Node_3)
l_list2 = LinkedList(2, next= Node_2)
 
def merge_linked_list (l_list1, l_list2):
    dummy = LinkedList()
    current = dummy
    while l_list1 and l_list2:
        if l_list1.val < l_list2.val:
            current.next = l_list1
            l_list1 = l_list1.next
        else:
            current.next = l_list2
            l_list2 = l_list2.next
        current = current.next
    if l_list1:
        current.next = l_list1
    else:
        current.next = l_list2
    return dummy.next
def print_linked_list(head):
    curr = head
    while curr:
        print(curr.val, end = " -> ")
        curr = curr.next
    print('None')

new_LinkedList = merge_linked_list(l_list1, l_list2)
print_linked_list(new_LinkedList)