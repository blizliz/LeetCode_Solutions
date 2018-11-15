# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        
        size = 0
        tail = head
        
        while tail != None:
            size += 1
            tail = tail.next
        
        if size < 2:
            return True
        
        i = 0
        tail = tmp = None
        while i < size // 2:
            tmp = head
            head = head.next
            tmp.next = tail
            tail = tmp
            i += 1
        
        ptr1 = tail
        if size % 2 == 0:
            ptr2 = head
        else:
            ptr2 = head.next
            
        while ptr1 != None:
            if ptr1.val != ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        return True