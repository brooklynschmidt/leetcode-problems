from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])
        queue = deque()

        for i in range(row_len):
            for j in range(col_len):
                if mat[i][j] == 0:
                    queue.append([i, j, 0])
                else:
                    mat[i][j] = float('-inf')

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:
            current = queue.popleft()
            i, j, dist = current[0], current[1], current[2]
            
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]

                if (0 <= new_i < row_len and 0 <= new_j < col_len and mat[new_i][new_j] < 0):
                    mat[new_i][new_j] = dist + 1
                    queue.append([new_i, new_j, dist + 1])
        
        return mat
        
