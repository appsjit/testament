class TrieNode:
    def __init__(self, char=''):
        self.children = [None] * 26  # Total # of English Alphabets
        self.isEndWord = False  # will be true if the node represents the end of word
        self.char = char  # To store the value of a particular key

    # Function to mark the currentNode as Leaf
    def markAsLeaf(self):
        self.isEndWord = True

    # Function to unMark the currentNode as Leaf
    def unMarkAsLeaf(self):
        self.isEndWord = False


trieNode = TrieNode('a')
print(trieNode.char)