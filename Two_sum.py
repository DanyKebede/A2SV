class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        result = []
        for i in range(len(nums)):
            for x in range(i+1, len(nums)):
                sum = nums[i] + nums[x]
                if sum == target:
                    result.append(i)
                    result.append(x)
                    break
        return result