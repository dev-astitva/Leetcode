# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        def height(root):
            if root==None:
                return 0
            lh=height(root.left)
            rh=height(root.right)
            val=max(lh,rh)
            return 1+val
        
        return height(root)