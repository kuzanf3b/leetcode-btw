class Solution:
    def trap(self, height: list[int]) -> int:
        maxL = 0
        maxR = 0
        bodyWaterCount = 0

        l = 0
        r = len(height) - 1

        while l < r:
            if height[l] < height[r]:
                if height[l] > maxL:
                    maxL= height[l]
                else:
                    bodyWaterCount += maxL - height[l]
                l += 1

            else:
                if height[r] > maxR:
                    maxR= height[r]
                else:
                    bodyWaterCount += maxR - height[r]
                r -= 1
        
        return bodyWaterCount
