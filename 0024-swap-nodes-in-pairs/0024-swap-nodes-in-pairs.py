# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head

        while slow and slow.next:
            slow.val,slow.next.val=slow.next.val,slow.val

            slow=slow.next.next
        
        return head