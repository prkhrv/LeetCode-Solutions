# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxlevel,tsum = 0,0
        def dfs(node,level):
            nonlocal maxlevel,tsum
            if not node:
                return
            dfs(node.left,level+1)
            dfs(node.right,level+1)
            
            if level > maxlevel:
                maxlevel = level
                tsum = 0
            if level == maxlevel:
                tsum += node.val
        
        dfs(root,0)
        
        return tsum
            
            
            
            
        
