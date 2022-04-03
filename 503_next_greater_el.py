class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        next_max = []
        
        l = 0
        r = len(nums)-1
        
        while l <= r:
            temp_arr = nums[l+1:]+nums[0:l]
            elm = nums[l]
            for elm in temp_arr:
                if elm > nums[l]:
                    next_max.append(elm)
                    break
            if elm <= nums[l]:
                next_max.append(-1)
                
            
            l+=1
            
        return next_max
            
        
