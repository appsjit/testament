import collections
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
#         if endWord not in wordList or not endWord or not beginWord or not wordList:
#             return 0
#
#         L = len(beginWord)
#
#         wordComb = collections.defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 ##print(word[:i]+"*"+word[i+1:])
#                 wordComb[word[:i] + "*" + word[i + 1:]].append(word)
#
#         print(wordComb)
#         prQ = collections.deque([(beginWord, 1)])
#         visited = {beginWord: True}
#
#         while prQ:
#             currWord, lvl = prQ.popleft()
#             ##print(currWord)
#             for i in range(L):
#                 intermediateWord = currWord[:i] + "*" + currWord[i + 1:]
#                 ##print(intermediateWord)
#                 for word in wordComb[intermediateWord]:
#                     if word == endWord:
#                         return lvl + 1
#
#                     if word not in visited:
#                         visited[word] = True
#                         prQ.append((word, lvl + 1))
#                 wordComb[intermediateWord] = []
#
#         return 0



from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queues for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = collections.deque([(endWord, 1)]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

s = Solution()
print(s.ladderLength('hit','cog',['hot','dot','dog','lot','log','cog']))