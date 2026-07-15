class Tree:
    def __init__(self, val=0, left= None, right = None):
        self.val = val
        self.left = left
        self.right = right
    def check_isvalidate(root):
        def check_node(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return check_node(node.left, low, node.val) and check_node(node.right, node.val, high)
        return check_node(root, float('-inf'), float('inf'))

node1 = Tree(1)
node3 = Tree(3)
node2 = Tree(2, node1, node3)
print(node2.check_isvalidate())

node3 = Tree(3)
node6 = Tree(6)
node4 = Tree(4, node3, node6)
node1 = Tree(1)
node5 = Tree(5, node1, node4)
print(node5.check_isvalidate())
