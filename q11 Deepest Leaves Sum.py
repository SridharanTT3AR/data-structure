# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deep = self.deepleaf(root)
        print("deep",deep)
        #ans = 0
        result = self.answer(root,1,deep)
        return result
        
    def deepleaf(self,root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return max(1+self.deepleaf(root.left),1+self.deepleaf(root.right))
        
    def answer(self,root,height,deep):
        if not root:
            return 0
        ans = 0
        if not root.left and not root.right:
            if height == deep:
                return root.val
            
            
        ans = ans + self.answer(root.left,1+height,deep)
        ans = ans + self.answer(root.right,1+height,deep)  
        return ans
