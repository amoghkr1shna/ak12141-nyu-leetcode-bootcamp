# from collections import deque
# from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        q = deque()      #stores r, c, and time
        fresh = 0        # count of fresh oranges
        
        # Initializing q with all rotten oranges and counting fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))   # rotten orange at time 0
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 4-directional
        
        # 2. BFS: spread rotting layer by layer
        while q:
            r, c, t = q.popleft()
            minutes = max(minutes, t)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # Check bounds and if it's a fresh orange
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2        # it becomes rotten
                    fresh -= 1
                    q.append((nr, nc, t + 1))
        
        # 3. If there are still fresh oranges, it's impossible
        return minutes if fresh == 0 else -1
