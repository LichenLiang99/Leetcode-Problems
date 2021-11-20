class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        i = 0
        for n in pushed:
            st.append(n)
            while st and st[-1] == popped[i]:
                i += 1
                st.pop()
        
        if st:
            return False
        else:
            return True