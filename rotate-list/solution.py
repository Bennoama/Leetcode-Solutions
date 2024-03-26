# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        curr = head
        while (curr):
            values.append(curr.val)
            curr = curr.next
        curr = head
        for i in range(len(values)):
            curr.val = values[(i - k) % len(values)]
            curr = curr.next
        return head
