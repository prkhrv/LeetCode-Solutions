class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        freq_dict = Counter(nums)
        ans = []
        
        for key in freq_dict.keys():
            if freq_dict[key] == 1 and key+1 not in freq_dict and key-1 not in freq_dict:
                ans.append(key)
        return ans
                
