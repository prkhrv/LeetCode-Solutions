class Solution:
        def jump(self, nums: List[int]) -> int:
            right = len(nums)-1
            left = 0
    
            jumps = 0
    
            while (left < right):
                leftJumpStrength = nums[left]
                newPositionIndex = leftJumpStrength + left
          
                if(newPositionIndex >= right):
                    jumps = jumps+1
                    right = left
                    left = 0
                else:
                    left = left+1
         
          

            return jumps

                
