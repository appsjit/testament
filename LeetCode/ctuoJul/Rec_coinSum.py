/ *
*Target
Practice
02 - Dynamic
Programming
* /

'use strict';

/ *
*Problem: Coin
Sum
*
*Given
an
array
of
coins and a
target
total,
return how
many
*unique
ways
there
are
to
use
the
coins
to
make
up
that
total.
*
*Input: coins
{Integer
Array}, total
{Integer}
*Output: {Integer}
*
*
*Example: Input:  [1, 2, 3], 4
*
*1 + 1 + 1 + 1
*1 + 3
*1 + 1 + 2
*2 + 2
*
*Output: 4
*
*
*Input: [2, 5, 3, 6], 10
*
*2 + 3 + 5
*5 + 5
*2 + 3 + 2 + 3
*2 + 2 + 6
*2 + 2 + 2 + 2 + 2
*
*
*Output: 5
*
*Note: You
have
an
unlimited
number
of
each
coin
type.All
coins in the
*coin
array
will
be
unique
*Order
does
not matter.Ex: One
penny and one
nickel
to
create
six
*cents is equivalent
to
one
nickel and one
penny
* /

// Time
Complexity:
// Auxiliary
Space
Complexity:
function
coinSum(coins, total)
{

    function
traverse(current, startIndex)
{
if (current === 0)
{
return 1;
}
if (current < 0) {
return 0;
}

let
sum = 0;
for (let i = startIndex; i < coins.length; i++)
{
let
coin = coins[i];
sum += traverse(current - coin, i);
}
return sum;
}

return traverse(total, 0);
}

// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
// // // // // // // / DO
NOT
TOUCH
TEST
BELOW!!! // // // // // // // /
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // //

console.log('Coin Sum Tests');
let
testCount = [0, 0];

assert (testCount, 'should work for first example case', () = > {
let test = coinSum([1, 2, 3], 4);
return test === 4;
});

assert (testCount, 'should work for second example case', () = > {
let
test = coinSum([2, 5, 3, 6], 10);
return test === 5;
});

assert (testCount, 'should work for a single coin', () = > {
let
test = coinSum([2], 10);
return test === 1;
});

assert (testCount, 'should work when there is no solution', () = > {
let
test = coinSum([7, 15], 20);
return test === 0;
});

assert (testCount, 'should work for variety of coins and large total', () = > {
let
test = coinSum(
    [78, 10, 4, 22, 44, 31, 60, 62, 95, 37, 28, 11, 17, 67, 33, 3, 65, 9, 26, 52, 25, 69, 41, 57, 93, 70, 96, 5, 97, 48,
     50, 27, 6, 77, 1, 55, 45, 14, 72, 87, 8, 71, 15, 59], 100);
return test === 3850949;
});

console.log('PASSED: ' + testCount[0] + ' / ' + testCount[1], '\n\n');

// function
for checking if arrays are equal
function arraysEqual(arr1, arr2) {
if (arr1.length != = arr2.length)
return false;
for (let i = arr1.length; i--;) {
if (arr1[i] !== arr2[i])
    return false;
}
return true;
}

// custom
assert function
to
handle
tests
// Array
count: keeps
track
out
how
many
tests
pass and how
many
total
// in the
form
of
a
two
item
array
i.e., [0, 0]
// String
name: describes
the
test
// Function
test: performs
a
set
of
operations and returns
a
boolean
// indicating if test
passed
function
assert (count, name, test)
{
if (!count | | !Array.isArray(count) | | count.length !== 2) {
count =[0, '*'];
} else {
count[1]++;
}

let
pass = 'false';
let
errMsg = null;
try {
if (test()) {
pass = ' true';
count[0]++;
}
} catch (e) {
errMsg = e;
}
console.log('  ' + (count[1] + ')   ').slice(0, 5) +
pass
+ ' : ' + name);
if (errMsg !== null) {
console.log('       ' + errMsg + '\n');
}
}