class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map = Counter(nums)
        res = []
        
        for num,count in map.items():
            if count > len(nums) // 3:
                res.append(num)
        
        return res