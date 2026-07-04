class Tree:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left =  left
        self.right = right
def maxDepth(root):
    if not root:
        return 0
    root_left = maxDepth(root.left)
    root_right = maxDepth(root.right)
    return 1 + max(root_left, root_right)

node6 = None
node5 = Tree(12)
node4 = Tree(8)
node3 = None
node2 = Tree(15, node5, node6)
node1 = Tree(5, node3, node4)
root = Tree(10, node1, node2)
print(maxDepth(root))
