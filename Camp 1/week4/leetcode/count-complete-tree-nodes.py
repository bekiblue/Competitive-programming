# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.counter(root)
    def counter(self,node):
        #Recursive Case
        if node.left and node.right:
            return 1 + self.counter(node.left) + self.counter(node.right)
        # Base Cases
        elif node.left or node.right:
            return 2
        else:
            return 1