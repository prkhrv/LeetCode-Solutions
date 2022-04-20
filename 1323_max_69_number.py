class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        if str_num.count("9") == len(str_num):
            return num
        str_num = str_num.replace("6","9",1)
        
        return int(str_num)
            
