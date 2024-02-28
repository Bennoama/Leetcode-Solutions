# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        array = []
        while (head != None):
            array.append(head.val)
            head = head.next

        i = 0
        j = len(array) - 1
        maxSum = 0
        while (i < j):
            currSum = array[i] + array[j]
            maxSum = max(currSum, maxSum)
            i += 1
            j -= 1           
        
        return maxSum
