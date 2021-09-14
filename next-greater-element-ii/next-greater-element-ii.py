class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        
        #reverse nums to start the stack
        stack = nums[::-1]
        
        for i in range(n - 1, -1, -1):
            #if current num is greater than top of stack, pop until the value in stack is greater than our num
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            #after poping, if stack still not empty, then top of stack is the next greater value
            if stack:
                res[i] = stack[-1]
            #add current number to stack
            stack.append(nums[i])
        
        return res
        
        #time o(n) space o(n) concept stack
        
        