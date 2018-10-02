# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        tail = None
        val = 0
        
        while l1 or l2:
            if l1 and l2:
                if l1.val <= l2.val:
                    val = l1.val
                    l1 = l1.next
                else:
                    val = l2.val
                    l2 = l2.next
            elif l1:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            if not head:
                head = ListNode(val)
                tail = head
            else:
                tail.next = ListNode(val)
                tail = tail.next
                    
        return head
                
        