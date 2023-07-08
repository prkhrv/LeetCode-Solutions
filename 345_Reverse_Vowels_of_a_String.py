class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s)-1

        s_list = list(s)

        vowels = ['a','e','i','o','u','A','E','I','O','U']

        while left < right:
            if s_list[left] in vowels:
                if s_list[right] in vowels:
                    s_list[left],s_list[right] = s_list[right],s_list[left]

                    left+=1
                    right-=1
                else:
                    right -=1 
            else:
                left +=1
        return "".join(s_list)

