class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        index = 0
        init_sum = nums[index]
        sum = init_sum
        
        for i in range(1,len(nums)):
            if nums[i] > (init_sum+nums[i]):
                init_sum = nums[i]
            else:
                init_sum = init_sum+nums[i]
            
            if init_sum > sum:
                sum = init_sum
        return sum
