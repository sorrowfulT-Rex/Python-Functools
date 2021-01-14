# Accessibility

Current Version: 0.0.6  
Install with ```pip install RC-Functools```  
```from RC_Functools import rc_func``` to use  

# Introduction

Since I just had some courses on Haskell and Kotlin, I found it intriguing to implement some of the functional tools in Python. For example, forEach and mapIndexed from Kotlin and ($) and scanl from Haskell. I've also included more intricate functions such as filter_acc, which can be used to build cool one-liners such as prime filterer with the Sieve of Eratosthenes. Check for the examples provided in the code.

Additionally, I've added some null-handling (None-handling?) functions, such as one that imitates the Elvis Operator in Kotlin/Swift.

# RC-Functools (rc_func)

The prefix "l\_" means the function returns a list instead of a map;  
The suffix "\_r" means the function starts from the right of the list, e.g. reduce_r is foldr in Haskell.  

## flatmap(f, \*args) -> list  
* Parameter f takes a function that takes n (n > 0) parameters and returns an iterable;
* Parameters \*args takes n iterables;
* Returns the list concatenated from the lists result from applying f on each corresponding elements of \*arg.
```
rc_func.flatmap(lambda x: [x, x + 2], [2, 3, 4])
# [2, 4, 3, 5, 4, 6]
```

## flatmap_indexed(f, \*args) -> list  
* Parameter f takes a function that takes an index (int) and n (n > 0) parameters and returns an iterable;
* Parameters \*args takes n iterables;
* Returns the list concatenated from the lists result from applying f on the index and each corresponding elements of \*arg.
```
rc_func.flatmap_indexed(lambda i, x: [i, x], [2, 3, 4])
# [0, 2, 1, 3, 2, 4]
```

## l_map(f, \*args)
* Returns list converted from the map object; list(map(f, \*args)). Same below for all functions starting with "l\_".

## map_indexed(f, \*args)
* Parameter f takes a function that takes an index (int) and n (n > 0) parameters and returns an iterable;
* Parameters \*args takes n iterables;
* Returns an interable whose elements come from applying f on the index and each corresponding elements of \*arg.
```
list(rc_func.map_indexed(lambda i, x: i + x, [2, 3, 4]))
# [2, 4, 6]
```

## l_map_indexed(f, \*args)

## l_str(xs, separator=", ", brackets="[]", end="\n")
* Parameter xs takes an iterable;
* Parameter separator takes a str;
* Parameter brackets tkae a str;
* Returns the string consists of each element of xs, separated by separator. If brackets contains two characters, then use them as brackets for the output.
```
list(rc_func.map_indexed(lambda i, x: i + x, [2, 3, 4]))
# <0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9>
<0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9>
```

## reduce_r(f, xs, initial=None)
* Parameter f takes a function that takes a parameter of type A and a parameter of type B;
* Parameter xs takes an iterable of type A;
* Parameter initial takes a value of type B or None;
* Returns the value results from applying f on the last element of xs and initial, then the second last element of xs and the previous result, and so on.
  * If initial is None, then treat the last element of xs as the initial and start from the second last and the last.
```
rc_func.reduce_r(lambda x, y: x + y, [1, 2, 3, 4, 5])
# 15 "1 + (2 + (3 + (4 + 5))))"
```

## scan(f, xs, initial=None)
* Parameter f takes a function that takes a parameter of type B and a parameter of type A;
* Parameter xs takes an iterable of type A;
* Parameter initial takes a value of type B or None;
* Returns an iterable whose first element is intial, second element is f(initial, xs[0]), third element is f(f(initial, xs[0]),, xs[1]), and so on.
  * Note that xs is not necessarily a list; here xs[0] only represents the first element this iterable would produce.
  * If initial is None, then start with f(xs[0, xs[1])
```
list(rc_func.scan(lambda x, y: x + y, [1, 2, 3, 4, 5], 100))
# [100, 101, 103, 106, 110, 115]
```

## l_scan(f, xs, initial=None)

## foreach(f, xs)
* Parameter f takes a function that takes a single parameter;
* Parameter xs takes an iterable;
* Applies f on the elements in xs from left to right;
* Returns None
```
rc_func.foreach(print, [1,2,3])
# 1
# 2
# 3
```

## foreach_indexed(f, xs)
* Parameter f takes a function that takes an index (int) and another parameter;
* Parameter xs takes an iterable;
* Applies f on the index of elements in xs and the elements themselves from left to right;
* Returns None
```
rc_func.foreach_indexed(print, [1,2,3])
# 0 1
# 1 2
# 2 3
```

## apply(f, \*args)
* Same as f(\*args)

## filter_indexed(f, xs)
* Parameter f takes a function that takes an index (int) and returns a bool;
* Parameter xs takes an iterable to be filtered;
* Returns an iterable containing the elements x in xs where f(i, x) == True, i is the index of x.
```
list(rc_func.filter_indexed(lambda i, _: i % 3 == 0, [1, 1, 4, 5, 1, 4]))
# [1, 5]
```

## l_filter_indexed(f, xs)

## filter_acc(f, xs, acc=None)
* Parameter f takes a function taking an element from xs and an accumulator, returning a bool and the updated accumulator;
* Parameter xs takes an iterable to be filtered;
* Parameter acc takes the initial accumulator;
* Returns an iterable containing the elements x where f(x, acc)[0] == True;
* For more information, check the example within the code.

## l_filter_acc(f, xs, acc=None)

## l_takewhile(f, xs)

## l_dropwhile(f, xs)

## elvis(x, default)
* Returns x if x is not None; otherwise returns default.

## safe_apply(f, \*args, default=None)
* Applies f on \*args if none of them are None; otherwise returns default.
```
rc_func.safe_apply(lambda x, y: x + y, 1, 2, default=10)
# 3
rc_func.safe_apply(lambda x, y: x + y, None, 2, default=10)
# 10
```

Sorrowful T-Rex on 21 Dec. 2020
