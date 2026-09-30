class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineLetters = {} # k = 26

        for i in range(len(magazine)):
            m = magazine[i]

            currentCount = magazineLetters.get(m, 0)
            magazineLetters[m] = currentCount + 1
        
        # bounded by m
        for i in range(len(ransomNote)):
            r = ransomNote[i]

            currentCount = magazineLetters.get(r, 0)

            if currentCount == 0:
                return False
            
            magazineLetters[r] = currentCount - 1

        return True

    # time complexity: O(m + n) where m is the length of magazine and n is the length of ransomNote
    # space complexity: O(k) where k is the number of unique letters in magazine (at most 26 for lowercase letters)
