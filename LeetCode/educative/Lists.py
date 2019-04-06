def findSum(lst,value):
  # Write your code here
  res =[]
  for x in range(len(lst)):
    cval = lst[x]
    for y in range(len(lst)):
      if ((lst[y] != cval) and (lst[y] + cval) ==  value):
        res.append(cval),
        res.append(lst[y])
        return res