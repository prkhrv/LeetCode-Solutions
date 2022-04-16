class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        ans = 0
        num_sum = sum(nums)
        
        if num_sum == goal:
            return ans
        else:
            diff = goal - num_sum
            if abs(diff) % limit == 0:
                return abs(diff)// limit
            else:
                return abs(diff)// limit +1
                
