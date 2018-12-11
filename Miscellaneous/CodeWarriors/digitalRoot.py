def digital_root(n):
        return n if n < 10 else digital_root(sum(map(int, str(n))))

# def digital_root(n):
#     # ...
#     while n>9:
#         n=sum(map(int,str(n)))
#     return n
#
# def digital_root(n):
#     while n>10:
#         n = sum([int(i) for i in str(n)])
#     return n
#
# def digital_root(n):
#     while (n > 9):
#         n = reduce(lambda a, b: int(a) + int(b), list(str(n)))
#     return n
#
#
# def digital_root(n):
#     return n if n < 10 else digital_root(sum([int(c) for c in str(n)]))
#
