class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #key: course value: list of prereqs it needs
        preqMap = {i:[] for i in range(numCourses)}
        
        #for cycle detection
        visited = set()
        cycle = set()
        
        #add all courses to preqMap
        for course, preq in prerequisites:
            preqMap[course].append(preq)
            
        res = []
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for preq in preqMap[course]:
                if not dfs(preq):
                    return False
            cycle.remove(course)
            
            visited.add(course)
            res.append(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
    
    #time o(E+V) space o(p+n)