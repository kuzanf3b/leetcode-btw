class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Brute Force approach: check all pairs of numbers to see if they add up to the target
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # time complexity: O(n^2) where n is the length of the input list nums
        # space complexity: O(1) since we are not using any additional data structures

        # Hash Map approach: use a hash map to store the numbers we have seen so far and their indices
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

        # time complexity: O(n) where n is the length of the input list nums
        # space complexity: O(n) since we are using a hash map to store the numbers and their indices
