class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        trie = {}

        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node[WORD_KEY] = word
        print(trie.get('o'))

        rowLen = len(board)
        colLen = len(board[0])

        result = []

        ### BackTracking function starts
        def recur(pRow, pCol, parent):
            letter = board[pRow][pCol]
            curNode = parent[letter]

            word_matched = curNode.pop(WORD_KEY, False)
            if word_matched:
                result.append(word_matched)

            ## Mark Visited #
            board[pRow][pCol] = '#'

            for (rowExplore, colExplore) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = pRow + rowExplore, pCol + colExplore
                if newRow < 0 or newRow >= rowLen or newCol < 0 or newCol >= colLen:
                    continue
                if not board[newRow][newCol] in curNode:
                    continue
                recur(newRow, newCol, curNode)
            # End of EXPLORATION, we restore the cell
            board[pRow][pCol] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not curNode:
                parent.pop(letter)

        ### BackTracking function ends

        for r in range(0, rowLen):
            for c in range(0, colLen):
                if board[r][c] in trie:
                    ##print('Start BackTracking : '+board[r][c])
                    recur(r, c, trie)

        return result
