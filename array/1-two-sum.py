class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        # time complexity: O(n^2) where n is the length of the input list nums
        # space complexity: O(1) since we are not using any additional data structures
