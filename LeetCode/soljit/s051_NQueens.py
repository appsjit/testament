class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def create_board(state):
            board = []
            for row in state:
                board.append("".join(row))
            return board

        def validate(pBoard, pRow, pCol):
            for i in range(n):
                j = 0
                while (j < pCol):
                    if (pBoard[i][j] == 'Q' and
                            (pRow + j == pCol + i or  ## Diagonal
                             pRow + pCol == i + j or
                             pRow == i)):  ## Not in same Row
                        return False
                    j += 1
            return True

        def dfs(pBoard, pCol, pLvl):
            if (pCol == n):
                print('Hit')
                res.append(create_board(pBoard))
                return

            ## Iterate over Row to check where to keep Q on row
            for i in range(n):
                print(' ' * pLvl + 'Validating row idx :' + str(i) + '  col idx:' + str(pCol) + '   result :' + str(
                    validate(pBoard, i, pCol)))
                if validate(pBoard, i, pCol):
                    pBoard[i][pCol] = 'Q'  ## Choice
                    print('Q is at row idx :' + str(i) + '  col idx:' + str(pCol))
                    dfs(pBoard, pCol + 1, pLvl + 1)  # Recurse
                    pBoard[i][pCol] = '.'  ## Revert to backtrack

        res = []
        emptyBoard = [["."] * n for _ in range(n)]
        dfs(emptyBoard, 0, 0)

        return res

