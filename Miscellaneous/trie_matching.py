# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4


def processPat(p_tree, p_pat):
    global wordCurrentCntr
    print(p_pat);
    patLvl = 0
    for p in p_pat:
        if patLvl in p_tree:
            childDict = p_tree.get(patLvl)
            if p not in childDict:
                wordCurrentCntr = wordCurrentCntr + 1
                    ##patLvl = wordCurrentCntr
                childDict[p] = wordCurrentCntr
                p_tree[patLvl] = childDict
                patLvl = childDict.get(p)
            else:
                childDict = dict()
                childDict[p] = patLvl + 1
                p_tree[wordCurrentCntr] = childDict
                wordCurrentCntr = wordCurrentCntr + 1
                patLvl = patLvl + 1
        print(p);
    return p_tree


def build_trie(patterns):
    print(patterns)
    global tree
    for pat in patterns:
        tree = processPat(tree, pat)
    return tree

def solve (text, n, patterns):
    result = []
    tree = build_trie(patterns)
    print(tree)

    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

    return result

tree = dict()
text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)


sys.stdout.write (' '.join (map (str, ans)) + '\n')
