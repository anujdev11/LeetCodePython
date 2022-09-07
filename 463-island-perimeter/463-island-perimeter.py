class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        
        rows = len(grid)
        cols = len(grid[0])
        
        perimeter = [0]
        
        visited = set()
        
        
        
        def bfs(r,c):
            queue = deque()
            visited.add((r,c))
            queue.append((r,c))
    
            while queue:
                dr,dc = queue.popleft()
                posibilities = [(1,0),(-1,0),(0,1),(0,-1)]
                
                for row,column in posibilities:
                    r,c=dr+row,dc+column
                    
                    if (r<0 or r > rows-1 or c<0 or c > cols-1):
                        perimeter[0]+=1
                    
                    elif(grid[r][c] == 0):
                        perimeter[0]+=1
                    
                    elif(grid[r][c] == 1 and (r,c) not in visited):
                        visited.add((r,c))
                        queue.append((r,c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
                    return perimeter[0]
        