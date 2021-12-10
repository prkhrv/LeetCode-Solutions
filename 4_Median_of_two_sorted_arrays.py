class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1+nums2
        arr.sort()
        if len(arr) % 2 == 0 :
            index = len(arr)//2
            median = (arr[index]+arr[index-1])/2
            
        else:
            index = len(arr)//2
            median = float(arr[index])
        return median
