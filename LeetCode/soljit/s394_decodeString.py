class Solution:
    def decodeString(self, s: str) -> str:
        ans = ""

        def peek_stack(stack):
            if stack:
                return stack[-1]  # this will get the last element of stack
            else:
                return None

        stack = []
        k = ''
        for idx, x in enumerate(s):
            if x == '[':
                # Store the current string in stack with the current multiplier
                stack.append((idx, int(k)))
                k = ''
                continue
            elif x == ']':
                ## pop last string
                last_string, last_k = stack.pop()
                if stack == []:
                    inside = self.decodeString(s[last_string + 1:idx])
                    ans += last_k * inside
                continue
                ##ans = last_string + ans*last_k
            elif x.isnumeric():
                k += x
                continue

            if stack == []:
                ans += x

        return ans
#     def decodeString(self, s: str) -> str:
#         ans = ""
#         def peek_stack(stack):
#             if stack:
#                 return stack[-1]    # this will get the last element of stack
#             else:
#                 return None

#         stack = []
#         k = 0
#         for x in s:
#             if x == '[' :
#             # Store the current string in stack with the current multiplier
#                 stack.append((ans, k))
#                 ans = ""
#                 k = 0
#             elif x == ']' :
#                 ## pop last string
#                 last_string, last_k = stack.pop(-1)
#                 ans = last_string + ans*last_k
#             elif x.isnumeric():
#                 k = k*10 + int(x)
#             else :
#                 ans += x

#         return ans

