import math

class Solution(object):
    def bestCoordinate(self, towers, radius):
        """
        :type towers: List[List[int]]
        :type radius: int
        :rtype: List[int]
        """
        xmin,xmax = min([t[0] for t in towers]), max([t[0] for t in towers])
        ymin,ymax = min([t[1] for t in towers]), max([t[1] for t in towers])
        m=0
        res=[0,0]
        for x in range(xmin,xmax+1):
            for y in range(ymin,ymax+1):
                curr=0
                for xt,yt,q in towers:
                    d=sqrt((x-xt)**2+(y-yt)**2)
                    if d<=radius+0.01:
                        curr+=math.floor(q / (1+d))
                if curr>m:
                    res=[x,y]
                    m=curr
        return res
