class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        s_count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse=True)}
        ans = ""
        
        for key in s_count.keys():
            ans += key*s_count[key]
        return ans
        
