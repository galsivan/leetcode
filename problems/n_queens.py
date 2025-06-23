# https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        occupied_cols = set()
        pos_diags = set()
        neg_diags = set()
        answer = []
        board = [["."] * n for row in range(n)]

        def backtrack(row):
            # Check if done
            if row == n:
                board_copy = ["".join(r) for r in board]
                answer.append(board_copy)
                return

            for col in range(n):
                if col in occupied_cols or \
                    (row - col) in pos_diags or \
                    (row + col) in neg_diags:
                    continue
                
                # place queen
                board[row][col] = "Q"
                occupied_cols.add(col)
                pos_diags.add(row - col)
                neg_diags.add(row + col)

                backtrack(row + 1)

                occupied_cols.remove(col)
                pos_diags.remove(row - col)
                neg_diags.remove(row + col)
                board[row][col] = "."
        
        backtrack(0)
        return answer
