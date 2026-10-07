class Solution:
    def climbStairs(self, n: int) -> int:
        current, previous = 1, 1

        for i in range(1, n):
            current, previous = current + previous, current
            
        return current

    # time complexity: O(n) where n is the number of steps
    # space complexity: O(1) since we are using constant space to store the current and previous values
