class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []

        for i in range(1, n + 1):
            divisibleBy3 = i % 3 == 0
            divisibleBy5 = i % 5 == 0

            currStr = ""

            if divisibleBy3:
                currStr += "Fizz"
            if divisibleBy5:
                currStr += "Buzz"
            if currStr == "":
                currStr += str(i)

            answer.append(currStr)
        
        return answer

    # time complexity: 0(n) to find each value in our output array
    # space complexity: 0(n) because we don't create any additional data structures
