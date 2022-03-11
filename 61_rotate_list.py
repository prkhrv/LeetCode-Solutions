# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        firstnode = lastnode = head
        len = 0
        while(head):
            lastnode = head
            len = len+1
            head = head.next
        
        if len == 0 or k == 0:
            return firstnode
        k = k % len
        
        
        if k == 0:
            return firstnode
        
        rot = len - k
        
        if rot == 0:
            return firstnode
        
        i = 0
        temp = newfnode= firstnode
        
        while(i < rot):
            if i < rot-1:
                temp = temp.next
            newfnode = newfnode.next
            i = i+1
        
            
        lastnode.next = firstnode
        temp.next = None
        
        return newfnode
            
            
        
        
        
