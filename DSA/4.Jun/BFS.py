from collections import deque
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
def BFS(root):
    queue = deque([root])
    result = []
    while queue:
        size = len(queue)
        level = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result
    # while queue:
    #     node = queue.popleft()
    #     result.append(node.val)
    #     if node.left:
    #         queue.append(node.left)
    #     if node.right:
    #         queue.append(node.right)
    # return result
print(BFS(root))