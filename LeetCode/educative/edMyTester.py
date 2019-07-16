# list = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# def foo(m):
#   print(m)
#   print(m[1][0])
#
#   v = m[0][0]
#
#   for row in m:
#     print(row)
#     for element in row:
#       if v < element: v = element
#   return v
#
# print(foo(list[0]))

############################################

# lst = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
#
# for i in range(0, 4):
#     ##print(i)
#     print(lst[i].pop())
#     ##print(lst[i].pop()),


def f(i, values = []):
    values.append(i)
    print (values),
    return values
f(1)
f(2)
f(3)