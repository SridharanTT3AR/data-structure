# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        curnode = head
        l = 0
        while(curnode):
            l+=1
            curnode = curnode.next
        curnode = head
        for i in range(1,k):
            curnode = curnode.next
        secondnode = head
        for i in range(l-k):
            secondnode = secondnode.next
        
        curnode.val,secondnode.val = secondnode.val,curnode.val
        return head
        
