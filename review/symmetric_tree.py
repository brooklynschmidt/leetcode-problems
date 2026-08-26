# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            
            if left.val == right.val:
                return helper(left.left, right.right) and helper(right.left, left.right)
            else:
                return False
        
        return helper(root.left, root.right)
        
