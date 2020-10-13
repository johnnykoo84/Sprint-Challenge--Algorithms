#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) the runtime will n times. When this code runs for 1 sec with n=1, then it will be n seconds. O(n)

Reason: the whil loop pseudocde is acutally a math question as below

```
a + C*n^2 < n^3 # here a = 0 initially so
C*n^2 < n^3
n^3 - C*n^2 > 0
n^2(n-C) > 0
```

so when n is equal to C the loop stops
we could say n = C, Whatever n is given, it will take n then.

b) I'not sure about b)
When I do the math, it seems like solving the problem below
2^(n-1) < n
but I'm not sure how to solve it, and it seems not that lambda wants me to solve math problem here so.

c) if bunnies = n, the answer is n times. If n=1, and it takes 1sec, then the answer is s seconds. O(n)

Reason: bunnies will decrease by one as it goes one recursion. When bunnies = 0, then the recursion stops. (exit condtion)

## Exercise II

answer) We randomly pick the middle floor and try dropping it. If it breaks, then we pick another lower middle floor, otherwise we go to upper middle floor, this way we know it is not O(n), but rather, O(Log(n)), just like binary search
