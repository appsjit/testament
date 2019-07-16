def print_list(lst):
    # YOUR WORK HERE
    if len(lst) == 0:
        print(lst[0])
    else:
        if len(lst ) > 1:
            return print_list(lst[1:])



if __name__ == '__main__':
    print(print_list([1,2,3]))
