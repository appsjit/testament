class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.visitedSuccess = [False] * numCourses  ## For improvised Post DFS

        vertices = defaultdict(list)
        indegree = {}
        for i in prerequisites:
            course, depCourse = i[0], i[1]
            vertices[depCourse].append(course)
            # Record each node's in-degree
            indegree[course] = indegree.get(course, 0) + 1
        # myQu = []
        # for i in range(numCourses):
        #     if i not in vertices:
        #         myQu.append(i)

        # starterCourseQue = [x for x in range(numCourses) if x not in vertices]
        starterCourseQue = [x for x in range(numCourses) if x not in indegree]
        print(indegree)

        topological_sorted_order = []

        while len(starterCourseQue) > 0:
            prcCourse = starterCourseQue.pop()
            print(prcCourse)
            topological_sorted_order.append(prcCourse)

            if prcCourse in vertices:
                for depCourse in vertices[prcCourse]:
                    indegree[depCourse] -= 1
                    if indegree[depCourse] == 0:
                        starterCourseQue.append(depCourse)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []

