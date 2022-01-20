class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n ==1:
            return 1
        numbers = [None]*n
        numbers[0] = 1
        numbers[1] = 2
        
        for i in range(2,n):
            numbers[i] = numbers[i-1] + numbers[i-2]
        
        return numbers[n-1]
