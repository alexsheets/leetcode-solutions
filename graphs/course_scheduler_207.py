# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

#----------------------------------------------------------------------------------------------------------------

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        in_deg = defaultdict(set)
        out_deg = defaultdict(set)
        courses_taken = 0
        queue = []

        # get indeg and outdeg for each course
        for course, requires in prerequisites:
            in_deg[course].add(requires)
            out_deg[requires].add(course)

        # init queue with courses which have in degree 0
        for i in range(numCourses):
            if len(in_deg[i]) == 0:
                queue.append(i)
            
        while len(queue) > 0:    
            # remove from queue and add to topo order (here use counter)
            course = queue.pop(0)
            courses_taken += 1

            # reduce indeg for neighbors
            for neighbor in out_deg[course]:
                in_deg[neighbor].remove(course)

                # re look: add neighbors to queues who now have indeg 0
                if len(in_deg[neighbor]) == 0:
                    queue.append(neighbor)

        return courses_taken == numCourses
    

# EXPLANATION AND COMPLEXITY: 
# uses at most O(V+E) time complexity to visit each vertex and edge at most once (grows linearly). i had studied topological graphs earlier today so this was a great application of the algorithm.
# essentially, this problem is asking if there is a cycle in the graph. if so, we do not have a topological sorting, and thus cannot take all the courses.