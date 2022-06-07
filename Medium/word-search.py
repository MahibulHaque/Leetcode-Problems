class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, pos):
            if pos == len(word):
                return True
            if (min(r, c) < 0 or r >= rows or c >= cols or
                word[pos] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, pos + 1) or
                   dfs(r - 1, c, pos + 1) or
                   dfs(r, c + 1, pos + 1) or
                   dfs(r, c - 1, pos + 1))
            path.remove((r, c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0): return True
        return False    