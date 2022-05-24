class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        stack = [-1]
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            if s[i] == ")":
                stack.pop()
                if len(stack) > 0:
                    maxlen = max(maxlen,i - stack[-1])
            if len(stack) == 0:
                stack.append(i)
        
        return maxlen
