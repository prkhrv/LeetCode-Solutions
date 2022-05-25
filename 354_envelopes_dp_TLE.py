class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        N = len(envelopes)
        if N == 0:
            return 0
        
        envelopes.sort(key=lambda x:x[0])
        dp = [1]*N
        max_so_far = 1
        
        for i in range(1,N):
            for j in range(i):
                if (envelopes[j][0] < envelopes[i][0]) and (envelopes[j][1] < envelopes[i][1]):
                    dp[i] = max(dp[i], dp[j]+1)
            max_so_far = max(max_so_far, dp[i])
        return max_so_far
      
            
            
            
