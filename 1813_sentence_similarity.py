class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split(" ")
        b = sentence2.split(" ")
        
        if len(a)>len(b):
            a,b=b,a
        
        if len(a)==len(b):
            return a==b
        
        i = 0
        while i < len(a) and a[i] == b[i]:
            i+=1
        
        j=1
        while j <=len(a) and a[-j] == b[-j]:
            j+=1
        
        return len(a)==i+j-1 or i>len(a) or j>len(a)
