class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def is_inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid)

        if grid[0][0] != 0:
            return -1

        visited = set()
        visited.add((0, 0))

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

        level = 0
        queue = deque([(0, 0)])

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()
                if (row, col) == (len(grid) - 1, len(grid) - 1):
                    return level + 1

                for i, j in directions:
                    new_row, new_col = row + i, col + j
                    if is_inbound(new_row, new_col) and (new_row, new_col) not in visited and grid[new_row][new_col] == 0:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            level += 1

        return -1
