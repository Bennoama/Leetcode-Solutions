# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while (l1 or l2):
            if l1:
                num1.append(l1.val)
                l1 = l1.next
            if l2:
                num2.append(l2.val)
                l2 = l2.next
        for i in range(0, len(num2) - len(num1)):
            num1.insert(0, 0)
        for i in range(0, len(num1) - len(num2)):
            num2.insert(0, 0)

        num3 = [0] * len(num1)
        addOne = 0
        for i in range(len(num1) - 1, -1, -1):
            num3[i] = (num2[i] + num1[i] + addOne) % 10
            addOne = (num2[i] + num1[i] + addOne) // 10

        if addOne:
            num3.insert(0,1)
        head = ListNode(num3[0])
        runner = head
        for i in range(0, len(num3) - 1):
            runner.val = num3[i]
            runner.next = ListNode(num3[i + 1])
            runner = runner.next
        
        print(num3)
        
        return head
        
