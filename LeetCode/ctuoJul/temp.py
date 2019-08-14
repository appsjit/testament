#
#  Homework 12 - Binary Heap
#
#  Problem: Binary Heap Class
#
#  Prompt: Create a Heap class/constructor
#
#  The Heap will take in the following input:
#
#                type: argument should be either 'min' or 'max'. This will
#                      dictate whether the heap will be a minheap or maxheap.
#                      The comparator method will be affected by this
#                      argument. See method description below
#
#  The Heap will have the following property:
#
#             storage: list
#
#                type: property that will be either 'min' or 'max'. This will
#                      be dictated by
#
#  The Heap will have the following methods:
#
#             compare: takes in two arguments (a and b). Depending on the heap
#                      type (minheap or maxheap), the comparator will behave
#                      differently. If the heap is a minheap, then the compare
#                      function will return true if a is less than b, false
#                      otherwise. If the heap is a maxheap, then the compare
#                      function will return true if a is greater than b, false
#                      otherwise.
#
#                swap: takes in two indexes and swaps the elements at the two
#                      indexes in the storage list
#
#                peak: returns the peak element of the storage list. This
#                      will be the most minimum and maximum element for a
#                      minheap and maxheap respectively
#
#                size: returns the number of elements in the heap
#
#              insert: inserts a value into the heap. Should begin by pushing
#                      the value onto the end of the list, and then calling
#                      the bubbleUp method from the last index of the list
#
#           bubble_up: takes in an index, and considers the element at that
#                      index to be a child. Continues to swap that child with
#                      its parent value if the heap comparator condition is
#                      not fulfilled
#
#         remove_peak: removes the peak element from the heap and returns it.
#                      Should begin by swapping the 0th-index element with the
#                      last element in the storage list. Uses bubbleDown
#                      method from the 0th index
#
#         bubble_down: takes in an index, and considers the element at this
#                      index to be the parent. Continues to swap this parent
#                      element with its children if the heap comparator
#                      condition is not fulfilled
#
#              remove: takes in a value and (if it exists in the heap),
#                      removes that value from the heap data structure and
#                      returns it. Should rearrange the rest of the heap to
#                      ensure the heap comparator conditions are fulfilled
#                      for all of its elements
#
#
#
#  Input:  N/A
#  Output: A Heap instance
#
#  What are the time and auxilliary space complexities of the various methods?
#

class Heap:

    def __init__(self, type='min'):
        self.type = type
        self.storage = []

    def getParent(self, child):
        if (child%2 == 0):
            return int((child - 2)/2)
        else:
            return int((child -1)/2)

    def getChild(self, parent):
        child1 = 2*parent + 1
        child2 = 2*parent + 2

        if (child1 >= self.size()):
            return child1
        elif (child2 >= self.size()):
            return child1
        elif ( self.compare(self.storage[child1], self.storage[child2] ) ):##self.storage[child1] < self.storage[child2]):
            return child1
        else :
            return child2


    # Time Complexity:
    # Auxiliary Space Complexity:
    def compare(self, a, b):
        if self.type == 'min' :
            if self.storage[a] < self.storage[b] :
                return True
            else:
                return False

        if self.type == 'max' :
            if self.storage[a] > self.storage[b] :
                return True
            else:
                return False

    # Time Complexity:
    # Auxiliary Space Complexity:
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

    # Time Complexity:
    # Auxiliary Space Complexity:
    def peak(self):
        if self.size() == 0:
            return None

        return self.storage[0]

    # Time Complexity:
    # Auxiliary Space Complexity:
    def size(self):
        return len(self.storage)

    # Time Complexity:
    # Auxiliary Space Complexity:
    def insert(self, value):
        self.storage.append(value)
        self.bubble_up(self.size() - 1)
        # if self.type == 'min':
        #     self.bubble_up(self.size() -1)
        # elif self.type == 'max':
        #     self.bubble_down(0)

    # Time Complexity:
    # Auxiliary Space Complexity:
    def bubble_up(self, index):
        parent = self.getParent(index)
        while(index > 0  and self.compare(self.storage[index], self.storage[parent])) :  ##self.storage[index] < self.storage[parent]):
            self.swap(index, parent)
            index = parent
            parent = self.getParent(index)

    # Time Complexity:
    # Auxiliary Space Complexity:
    def remove_peak(self):
        # YOUR WORK HERE
        pass

    # Time Complexity:
    # Auxiliary Space Complexity:
    def bubble_down(self, index):
        child = self.getChild(index)

        while (child < self.size() and self.compare(self.storage[child],  self.storage[index])):##self.storage[index] > self.storage[child]):
            self.swap(child, index)
            index = child
            child = self.getChild(index)

    # Time Complexity:
    # Auxiliary Space Complexity:
    def remove(self, value):
        remIndx = -1

        for x in range(self.size() - 1 ):
            if (self.storage[x] == value):
                remIndx = x

        if remIndx == -1:
            return

        self.swap(remIndx, self.size()-1)

        self.storage.pop()
        self.bubble_up(remIndx)
        self.bubble_down(remIndx)


work = Heap('max')
work.insert(5)
work.insert(10)
work.insert(7)
work.insert(1)
work.insert(8)
work.insert(6)

print(work.storage)

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
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')

# compare if two flat lists are equal
def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True



print('Heap Class')
test_count = [0, 0]


def test():
    work = Heap()
    return isinstance(work, object)


expect(test_count, 'able to create an instance', test)


def test():
    work = Heap()
    return hasattr(work, 'storage')


expect(test_count, 'has storage property', test)


def test():
    work = Heap()
    return hasattr(work, 'type')


expect(test_count, 'has type property', test)


def test():
    work = Heap()
    return isinstance(work.storage, list)


expect(test_count, 'default storage set to a list', test)


def test():
    work = Heap()
    return work.type == 'min'


expect(test_count, 'default type property is set to \'min\'', test)


def test():
    work = Heap('max')
    return work.type == 'max'


expect(test_count, 'default type property can be set to \'max\'', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap compare method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'compare') and callable(getattr(work, 'compare'))


expect(test_count, 'has compare method', test)


def test():
    work = Heap('min')
    work.storage.append(1)
    work.storage.append(10)
    return work.compare(0, 1) is True


expect(test_count, 'returns true for minheap if element at first argument index is less than element at second argument index', test)


def test():
    work = Heap('min')
    work.storage.append(10)
    work.storage.append(1)
    return work.compare(0, 1) is False


expect(test_count, 'returns false for minheap if element at first argument index is greater than element at second argument index', test)


def test():
    work = Heap('max')
    work.storage.append(10)
    work.storage.append(1)
    return work.compare(0, 1) is True


expect(test_count, 'returns true for maxheap if element at first argument index is greater than element at second argument index', test)


def test():
    work = Heap('max')
    work.storage.append(1)
    work.storage.append(10)
    return work.compare(0, 1) is False


expect(test_count, 'returns false for maxheap if element at first argument index is less than element at second argument index', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap swap method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'swap') and callable(getattr(work, 'swap'))


expect(test_count, 'has swap method', test)


def test():
    work = Heap()
    work.storage.append(1)
    work.storage.append(5)
    work.storage.append(10)
    work.swap(0, 2)
    return work.storage[0] == 10 and work.storage[2] == 1


expect(test_count, 'should be able to swap the locations of two elements given two indices', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap peak method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'peak') and callable(getattr(work, 'peak'))


expect(test_count, 'has peak method', test)


def test():
    work = Heap()
    work.storage.append(1)
    work.storage.append(5)
    work.storage.append(10)
    return work.peak() == 1


expect(test_count, 'should return the 0th element of the storage array', test)


def test():
    work = Heap('min')
    work.insert(2)
    work.insert(5)
    work.insert(10)
    work.insert(1)
    return work.peak() == 1


expect(test_count, 'upon building out your insert method, should return the smallest element for a minheap', test)


def test():
    work = Heap('max')
    work.insert(2)
    work.insert(5)
    work.insert(10)
    work.insert(1)
    return work.peak() == 10


expect(test_count, 'upon building out your insert method, should return the largest element for a maxheap', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap size method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'size') and callable(getattr(work, 'size'))


expect(test_count, 'has size method', test)


def test():
    work = Heap()
    work.storage.append(1)
    work.storage.append(5)
    work.storage.append(10)
    return work.size() == 3


expect(test_count, 'returns number of elements in the storage array', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap insert method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'insert') and callable(getattr(work, 'insert'))


expect(test_count, 'has insert method', test)


def test():
    work = Heap()
    work.insert(5)
    return work.storage[0] == 5


expect(test_count, 'should be able to insert a single element', test)


def test():
    work = Heap('min')
    work.insert(5)
    work.insert(10)
    work.insert(7)
    work.insert(1)
    work.insert(8)
    work.insert(6)
    return work.peak() == 1


expect(test_count, 'should be able to insert multiple elements into a minheap and have peak element be smallest element', test)


def test():
    work = Heap('max')
    work.insert(5)
    work.insert(10)
    work.insert(7)
    work.insert(1)
    work.insert(8)
    work.insert(6)
    return work.peak() == 10


expect(test_count, 'should be able to insert multiple elements into a maxheap and have peak element be largest element', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap bubble_up method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'bubble_up') and callable(getattr(work, 'bubble_up'))


expect(test_count, 'has bubble_up method', test)


def test():
    work = Heap('min')
    work.storage = [2, 4, 7, 6, 9, 10, 8, 1]
    work.bubble_up(7)
    return lists_equal([1, 2, 7, 4, 9, 10, 8, 6], work.storage)


expect(test_count, 'should be able to \'bubble up\' an element if its minheap condition is not fulfilled', test)


def test():
    work = Heap('max')
    work.storage = [9, 8, 5, 7, 3, 6, 2, 10]
    work.bubble_up(7)
    return lists_equal([10, 9, 5, 8, 3, 6, 2, 7], work.storage)


expect(test_count, 'should be able to \'bubble up\' an element if its maxheap condition is not fulfilled', test)


def test():
    work = Heap('min')
    work.storage = [1, 2, 7, 4, 9, 10, 8, 6]
    work.bubble_up(7)
    return lists_equal([1, 2, 7, 4, 9, 10, 8, 6], work.storage)


expect(test_count, 'should not perform bubbling up if minheap conditions are fulfilled', test)


def test():
    work = Heap('max')
    work.storage = [10, 9, 5, 8, 3, 6, 2, 7]
    work.bubble_up(7)
    return lists_equal([10, 9, 5, 8, 3, 6, 2, 7], work.storage)


expect(test_count, 'should not perform bubbling down if maxheap conditions are fulfilled', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap remove_peak method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'remove_peak') and callable(getattr(work, 'remove_peak'))


expect(test_count, 'has remove_peak method', test)


def test():
    work = Heap()
    work.insert(5)
    work.remove_peak()
    return len(work.storage) == 0


expect(test_count, 'should be able to remove a single element', test)


def test():
    work = Heap('min')
    work.storage = [1, 2, 7, 4, 9, 10, 8, 6]
    example = work.remove_peak()
    return example == 1 and lists_equal([2, 4, 7, 6, 9, 10, 8], work.storage)


expect(test_count, 'should be able to remove and return peak element for a minheap and rearrange minheap accordingly', test)


def test():
    work = Heap('max')
    work.storage = [10, 9, 5, 8, 3, 6, 2, 7]
    example = work.remove_peak()
    return example == 10 and lists_equal([9, 8, 5, 7, 3, 6, 2], work.storage)


expect(test_count, 'should be able to remove and return peak element for a maxheap and rearrange maxheap accordingly', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap bubble_down method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'bubble_down') and callable(getattr(work, 'bubble_down'))


expect(test_count, 'has bubble_down method', test)


def test():
    work = Heap('min')
    work.storage = [10, 1, 2, 7, 4, 9, 8, 6]
    work.bubble_down(0)
    return lists_equal([1, 4, 2, 7, 10, 9, 8, 6], work.storage)


expect(test_count, 'should be able to \'bubble down\' an element if its minheap condition is not fulfilled', test)


def test():
    work = Heap('max')
    work.storage = [2, 10, 9, 5, 8, 3, 6, 7]
    work.bubble_down(0)
    return lists_equal([10, 8, 9, 5, 2, 3, 6, 7], work.storage)


expect(test_count, 'should be able to \'bubble down\' an element if its maxheap condition is not fulfilled', test)


def test():
    work = Heap('min')
    work.storage = [1, 2, 7, 4, 9, 10, 8, 6]
    work.bubble_down(0)
    return lists_equal([1, 2, 7, 4, 9, 10, 8, 6], work.storage)


expect(test_count, 'should not perform bubbling down if minheap conditions are fulfilled', test)


def test():
    work = Heap('max')
    work.storage = [10, 9, 5, 8, 3, 6, 2, 7]
    work.bubble_down(0)
    return lists_equal([10, 9, 5, 8, 3, 6, 2, 7], work.storage)


expect(test_count, 'should not perform bubbling down if maxheap conditions are fulfilled', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')


print('Heap remove method')
test_count = [0, 0]


def test():
    work = Heap()
    return hasattr(work, 'remove') and callable(getattr(work, 'remove'))


expect(test_count, 'has remove method', test)


def test():
    work = Heap('min')
    work.storage = [1, 2, 7, 4, 9, 10, 8, 6]
    example = work.remove(10)
    return example == 10 and lists_equal(work.storage, [1, 2, 6, 4, 9, 7, 8])


expect(test_count, 'is able to remove specified value from minheap', test)


def test():
    work = Heap('max')
    work.storage = [10, 9, 5, 8, 3, 6, 2, 7]
    example = work.remove(6)
    return example == 6 and lists_equal(work.storage, [10, 9, 7, 8, 3, 5, 2])


expect(test_count, 'is able to remove specified value from maxheap', test)


def test():
    work = Heap('min')
    work.storage = [1, 2, 7, 4, 9, 10, 8, 6]
    example = work.remove(6)
    return example == 6 and lists_equal(work.storage, [1, 2, 7, 4, 9, 10, 8])


expect(test_count, 'is able to remove last value from minheap', test)


def test():
    work = Heap('max')
    work.storage = [10, 9, 5, 8, 3, 6, 2, 7]
    example = work.remove(7)
    return example == 7 and lists_equal(work.storage, [10, 9, 5, 8, 3, 6, 2])


expect(test_count, 'is able to remove last value from maxheap', test)


def test():
    work = Heap('min')
    work.storage = [1, 2, 7, 4, 9, 10, 8, 6]
    work.remove(3)
    return lists_equal(work.storage, [1, 2, 7, 4, 9, 10, 8, 6])


expect(test_count, 'does not remove anything from minheap if value does not exist', test)


def test():
    work = Heap('max')
    work.storage = [10, 9, 5, 8, 3, 6, 2, 7]
    work.remove(4)
    return lists_equal(work.storage, [10, 9, 5, 8, 3, 6, 2, 7])


expect(test_count, 'does not remove anything from maxheap if value does not exist', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
