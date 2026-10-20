from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        row_len = len(grid)
        col_len = len(grid[0])

        queue = deque()

        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == "1":
                    islands += 1
                    # Sink it
                    grid[i][j] = 0
                    queue.append([i, j])

                    while queue:
                        current = queue.popleft()
                        r, c = current[0], current[1]
                        for d in directions: 
                            new_r = r + d[0]
                            new_c = c + d[1]

                            if (0 <= new_r < row_len and 0 <= new_c < col_len and grid[new_r][new_c] == "1"):
                                # Sink it
                                grid[new_r][new_c] = "0"
                                queue.append([new_r, new_c])
                        
        return islands
