class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def divide(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums) // 2

            left = divide(nums[:mid])
            right = divide(nums[mid:])

            return mergeSort(left,right)
        
        def mergeSort(left,right):
            res = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            
            while i < len(left):
                res.append(left[i])
                i += 1
            
            while j < len(right):
                res.append(right[j])
                j += 1
            
            return res
        
        return divide(nums)