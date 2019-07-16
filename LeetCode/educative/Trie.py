from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of character 't'
    def getIndex(self, t):
        return ord(t) - ord('a')

    # Function to insert a key,value pair in the Trie
    def insert(self, key, value):
        # None keys are not allowed
        if key == None:
            return

        key = key.lower()  # Keys are stored in lowercase
        currentNode = self.root
        index = 0  # to store character index

        # Iterate the Trie with given character index,
        # If it is None, then simply create a TrieNode and go down a level
        for level in range(len(key)):
            index = self.getIndex(key[level])

            if currentNode.children[index] == None:
                currentNode.children[index] = TrieNode()

            currentNode = currentNode.children[index]

        # Mark the end character as leaf node
        currentNode.markAsLeaf()

    # Function to search a given key in Trie
    def search(self, key):
        if key == None:
            return False  # None key

        key = key.lower();
        currentNode = self.root
        index = 0

        # Iterate the Trie with given character index,
        # If it is None at any point then we stop and return false
        # We will return true only if we reach leafNode and have traversed the
        # Trie based on the length of the key

        for level in range(len(key)):
            index = self.getIndex(key[level])
            if currentNode.children[index] == None:
                return False
            currentNode = currentNode.children[index]

        if currentNode != None and currentNode.isEndWord:
            return True

        return False

    # Helper Function to return true if currentNode does not have any children
    def hasNoChildren(self, currentNode):
        for i in range(len(currentNode.children)):
            if currentNode.children[i] != None:
                return False
        return True

    # Recursive function to delete given key
    def deleteHelper(self, key, currentNode, length, level):
        deletedSelf = False

        if currentNode == None:
            print("Key does not exist")
            return deletedSelf

        # Base Case: If we have reached at the node which points to the alphabet at the end of the key.
        if level == length:
            # If there are no nodes ahead of this node in this path
            # Then we can delete this node
            if self.hasNoChildren(currentNode):
                currentNode = None
                deletedSelf = True

            # If there are nodes ahead of currentNode in this path
            # Then we cannot delete currentNode. We simply unmark this as leaf
            else:
                currentNode.unMarkAsLeaf()
                deletedSelf = False

        else:
            childNode = currentNode.children[self.getIndex(key[level])]
            childDeleted = self.deleteHelper(key, childNode, length, level + 1)
            if childDeleted:
                # Making children pointer also None: since child is deleted
                currentNode.children[self.getIndex(key[level])] = None;
                # If currentNode is leaf node that means currentNode is part of another key
                # and hence we can not delete this node and it's parent path nodes
                if currentNode.isEndWord:
                    deletedSelf = False

                # If childNode is deleted but if currentNode has more children then currentNode must be part of another key
                # So, we cannot delete currenNode
                elif self.hasNoChildren(currentNode) == False:
                    deletedSelf = False

                # Else we can delete currentNode
                else:
                    currentNode = None
                    deletedSelf = True

            else:
                deletedSelf = False

        return deletedSelf

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root == None or key == None:
            print("None key or empty trie error")
            return

        self.deleteHelper(key, self.root, len(key), 0)


# Input keys (use only 'a' through 'z' and lower case)
keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
output = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

# Construct Trie
for i in range(len(keys)):
    t.insert(keys[i], i)

# Search for different keys
if t.search("the") == True:
    print("the --- " + output[1])
else:
    print("the --- " + output[1])

if t.search("these") == True:
    print("these --- " + output[1])
else:
    print("these --- " + output[0])

if t.search("abc") == True:
    print("abc --- " + output[1])
else:
    print("abc --- " + output[1])

t.delete("abc");
print("Deleted key \"abc\"");

if t.search("abc") == True:
    print("abc --- " + output[1]);
else:
    print("abc --- " + output[0]);
