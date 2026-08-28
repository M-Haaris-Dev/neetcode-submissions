class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen =set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val ==".":
                    continue 
                ri = f"row{r} has {val}"
                ci = f"col{c} has {val}"
                bi = f"box{r//3},{c//3} has {val}"
                if ri in seen or ci in seen or bi in seen:
                    return False
                seen.add(ri)
                seen.add(ci)
                seen.add(bi)
        return True
                    