class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rowLen = len(board)
        colLen = len(board[0])
        ans = False

        def backTrack(pRow, pCol, remWord):
            flag = False
            # bottom case: we find match for each letter in the word
            if len(remWord) == 0:
                return True

            # Check the current status, before jumping into backtracking
            if pRow < 0 or pRow == rowLen or pCol < 0 or pCol == colLen or board[pRow][pCol] != remWord[0]:
                return False


            ## Mark Visited #
            board[pRow][pCol] = '#'

            for (rowExplore, colExplore) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = pRow + rowExplore, pCol + colExplore
                flag = backTrack(newRow, newCol, remWord[1:])

                if flag:
                    break

            # End of EXPLORATION, we restore the cell
            board[pRow][pCol] = remWord[0]

            return flag

        for r in range(rowLen):
            for c in range(colLen):
                if backTrack(r, c, word):
                    return True

        return ans