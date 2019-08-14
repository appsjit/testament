
# ```
# Input: "abc"
# Output: ["ABC", "ABc", "AbC", "aBC", "Abc", "aBc", "abC", "abc"]






#                              abc

#                           /         \
#                      abc .           Abc
#                     /   \          /     \
#                 abc     aBc       Abc         ABc
#               /  \       / \       /   \ .     / .   \
#             abc   abC   aBc  aBC Abc .  AbC   ABc        ABC





def cal(str):
  ans = []

  def traverse( build , depth) :
      if (depth == len(str)):
        ans.append(build)
        return
      traverse(build + str[depth], depth +1 )
      #traverse(build[0:depth].upper() + build[depth: len(str) - depth  ] + build[ len(str) - depth:].upper()  ,   depth + 1 )
      traverse(build + str[depth].upper(), depth + 1)



  traverse("", 0)

  return ans


print(cal('abc'))