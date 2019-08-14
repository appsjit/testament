#
#  Target Practice 02 - Dynamic Programming - Tabulation/Memoization
#
#  Problem: Coin Sum
#
#  Given an array of coins and a target total, return how many
#  unique ways there are to use the coins to make up that total.
#
#  Input:  coins {Integer Array}, total {Integer}
#  Output: {Integer}
#
#
#  Example:
#  Input:  [1,2,3], 4
#  Output: 4
#
#  1+1+1+1
#  1+3
#  1+1+2
#  2+2
#
#
#  Input:  [2,5,3,6], 10
#  Output: 5
#
#          2+3+5
#          5+5
#          2+3+2+3
#          2+2+6
#          2+2+2+2+2
#
#  Note: You have an unlimited number of each coin type. All coins in the
#        coin array will be unique
#        Order does not matter. Ex: One penny and one nickel to create six
#        cents is equivalent to one nickel and one penny
#
#


# Time Complexity:
# Auxiliary Space Complexity:


## Rule Once coin has been used we can only use that coin and coins following the coins array (To avoid duplicate)


## memoization
def coin_sum(coins, total):
    # YOUR WORK HERE
    cache = {}
    def traverse(curr, startIdx):
        key = str(curr) + "_" + str(startIdx);

        if key in cache.keys():
            return cache[key]

        if (curr == 0) :
            return 1
        if (curr < 0) :
            return 0

        sum = 0

        for x in range(startIdx,len(coins)):  ## startIcx for
            coin = coins[x]
            sum += traverse(curr - coin, x )
        cache[key] = sum;
        return sum


    return traverse(total, 0)


## Recursion
# def coin_sum(coins, total):
#     # YOUR WORK HERE
#     def traverse(curr, startIdx):
#         if (curr == 0) :
#             return 1
#         if (curr < 0) :
#             return 0
#
#         sum = 0
#
#         for x in range(startIdx,len(coins)):  ## startIcx for
#             coin = coins[x]
#             sum += traverse(curr - coin, x )
#
#         return sum
#     return traverse(total, 0)



############################################################
###############  DO NOT TOUCH TEST BELOW!!!  ###############
############################################################

# custom assert function to handle tests
# input: count {List} - keeps track out how many tests pass and how many total
#        in the form of a two item array i.e., [0, 0]
# input: name {String} - describes the test
# input: test {Function} - performs a set of operations and returns a boolean
#        indicating if test passed
# output: {None}
def expect(count, name, test):
    if (count == None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    errMsg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        errMsg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if errMsg != None:
        print('       ' + errMsg + '\n')

def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

print("\nCoin Sum Tests")
test_count = [0, 0]

def test():
    example = coin_sum([1, 2, 3], 4)
    return example == 4

expect(test_count, 'should work for first example case', test)

def test():
    example = coin_sum([2, 5, 3, 6], 10)
    return example == 5

expect(test_count, 'should work for second example case', test)

def test():
    example = coin_sum([2], 10)
    return example == 1

expect(test_count, 'should work for a single coin', test)

def test():
    example = coin_sum([7, 15], 20)
    return example == 0

expect(test_count, 'should work when there is no solution', test)

def test():
    example = coin_sum(
        [78, 10, 4, 22, 44, 31, 60, 62, 95, 37, 28, 11, 17, 67, 33, 3, 65, 9, 26, 52, 25, 69, 41, 57, 93, 70, 96, 5,
         97, 48, 50, 27, 6, 77, 1, 55, 45, 14, 72, 87, 8, 71, 15, 59], 100)
    return example == 3850949

expect(test_count, 'should work for variety of coins and large total', test)

print(('\nPASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1])))
