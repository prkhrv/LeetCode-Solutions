class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def split(left,right):  
            arr = nums[left:right]
            print(arr)
            size = len(arr)
            
            if size == 1:
                i = nums.index(arr[0])
                if target < arr[0]:
                    return i
                else:
                    return i+1
            if size == 2:
                if target > arr[1]:
                    return nums.index(arr[1]) + 1
                elif target > arr[0] and target < arr[1]:
                    return nums.index(arr[0]) + 1
                elif target < arr[0]:
                    return nums.index(arr[0])
            
            mid = size//2           
            
            print(left,right,mid)
            if arr[mid] > target:
                right = nums.index(arr[mid])
                return split(left,right)
            elif arr[mid] < target:
                left = nums.index(arr[mid])
                return split(left,right)
                
            
        
        try:
            index = nums.index(target)
        except:
            index = split(0,len(nums))
            print(index)
            
        
        return index
        
