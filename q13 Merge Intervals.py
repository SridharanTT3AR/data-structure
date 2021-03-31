class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if(len(intervals)==1):
            return intervals
        
        
        intervals = sorted(intervals,key = lambda k:k[0])
        n = len(intervals)
        i=0
        print(intervals)
        while(i<n-1):
            if(intervals[i][1]>=intervals[i+1][0]):
                intervals[i][1]=max(intervals[i+1][1],intervals[i][1])
                del(intervals[i+1])
                n-=1
                i-=1
            i+=1
        print(intervals)
        return intervals
