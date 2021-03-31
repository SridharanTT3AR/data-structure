# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        queue = []
        flag = False
        
        queue.append(root)
        
        while(queue):
            curnode = queue.pop(0)
            if(curnode.left):
                if flag == True:
                    return False
                queue.append(curnode.left)
            else:
                flag = True    #says that there no child
            if(curnode.right):
                if flag == True:
                    return False
                queue.append(curnode.right)
            else:
                flag = True
        return flag
