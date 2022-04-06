# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
class Solution:
    
    def binary_bad_version(left,right):
        if left <=right:
            mid  = left + (right-left) //2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1):
                return Solution.binary_bad_version(left,mid-1)
            elif not isBadVersion(mid) and not isBadVersion(mid-1):
                return Solution.binary_bad_version(mid+1,right)
        
        
        
        
    def firstBadVersion(self, n: int) -> int:
        # versions = [x for x in range(1,n+1)]
        left  = 0
        right = n
        return Solution.binary_bad_version(left,right)
