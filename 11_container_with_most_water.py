class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height)-1
        
        max_height = max(height)
        
        
        while right > left and max_height * (right - left) > water:
            area = (right - left) * min(height[right], height[left])
        
            # we are looking for a couple of heighest bars moving from lower bar to the next one
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            
            water = max(water, area)
        
        return water
        
