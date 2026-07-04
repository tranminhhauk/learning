class Tree:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left =  left
        self.right = right
node6 = None
node5 = Tree(12)
node4 = Tree(8)
node3 = None
node2 = Tree(15, node5, node6)
node1 = Tree(5, node3, node4)
root = Tree(10, node1, node2)

def banlace_tree(root):
    def check_height(root):
        if not root:
            return 0
        left_height = check_height(root.left)
        if left_height == -1:
            return -1
        right_height = check_height(root.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)
    total = check_height(root)
    if total == -1:
        return False
    else:
        return True
print(banlace_tree(root))