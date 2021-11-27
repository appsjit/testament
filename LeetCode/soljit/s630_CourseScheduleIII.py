import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        ## Sort by course end date
        courses = sorted(courses, key=lambda x: x[1])
        ##print(courses)

        course_plan = []  ## Plan to take courses
        time_spent = 0
        for start, end in courses:
            ##if course duration + time spent till now less than end date for course
            if time_spent + start <= end:
                # print(start)
                ## Min heap of course plan will maintain course duration with maximum length after multiplying by -1
                heapq.heappush(course_plan, -start)
                time_spent += start
                ##print(course_plan)
            else:
                ## if any later occurence of course with same or higher end date having smaller duration can be prioritized
                if course_plan and start < -1 * course_plan[0]:
                    time_spent -= -1 * heapq.heappop(
                        course_plan)  ## remove longest duration course to replace with smaller duration course to accomodate more courses
                    time_spent += start
                    heapq.heappush(course_plan, -start)

        return len(course_plan)
