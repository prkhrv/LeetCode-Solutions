class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        return str(Solution.convertToNumber(num1)* Solution.convertToNumber(num2))
    
    
    def convertToNumber(num_str):
        value_dict = {
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0
        }
    
        digit = len(num_str) - 1
        number = 0
        i = 0
    
        while(digit >= 0):
            number = number + (value_dict[num_str[digit]] * (10**i))
            digit = digit - 1
            i = i+1
    
        return number
