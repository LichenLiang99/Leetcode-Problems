class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        #start facing up, from origin
        dirX, dirY = 0, 1
        x, y = 0, 0
        
        #left:(-1,0), up(0,1), down(0,-1), right(1,0)
        for i in instructions:
            if i == "G":
                x, y = x + dirX, y + dirY
            elif i == "L":
                dirX, dirY = -1 * dirY, dirX
            else:
                dirX, dirY = dirY, -1 * dirX
        
        #if location at origin, OR direction is changing(different from start direction)
        return (x, y) == (0, 0) or (dirX, dirY) != (0, 1)