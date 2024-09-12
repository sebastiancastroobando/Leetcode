# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        solutionList = ListNode()
        solutionListHead = solutionList;
        while (True):
            if (l1):
                sum += l1.val
                l1 = l1.next
            if (l2):
                sum += l2.val
                l2 = l2.next
            
            remainder = sum % 10
            carry = 1 if sum > 9 else 0
            solutionList.val = remainder 
            if (l1 or l2 or carry):
                solutionList.next = ListNode()
                solutionList = solutionList.next
                sum = carry
            else:
                break

        return solutionListHead