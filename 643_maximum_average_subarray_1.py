class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window = n-k+1
        dp = [0] * window
        dp[0] = sum(nums[:k])
        ans = dp[0]/k
        dp_index = 1
        for i in range(k,n):
            dp[dp_index] = dp[dp_index-1] + nums[i] - nums[dp_index-1]
            avg = dp[dp_index] / k
            if avg > ans:
                ans = avg
            
            dp_index +=1

        return ans
        
