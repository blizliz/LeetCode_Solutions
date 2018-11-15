# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #two pointers solution
        if not head:
            return False
        
        ptr1 = head.next
        ptr2 = head.next
        
        if ptr2 == None:
            return False
        
        ptr2 = ptr2.next
        
        while ptr2 != None:
            if ptr1 == ptr2:
                return True
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if ptr2 != None:
                ptr2 = ptr2.next
                
        return False