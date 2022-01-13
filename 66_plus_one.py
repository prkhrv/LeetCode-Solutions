class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        test = "".join(str(x) for x in digits)
        num = str(int(test)+1)
        return [int(x) for x in str(num)]
'''
Runtime: 28 ms, faster than 90.91% of Python3 online submissions for Plus One.
Memory Usage: 14.3 MB, less than 14.07% of Python3 online submissions for Plus One.
'''
