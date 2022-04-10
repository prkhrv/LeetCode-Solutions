class Solution:
    def binarySum(left,right,num):
        if left <= right:
            mid = left + (right-left)//2
            
            numx = mid-1
            numy = mid
            numz = mid+1
            
            if numx+numy+numz == num:
                return [numx,numy,numz]
            elif numx+numy+numz < num:
                return Solution.binarySum(mid+1,right,num)
            elif numx+numy+numz > num:
                return Solution.binarySum(left,mid-1,num)
        else:
            return []
        
    def sumOfThree(self, num: int) -> List[int]:        
        left = 0
        right = num
        return Solution.binarySum(left,right,num)
