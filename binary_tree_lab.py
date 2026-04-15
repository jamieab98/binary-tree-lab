from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    
    return left if left else right


tree = TreeNode(10)
tree.left = TreeNode(4)
tree.right = TreeNode(8)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(3)
tree.left.left.left = TreeNode(1)
tree.right.left = TreeNode(7)
tree.right.right = TreeNode(9)
tree.right.right.right = TreeNode(10)
tree.right.right.right.right = TreeNode(11)

print(max_depth(tree))