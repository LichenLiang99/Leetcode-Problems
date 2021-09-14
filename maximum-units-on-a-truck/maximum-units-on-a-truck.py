class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        box = []
        unit = []
        for b, u in boxTypes:
            box.append(b)
            unit.append(u)
        
        arr = zip(box, unit)
        arr = list(arr)
        
        
        arr.sort(key = lambda x:x[1], reverse = True)
        
        boxRemain = truckSize
        total = 0
        for numboxes, units in arr:
            if boxRemain <= numboxes:
                total += boxRemain * units
                break
            else:
                total += numboxes * units
                boxRemain -= numboxes
            
        return total
            