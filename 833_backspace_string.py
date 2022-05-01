class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while "#" in s:
            i = s.index("#")
            if i > 0:
                s = s[:i-1] + s[i + 1:]
            else:
                s = s[i+1:]
        while "#" in t:
            j = t.index("#")
            if j > 0:
                t = t[:j-1] + t[j + 1:]
            else:
                t = t[j+1:]
        
        return s == t
