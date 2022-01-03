class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        def checktrustedbyall(judge,n,trusted):
            t = trusted.count(judge)
            
            if t == n-1:
                return True
            else:
                return False
            
        labels = list(range(1,n+1))
        trusted = []
        for arr in trust:
            a = arr[0]
            b = arr[1]
            
            if a in labels:
                labels.remove(a)
            
            trusted.append(b)
        
        if len(labels) == 1:
            judge = labels[0]
            
            trust = checktrustedbyall(judge,n,trusted)
            
            if trust:
                return judge
            else:
                return -1
        else:
            return -1
        
