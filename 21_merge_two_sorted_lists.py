class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            return ListNode(list1.val,self.mergeTwoLists(list1.next,list2))
        else:
            return ListNode(list2.val,self.mergeTwoLists(list1,list2.next))
