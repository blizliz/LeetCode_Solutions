# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = tail = None
        rem = 0
        
        while l1 or l2:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rem
            rem = sum // 10
            
            if head == None:
                head = ListNode(sum % 10)
                tail = head
            else:
                tail.next = ListNode(sum % 10)
                tail = tail.next
                
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if rem == 1:
            tail.next = ListNode(rem)
            
        return head