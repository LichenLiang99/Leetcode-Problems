class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        waterCount = 0
        
        while l < r:
            
            #move left pointer
            if leftMax < rightMax:
                l += 1

                leftMax = max(leftMax, height[l])
                waterCount += leftMax - height[l]
                
            #move right pointer 
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                waterCount += rightMax - height[r]
                
        return waterCount