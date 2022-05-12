class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = {0:0}
        for x in rods:
            for d, y in dp.copy().items():
                # init state 
                # ------|----- d -----|      # tall side 
                # - y --|                    # low  side

                # put x to tall side 
                # ------|----- d -----|---- x --|
                # - y --|
                dp[d+x] = max( dp.get(d+x, 0), y )

                # put x to low side 
                if d >= x:
                    # ------|----- d -----|
                    # - y --|---- x ---|
                    dp[d-x] = max( dp.get(d-x, 0), y+x)
                else:
                    # ------|----- d -----|
                    # - y --|-------- x --------|   
                    dp[x-d] = max(dp.get(x-d, 0), y+d)
        return dp[0]