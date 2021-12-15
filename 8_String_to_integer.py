import math

class Solution:
    def myAtoi(self, s: str) -> int:
        
        num = ""
        coeff = 1
        flag = False
        for char in s:
            if char == " " and flag ==False:
                continue
            elif char == "-" and flag == False:
                flag = True
                coeff = -1
            elif char == "+" and flag == False:
                flag = True
                continue
            elif not char.isdigit():
                if len(num) == 0:
                    return 0
                else:
                    if -1*(2**31) <= int(num) <= (2**31)-1:
                        return coeff*int(num)
                    else:
                        if coeff == 1:
                            return (coeff*(2**31))-1
                        else:
                            return (coeff*(2**31))
            else:
                flag = True
                num = num+char
        
        if len(num) == 0:
            return 0
        else:
            if -1*(2**31) <= int(num) <= (2**31)-1:
                return coeff*int(num)
            else:
                if coeff == 1:
                    return (coeff*(2**31))-1
                else:
                    return (coeff*(2**31))
                    

                
        
        
            
                
        
