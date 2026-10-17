class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

    # time complexity: O(2^n) exponential time complexity due to the recursive calls
    # space complexity: O(n) due to the call stack of the recursion
