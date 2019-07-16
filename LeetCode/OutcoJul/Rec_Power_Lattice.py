#
# Target Practice 01 - Recursion
#
# Problem 1: Power Set
#
# Prompt:   Given a set S, return the powerset P(S), which is
#           a set of all subsets of S.
#
# Input:    A String
# Output:   An Array of String representing the power set of the input
#
# Example:  S = "abc", P(S) = ['', 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc']
#
# Note:     The input string will not contain duplicate characters
#           The letters in the subset string must be in the same order
#           as the original input.

# Problem 2: Lattice Paths
#
# Prompt:  Count the number of unique paths to travel from the top left
#          corder to the bottom right corner of a lattice of M x N squares.
#
#          When moving through the lattice, one can only travel to the
#          adjacent corner on the right or down.
#
# Input:   m {Integer} - rows of squares
# Input:   n {Integer} - column of squares
# Output:  {Integer}
#
# Example: input: (2, 3)
#
#          (2 x 3 lattice of squares)
#           __ __ __
#          |__|__|__|
#          |__|__|__|
#
#          output: 10 (number of unique paths from top left corner to bottom right)
#
# Resource: https://projecteuler.net/problem=15
#
#


def powerset(input):
    results = []

    def traverse(build, depth):
        print('build '+build+'   depth '+str(depth))
        if (depth == len(input)):
            results.append(build)
            return
        traverse(build, depth + 1)
        traverse(build + input[depth], depth + 1)

    traverse("", 0)
    return results


def lattice_paths(m, n):
    if (m == 0 and n == 0):
        return 1
    if (m < 0 or n < 0):
        return 0
    return lattice_paths(m - 1, n) + lattice_paths(m, n - 1)


# ###########################################################
# ##############  DO NOT TOUCH TEST BELOW!!!  ###############
# ###########################################################


from io import StringIO
import sys


# custom expect function to handle tests
# List count : keeps track out how many tests pass and how many total
#   in the form of a two item array i.e., [0, 0]
# String name : describes the test
# Function test : performs a set of operations and returns a boolean
#   indicating if test passed
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
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
    if errMsg is not None:
        print('       ' + errMsg + '\n')


# code for checking if lists contain the same elements
def lists_matching(lst1, lst2):
    if len(lst1) != len(lst2):
        return False

    cache = {}
    for i in range(0, len(lst1)):
        if lst1[i] in cache:
            cache[lst1[i]] += 1
        else:
            cache[lst1[i]] = 1
    for j in range(0, len(lst2)):
        if lst2[j] not in cache or cache[lst2[j]] == 0:
            return False
        cache[lst2[j]] -= 1
    return True


print('Powerset Tests')
test_count = [0, 0]


def test():
    example = powerset('abc')
    return (example is not None and lists_matching(example,
                                                   ['', 'a', 'b', 'c', 'ab', 'bc', 'ac', 'abc']))


expect(test_count, 'should work on example input abc', test)


def test():
    example = powerset('')
    return example is not None and lists_matching(example, [''])


expect(test_count, 'should work on empty input', test)


def test():
    example = powerset('ab')
    return (example is not None and
            lists_matching(example, ['', 'a', 'b', 'ab']))


expect(test_count, 'should work on two-letter input', test)


def test():
    example = powerset('abcdefg')
    solution = ['', 'g', 'f', 'fg', 'e', 'eg', 'ef', 'efg', 'd', 'dg', 'df',
                'dfg', 'de', 'deg', 'def', 'defg', 'c', 'cg', 'cf', 'cfg',
                'ce', 'ceg', 'cef', 'cefg', 'cd', 'cdg', 'cdf', 'cdfg', 'cde',
                'cdeg', 'cdef', 'cdefg', 'b', 'bg', 'bf', 'bfg', 'be', 'beg',
                'bef', 'befg', 'bd', 'bdg', 'bdf', 'bdfg', 'bde', 'bdeg',
                'bdef', 'bdefg', 'bc', 'bcg', 'bcf', 'bcfg', 'bce', 'bceg',
                'bcef', 'bcefg', 'bcd', 'bcdg', 'bcdf', 'bcdfg', 'bcde',
                'bcdeg', 'bcdef', 'bcdefg', 'a', 'ag', 'af', 'afg', 'ae',
                'aeg', 'aef', 'aefg', 'ad', 'adg', 'adf', 'adfg', 'ade',
                'adeg', 'adef', 'adefg', 'ac', 'acg', 'acf', 'acfg', 'ace',
                'aceg', 'acef', 'acefg', 'acd', 'acdg', 'acdf', 'acdfg',
                'acde', 'acdeg', 'acdef', 'acdefg', 'ab', 'abg', 'abf', 'abfg',
                'abe', 'abeg', 'abef', 'abefg', 'abd', 'abdg', 'abdf', 'abdfg',
                'abde', 'abdeg', 'abdef', 'abdefg', 'abc', 'abcg', 'abcf',
                'abcfg', 'abce', 'abceg', 'abcef', 'abcefg', 'abcd', 'abcdg',
                'abcdf', 'abcdfg', 'abcde', 'abcdeg', 'abcdef', 'abcdefg']
    return example is not None and lists_matching(example, solution)


expect(test_count, 'should work on longer input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('Lattice Paths Tests')
test_count = [0, 0]


def test():
    example = lattice_paths(2, 3)
    return example == 10


expect(test_count, 'should work on example case', test)


def test():
    example = lattice_paths(0, 0)
    return example == 1


expect(test_count, 'should return 1 for 0 x 0 lattice', test)


def test():
    example = lattice_paths(11, 13)
    return example == 2496144


expect(test_count, 'should return 2496144 for 13 x 11 lattice', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')