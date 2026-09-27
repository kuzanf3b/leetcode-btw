class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1

            steps += 1

        return steps

    # time complexity: O(log n), because we divide by 2 or subtract 1 in each step
    # space complexity: O(1), because we only use a constant amount of space