class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #key: course value: list of prereqs it needs
        preqMap = {i:[] for i in range(numCourses)}
        
        #for cycle detection
        visited = set()
        
        #add all courses to preqMap
        for course, preq in prerequisites:
            preqMap[course].append(preq)
        
        
        def dfs(course):
            #if already visied, there is cycle
            if course in visited:
                return False
            
            #doesn't need prereq or achivable already
            if preqMap[course] == []:
                return True
            
            #add course to visited
            visited.add(course)
            
            #for every prereq for this course, if pre is not achievable, return false
            for pre in preqMap[course]:
                if not dfs(pre):
                    return False
                
            #if returned true, we know prereq is achievable and course is achievable
            #remove course from visited and preq from preqMap
            visited.remove(course)
            preqMap[course] = []
            return True
        
        #need to go through each course because their might be disconnected graph
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
    
    #time o(n) space o(n)
            