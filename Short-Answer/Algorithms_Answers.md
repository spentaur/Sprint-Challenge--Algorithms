# Please add your answers to the **_Analysis of Algorithms_** exercises here

## Exercise I

a) O(n)  
The n^2 that a is incrementing by cancels out 2 from the n^3 in the while loop. For example:

```python
n = 5

a = 0
# 175 = 5*5*5
while a < 175:
    # 25 = 5 * 5
    a += 25
    # 1: 25
    # 2: 50
    # 3: 75
    # 4: 100
    # 5: 125

```

Since a is increasing by 25 each time, you can see that it would take `n` times to exit loop.
If we run through another test case, if `n = 10` the code would look like:

```python
n = 10
a = 0
# 1000 = 10*10*10
while a < 1000:
    a += 100
    # 1: 100
    # 2: 200
    # 3: 300
    # 4: 400
    # 5: 500
    # 6: 600
    # 7: 700
    # 8: 800
    # 9: 900
    # 10: 1000
```

As you can see, as n increases, the number of loops increases by n, so it would be linear, or O(n)

b) O(n + log2(n))  
This one I'm not so sure about. I know that the first loop is linear. But the while loop throws me off. j increases exponentially (2^j) so I need to figure out when j will be greater than n. so 2^x = n so to solve for x I need to log base 2 of n. Again, not 100% on this one.

c) O(n)  
Since the parameter is decreasing by 1 until it reaches 0, this one would be linear.

## Exercise II

### IF THE BUILDING IS SUPER DUPER TALL

#### O(log(n))

Probably use a binary search approach. Start at on the middle floor. If the egg doesn't break, we know it wont break on any of the floors under. So now we only have half the floors to work with. Then just repeat. Start at the middle of the remaining half, if the egg breaks, we know it would break at any of the above floors so we can eliminate those. Repeat until you have 2 floors left, one where it breaks, and one where it doens't.
