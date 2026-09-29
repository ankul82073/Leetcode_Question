class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        visited = set()
        stack = [(0, 0, 0)]
        
        while stack:
            r, c, balance = stack.pop()
            
            balance += 1 if grid[r][c] == '(' else -1
            if balance < 0:
                continue
            
            if r == m - 1 and c == n - 1:
                if balance == 0:
                    return True
                continue
            
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n:
                    state = (nr, nc, balance)
                    if state not in visited:
                        visited.add(state)
                        stack.append(state)
                        
        return False