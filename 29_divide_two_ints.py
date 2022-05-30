class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        self.min = -2147483648
        
        # python doesn't have any real concept of this but the overflow of the min and a negative is the max
        # some languages handle this, some do not.
        if dividend == self.min and divisor == -1:
            return 2147483647
        
        # we store the sign so we can return the proper number in the end
        # since we're working entirely in negatives (see bloe)
        sign = (dividend < 0) == (divisor < 0)
        
        # we need to work in negatives because abs will not work for min_int
        # eg: abs(-2147483648) is out of the range of 2147483647 - -2147483648
        # to avoid this we work entirely in negatives
        if dividend > 0:
            dividend = -dividend
        
        if divisor > 0:
            divisor = -divisor
        
        res = self.divide_helper(dividend, divisor)
        
        return res if sign else -res
        
        
    def divide_helper(self, dividend, divisor):
        # edge case so we don't divide a smaller number by a larger one
        if divisor < dividend:
            return 0
        
        quotient = 1
        sums = divisor
        
        # python doesn't have fixed int numbers so we ensure we don't bottom out
        # since we're working in negatives, we need to make sure our sums of negatives will not overflow
        # eg: self.min = -20 , sums = -11, -11 + -11 = -22 which overflows
        while (sums + sums > self.min) and (sums + sums > dividend):
            sums +=  sums
            quotient += quotient
        
        # now that we've found the quotient for this number, find the next divisible part
        return quotient + self.divide_helper(dividend - sums, divisor)
        
