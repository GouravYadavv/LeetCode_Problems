class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        Rows, Col = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0
                or c < 0
                or r == Rows
                or c == Col
                or not grid[r][c]
                or (r, c) in visited
            ):
                return 0
            visited.add((r, c))
            res = 1
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            return res

        visited = set()
        land, BorderLand = 0, 0
        for r in range(Rows):
            for c in range(Col):
                land += grid[r][c]
                if (
                    grid[r][c]
                    and (r, c) not in visited
                    and (c in [0, Col - 1] or r in [0, Rows - 1])
                ):
                    BorderLand += dfs(r, c)
        return land - BorderLand