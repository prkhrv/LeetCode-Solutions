# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        node = head
        len = 0
        while(node.next):
            len = len+1
            node = node.next
        
        pos = len-n
        if pos < 0:
            return head.next
        new_node = head
        for i in range(0,pos):
            new_node = new_node.next
        
        if not new_node.next:
            head = None
        else:
            new_node.next = new_node.next.next
        
        return head
        
        
        
        
        
        
        
            
        
