# DFS-based Maze Solver

def find_path(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    path = []
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(x, y):
        if not (0 <= x < rows and 0 <= y < cols) or maze[x][y] == 1 or visited[x][y]:
            return False
        
        path.append((x, y))
        visited[x][y] = True
        
        # If we reached the end, return True
        if (x, y) == end:
            return True

        # Move in 4 possible directions (up, down, left, right)
        if dfs(x+1, y) or dfs(x-1, y) or dfs(x, y+1) or dfs(x, y-1):
            return True

        # Backtrack
        path.pop()
        return False

    if dfs(start[0], start[1]):
        return path
    else:
        return None

# Example Maze (0 = path, 1 = wall)
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
end = (4, 4)

path = find_path(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found.")
