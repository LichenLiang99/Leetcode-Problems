class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx <= tx and sy <= ty:
            if tx == ty:
                break
            #update ty
            elif tx < ty:
                if sx < tx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
            #update tx
            else:
                if sy < ty:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
        
        return sx == tx and sy == ty