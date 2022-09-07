class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        
        rows,cols = len(grid),len(grid[0])
        
        noOfIslands = 0
        
        visited = set()
        
        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
            
            while queue:
                posibilities = [(1,0),(-1,0),(0,1),(0,-1)]
                dr,dc = queue.popleft()
                
                for row,column in posibilities:
                    r,c = dr+row,dc+column
                        
                    if(r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited):
                        visited.add((r,c))
                        queue.append((r,c))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited: 
                    bfs(r,c)
                    noOfIslands+=1
                    
        return noOfIslands