class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for el in s:
            if stack and stack[-1][0]==el:
                stack[-1][1]+=1
            else:
                stack.append([el,1])
            if stack and stack[-1][1]==k:
                stack.pop()
        return ''.join([el[0]*el[1] for el in stack])
