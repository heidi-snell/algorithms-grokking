# Notes

## Binary Search

binary search runs at log2(*n*) speed. all logs mentioned in this text are assumed to be base 2. this makes sense because binary systems work on a base 2 system.

log2(32) = x is like asking "how many 2's do we multiply together to get 32?". the answer is 5, so 2*2*2*2*2 = 2^5 = 32. 

binary search can ONLY be performed on a SORTED list!

## Big O Notation

tells you how fast an algorithm is. the O denotes the maximum (worst case) number of **operations** it takes to complete the search.

### From fastest to slowest:
+ O(*n*), **linear time** - simple search
+ O(log(*n*)), **log time** - binary search
+ O(*n**log*n*) - quicksort
+ O(*n*^2) - selection sort
+ O(*n*!) - traveling salesperson

## Traveling Salesperson

traveling to *n* different cities - to compute the shortest path between all cities, you can calculate all posibilities, add up the distances and choose the one with the shortest path. it requires *n*! operations to find all posibilities! this sucks. it is so slow. 

## Takeaways

+ binary search is faster than simple search
+ O(log*n*) is faster than O(*n*), especially for longer lists
+ algorithm speed is not measured in seconds
+ algorithm times are measured in terms of *growth* of an algorithm
+ algorithm times are written in Big O notation

# Exercises

**1.1** you have a sorted list of 128 names. using binary search what is the max number of steps it would take?  
A: binary speed = log2(n) = log2(128) = 7 steps at most


**1.2** double the size of the list (now 256), how many steps?  
A: 8 steps max

#### give the runtime for each of these scenarios in terms of Big ):
**1.3** you have a name and want to find a persons phone number in the phone book  
A: O(log*n*)... binary search

**1.4** you have a phone number and want to find the persons name in the phone book  
A: O(*n*)... simple search, this is not an ordered list

**1.5** you want to read the numbers of every person in the phone book  
A: O(*n*)... simple search

**1.6** you want to read the numbers of just the *A*'s... this concept covered more in chapter 4  
A: simple search, but for only the first part of the list. will have to find out in ch 4

