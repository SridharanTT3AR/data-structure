# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = []
        flag=0
        count=count1=0
        curnode = l1
        while(curnode.next):
            count+=1
            curnode = curnode.next
            
        curnode1 = l2
        while(curnode1.next):
            count1+=1
            curnode1 = curnode1.next
            
        if(count>count1):
            temp = count - count1
            
            for i in range(temp):
                curnode1.next = ListNode(0,None)
                curnode1 = curnode1.next
        else:
            temp = count1 - count
            
            for i in range(temp):
                curnode.next = ListNode(0,None)
                curnode = curnode.next
            
            
            
        while(l1):
            val = l1.val + l2.val + flag
            if(val>=10):
                val = val%10
                flag = 1
            else:
                flag = 0
            ans.append(val)
            l1 = l1.next
            l2 = l2.next
        i=0
        if(flag==1):
            ans.append(flag)
        node = self.insert(ans[0],ans)
        
                        
        return node
          
    def insert(self,root,ans):
        node = ListNode(root,None)
        head = node
        for i in range(1,len(ans)):
            temp = ListNode(ans[i],None)
            node.next = temp
            node = node.next
        return head
        
