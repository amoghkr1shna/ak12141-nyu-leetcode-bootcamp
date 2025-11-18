# from collections import deque, defaultdict
# from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        # Building graph and indegree
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # Starting with all courses that don't have prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []
        
        while queue:
            cur = queue.popleft()
            order.append(cur)
            
            # Reducing indegree of the neighbors 
            for nxt in graph[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        
        return order if len(order) == numCourses else []
