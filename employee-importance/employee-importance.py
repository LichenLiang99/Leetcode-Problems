"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def helper(id):
            res = mapp[id]
            for s in sub[id]:
                res += helper(s)
            return res
        
        mapp = {}
        sub = {}
        for e in employees:
            mapp[e.id] = e.importance
            sub[e.id] = e.subordinates
        
        return helper(id)