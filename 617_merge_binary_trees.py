class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(node1,node2):
            if node1 == None and node2 == None:
                return None
            if node1 == None:
                return node2
            if node2 == None:
                return node1
            node1.val += node2.val
            node1.left = merge(node1.left,node2.left)
            node1.right = merge(node1.right,node2.right)
            
            return node1
        return merge(root1,root2)
