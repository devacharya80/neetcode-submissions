class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                if count > len(nums) // 3:
                    res.append(nums[i - 1])
                count = 1

        # Check last element's frequency
        if count > len(nums) // 3:
            res.append(nums[-1])

        return res