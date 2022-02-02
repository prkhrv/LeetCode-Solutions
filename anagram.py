class Solution:
    
    def findOccurrences(s, ch):
        return [i for i, letter in enumerate(s) if letter == ch]
    
    def check_pattern(pat,p):
        flag = False
        positions = []
    
        for i in range(0,len(p)):
            pos1 = Solution.findOccurrences(pat,p[i])
            pos2 = Solution.findOccurrences(p,p[i])
        
            if len(pos1) == len(pos2):
                flag = True
            else:
                flag = False
                break
    
        return flag
        
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = len(p)
        
        answer = []
        
        left = 0
        right = window
        
        while(right<=len(s)):
            pattern = s[left:right]
            flag = Solution.check_pattern(pattern,p)
            
            if flag:
                answer.append(left)
            
            left = left+1
            right = right +1
        
        return answer
        
