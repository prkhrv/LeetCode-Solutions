class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic={}
        while headA:
            dic[headA]=1
            headA=headA.next
        while headB:
            if headB in dic.keys():
                return headB
            headB=headB.next
        return None
