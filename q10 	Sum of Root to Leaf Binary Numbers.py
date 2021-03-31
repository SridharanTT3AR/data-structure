class Solution(object):
    def __init__(self):
        self.ans = 0    
        
    
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result(root,"")
        return int(self.ans)
    def result(self,root,value):
        
        if not root.left and not root.right:
            value+=str(root.val)
            self.binary_to_decimal(value)
            return
        if root.left:
            #value+=str(root.val)
            self.result(root.left,value+str(root.val))
        if root.right:
            #value+=str(root.val)
            self.result(root.right,value+str(root.val))
        
    def binary_to_decimal(self,value):
        j=0
        for i in range(len(value)-1,-1,-1):
            val = int(value[i:i+1])
            self.ans+= math.pow(2,j)*val
            j+=1
        print(self.ans)
