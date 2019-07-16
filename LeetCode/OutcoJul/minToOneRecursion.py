def minimumStepsToOne(num):
    # Write your code here

    if num == 1:
        return 0

    st = minimumStepsToOne(num - 1)

    if (num % 3 == 0):
        st3 = minimumStepsToOne(num / 3)
        st = min(st3, st)

    if (num % 2 == 0):
        st2 = minimumStepsToOne(num / 2)
        st = min(st2, st)

    return st + 1


print(minimumStepsToOne(30))