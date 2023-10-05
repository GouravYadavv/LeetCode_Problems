# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list2 is None and list1 is None:
            return None
        if list1.val > list2.val:
            list1, list2 = list2, list1
        head = list1
        while list1.next:
            if list1.next.val > list2.val:
                list1.next, list2 = list2, list1.next
            list1 = list1.next
        list1.next = list2
        return head