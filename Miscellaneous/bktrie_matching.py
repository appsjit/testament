# python3
import sys

NA = -1

class Node:

def processPat(p_tree, p_pat):
    global wordCurrentCntr
    patLvl = 0
        # for p in p_pat:
        #     if patLvl in p_tree:
        #         childDict = p_tree.get(patLvl)
        #         if p not in childDict:
        #             wordCurrentCntr = wordCurrentCntr + 1
        #             ##patLvl = wordCurrentCntr
        #             childDict[p] = wordCurrentCntr
        #             p_tree[patLvl] = childDict
        #         patLvl = childDict.get(p)
        #     else:
        #         childDict = dict()
        #         childDict[p] = patLvl + 1
        #         p_tree[wordCurrentCntr] = childDict
        #         wordCurrentCntr = wordCurrentCntr + 1
        #         patLvl = patLvl + 1
        #     #print(p);
    return p_tree

    def build_trie(patterns):
        global tree
        for pat in patterns:
            tree = processPat(tree, pat)
        return tree

def solve (text,n,p_patterns):
    result = []
    global tree
    print(p_patterns)
    tree = build_trie(p_patterns)
        # for node in tree:
        #     for c in tree[node]:
        #         print("{}->{}:{}".format(node, tree[node][c], c))
    print('write your code here')
    return result

def __init__ (self):
	self.next = [NA] * 4

tree = dict()
wordCurrentCntr = 0
text = 'AAA';##sys.stdin.readline ().strip ()
n = int (1);  ##sys.stdin.readline ().strip ())
patterns = []
patterns.append('AA')
# for i in range (n):
# 	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
