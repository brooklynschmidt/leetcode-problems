from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Store start color
        start_color = image[sr][sc]

        # Bounds
        row_len = len(image)
        col_len = len(image[0])

        # Start worklist & visited list
        visited = set([(sr, sc)])
        worklist = deque()
        worklist.append([sr, sc])

        # Directions
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # BFS
        while worklist:
            # We get the top node from our worklist
            current = worklist.popleft()
            r, c = current[0], current[1]
            if image[r][c] == start_color:
                image[r][c] = color

                for d in directions:
                    new_r = r + d[0]
                    new_c = c + d[1]
                    # bounds check
                    if (0 <= new_r < row_len and 0 <= new_c < col_len and (new_r, new_c) not in visited):
                        worklist.append([new_r, new_c])
                        visited.add((new_r, new_c))

        return image
