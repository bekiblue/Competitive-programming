# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack=[]
        node=root 
        total=0
        while node:
            if low<=node.val<=high :
                    total+=node.val
            if node.left and node.right:
                stack.append(node.right)
                node=node.left
            elif node.left:
                node=node.left
            elif node.right:
                node=node.right
            else:
                if stack:
                    node=stack.pop()
                else:
                    node=None
        return total


                
