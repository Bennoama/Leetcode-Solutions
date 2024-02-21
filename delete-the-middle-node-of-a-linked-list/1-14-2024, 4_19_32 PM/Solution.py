// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        curr = head
        while (curr):
            curr = curr.next
            size += 1
        
        if (None == head.next):
            return None

        curr = head
        prev = None
        nex = None
        index = 0
        while (curr):
            if (index == size // 2):
                if (prev):
                    prev.next = curr.next
                    return head
            nex = curr.next
            prev = curr
            curr = nex
            index += 1

        return head