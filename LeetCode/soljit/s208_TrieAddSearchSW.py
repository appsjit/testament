class TrieNode:
    def __init__(self, value=None):
        self.value = value
        self.next = {}
        self.end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for i in range(0, len(word)):
            letter = word[i]
            if (not letter in current.next):
                current.next[letter] = TrieNode(letter)
            current = current.next[letter]

        current.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        self.isFound = False

        def dfs(word, cur):
            if len(word) < 1:
                if cur.end:
                    self.isFound = True
                return
            elif word[0] == '.':
                for let in cur.next:
                    dfs(word[1:], cur.next[let])
            else:
                if word[0] in cur.next:
                    dfs(word[1:], cur.next[word[0]])
                else:
                    return

        print(word)
        dfs(word, self.root)
        return self.isFound

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        self.isStartWith = False

        def dfsSW(prefix, cur):
            if len(prefix) < 1:
                self.isStartWith = True
            else:
                if prefix[0] in cur.next:
                    dfsSW(prefix[1:], cur.next[prefix[0]])
                else:
                    return

        print(prefix)
        dfsSW(prefix, self.root)
        return self.isStartWith

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)