class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c_dict = Counter(nums)
        c_dict = dict(sorted(c_dict.items(), key=lambda item: item[1]))
        ans = []
        for key in c_dict:
            j = c_dict[key]
            for i in range(j):
                ans.append(key)
        return ans
        
