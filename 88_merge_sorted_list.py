class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:len(nums1)]
        del nums2[n:len(nums2)]
        
        nums1.extend(nums2)
        nums1.sort()
        
