class Solution:
    
    def create_ans(ans,del_arr,k):
        f_ans = ""
        
        i = 0
        while(i < len(ans)):
            if i in del_arr:
                i = i+k
            
            if i < len(ans):
                f_ans = f_ans+ans[i]
            else:
                break
                
            i = i+1
                
        
        return f_ans
        
        
    
    def to_delete(s,k):
        to_del = []
        for i in range(0,len(s)-1):
            curr_ch = s[i]
            flag = 0 
            if (i+k) <= len(s):
                for j in range(i,i+k):
                    if s[j] == curr_ch:
                        flag = flag + 1
                    else:
                        break
                    
            if flag == k:
                to_del.append(i)
        
        return to_del
                 
        
    def removeDuplicates(self, s: str, k: int) -> str:
        control = 1
        ans = s
        while(control):
            to_del = Solution.to_delete(ans,k)
            control = len(to_del)
            if control > 0:
                ans = Solution.create_ans(ans,to_del,k)
        
        return ans
        
                 
                
                
        
