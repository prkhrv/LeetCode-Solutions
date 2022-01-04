class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = True
        for br in s:
            if br == "(" or br =="[" or br == "{":
                stack.append(br)
            else:
                try:
                    if br == ")" and stack[-1] == "(":
                        stack.pop()
                        continue
                    elif br == "]" and stack[-1] == "[":
                        stack.pop()
                        continue
                    elif br == "}" and stack[-1] == "{":
                        stack.pop()
                        continue
                    else:
                        flag = False
                        break
                except:
                    flag = False
                    break
        if len(stack) > 0:
            flag = False
            
        return flag
