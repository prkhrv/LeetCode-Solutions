# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            ldepth = Solution.maxDepth(self,root.left)
            rdepth = Solution.maxDepth(self,root.right)
            
            if (ldepth > rdepth):
                return ldepth+1
            else:
                return rdepth+1
        
