# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if list is empty or has only 1 node, it's already reversed
        if head is None or head.next is None:
            return head
        
        # Recursive case
        # 1. Reverse the rest of the list (This dives down to the end and comes back up)
        reversed_rest = self.reverseList(head.next)
        
        # 2. Make the next node point back to the current head
        head.next.next = head
        
        # 3. Make the current head point to None (break the old forward arrow)
        head.next = None
        
        # 4. Return the new head of the reversed list
        return reversed_rest