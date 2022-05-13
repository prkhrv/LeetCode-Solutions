class Solution:
    def __init__(self):
        self.total = 0
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def preorder(root,val):
            if not root:
                return
            
            if root.left==None and root.right==None:
                self.total+= (val*10)+root.val
                return
            
            preorder(root.left,(val*10)+root.val)
            preorder(root.right,(val*10)+root.val)
        
        
        preorder(root,0)
        return self.total
