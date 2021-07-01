# Notes

## Binary Search

binary search runs at log2(n) speed. all logs mentioned in this text are assumed to be base 2. this makes sense because binary systems work on a base 2 system.

'log2(32) = x' is like asking "how many 2's do we multiply together to get 32?". the answer is 5, so 2*2*2*2*2 = 2^5 = 32. 

binary search can ONLY be performed on a SORTED list!

## Big O Notation

tells you how fast an algorithm is. the O denotes the maximum (worst case) number of operations it takes to complete the search.

#### From fastest to slowest:
O(*n*), **linear time**. simple search
O(log(*n*)), **log time**. binary search
O(*n**log*n*), quicksort
O(*n*^2), selection sort
O(*n*!), traveling salesperson

# Exercises

1.1 you have a sorted list of 128 names. using binary search what is the max number of steps it would take?

A: binary speed = log2(n) = log2(128) = 7 steps at most


1.2 double the size of the list (now 256), how many steps?

A: 8 steps max


1.3 

