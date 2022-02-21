# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        
        while(node):
            next_node = node.next
            
            while(next_node):
                if node.val == next_node.val:
                    node.next = next_node.next
                    next_node = next_node.next
                else:
                    break
            
            node = node.next
        return head
