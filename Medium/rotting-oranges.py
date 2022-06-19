class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
                
        '''
        SIMULTANOUS BFS FLOODING
        
            - push all rotten oranges to a queue
            - run simultanous BFS on queue
            - minutes = num of iterations
            
            - as you BFS, if a new fresh orange found -> mutate to rotten and add to q
            
        TIME:
            O(N) where N is the number of cells (nested for loop over a matrix)
            O(N^2) only if the nested for loop is running over a one dimensaional DS or array
        SPACE:
            O(M) where M is the max rotten oranges that can be held in the queue
        '''
		
		
        if not grid:
            return -1
        
        from collections import deque
        q = deque()
        
        fresh = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # if no fresh or no rotten -> -1
        if not fresh:
            return 0
        if len(q) == 0:
            return -1
        
        # run simaltanous flood fill style BFS
        minutes = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        while q and fresh: # -- NOTE [1]
            for i in range(len(q)):
                node = q.popleft()
                x, y = node
                
                for dir in dirs:
                    newX, newY = x+dir[0], y+dir[1]
                    if newX >= 0 and newX <= len(grid)-1 and newY >= 0 and newY <= len(grid[0])-1:
                            if grid[newX][newY] == 1: # fresh
                                grid[newX][newY] = 2 # make rotten
                                fresh -= 1
                                q.append((newX, newY))
            minutes += 1
        if not fresh:
            
            return minutes
        return -1