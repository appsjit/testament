class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visitedSuccess = [False] * numCourses  ## For improvised Post DFS

        vertices = defaultdict(list)

        for i in prerequisites:
            course, depCourse = i[0], i[1]
            vertices[course].append(depCourse)
        lvl = 0
        courseWise = [False] * numCourses
        for course in range(numCourses):
            if self.isCyclic(course, vertices, courseWise, 0):
                return False
        print('Final ' + str(lvl))
        return True

    def isCyclic(self, pCourse, pVertices, pCourseWise, pLvl):
        # print("Before lvl:"+str(pLvl))
        pLvl += 1
        if pCourseWise[pCourse]:
            return True
        ## For improvised Post DFS
        if (self.visitedSuccess[pCourse]):  ## Succesfully checked so no Cycle
            return False
        ## Mark True to process Children
        pCourseWise[pCourse] = True
        res = False

        for child in pVertices[pCourse]:
            res = self.isCyclic(child, pVertices, pCourseWise, pLvl)
            if res:
                break
        ## After Backtracking set to False
        pCourseWise[pCourse] = False
        ##sp = '-'*pLvl
        ##print("After lvl:"+ sp +str(pLvl))
        self.visitedSuccess[pCourse] = True  ## For improvised Post DFS
        return res


