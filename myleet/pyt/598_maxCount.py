class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops)==0:
            return 0
            
        ix=ops[0][0]
        iy=ops[0][1]
        
        for item in ops:
            if item[0]<ix:
                ix=item[0]
            if item[1]<iy:
                iy=item[1]
        print(ix,iy,ix*iy)
        return ix*iy

case1=3,3,[[2,2],[3,3]]
case2=3,3,[]
Solution().maxCount(3,3,[])
