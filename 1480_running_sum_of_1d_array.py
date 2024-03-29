class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0]*n 
        dp[0] = nums[0]
        for i in range(1,n):
            dp[i] = dp[i-1]+nums[i]
        return dp
