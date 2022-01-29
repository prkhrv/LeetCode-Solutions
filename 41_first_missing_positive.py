class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        maximum = max(nums)
        if maximum <= 0:
            return 1
        num_set = set(nums)
        for i in range(1,maximum):
            if i not in num_set:
                return i
        return maximum+1
