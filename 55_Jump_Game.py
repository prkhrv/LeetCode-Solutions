class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        right = goal-1

        while right >= 0:
            #reachable
            if right + nums[right] >= goal:
                goal = right
                right = right - 1
            # not reachable
            else:
                right = right - 1
                
        return goal == 0

    

        
