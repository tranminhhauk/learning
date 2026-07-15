class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val     
        self.left = left     
        self.right = right
def max_depth(root):
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
node15 = Tree(15)
node7 = Tree(7)
node20 = Tree(20, node15, node7)
node9 = Tree(9)
root = Tree(3, node9, node20)
print(max_depth(root))

node20 = Tree(20)
node13 = Tree(13, None, None)
node1 = Tree(1, None, None)
node15 = Tree(15, node13, node20)
node5 = Tree(5, node1, None)
root = Tree(10, node5, node15)

print(max_depth(root))