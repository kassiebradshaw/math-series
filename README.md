# Lab 02 - Modules & Testing

**Author**: Kassie Bradshaw

**Version**: 1.0.0

## Overview

The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55`

* Note: When asking for the `nth` number in a series, presume starting at zero.
  * `Fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1`, etc.

The Lucas Numbers are a related series of integers that start with the values 2 and 1 rther than 0 and 1. The resulting series looks like this: `2, 1, 3, 4, 7, 11, 18, 29, 47`

## Change Log

### [Link to PR on GitHub]

06-08-21:

* Wrote tests:
  * `test_fibonacci_function`
  * `test_fibonacci_wrong`
  * `test_lucas_function`
  * `test_lucas_wrong`
* Wrote functions `fibonacci` & `lucas`

06-09-21:

* Wrote tests:
  * `test_fibonacci_zerio`
  * `test_fibonacci_one`
  * `test_fibonacci_two`
  * `test_fibonacci_ten`
  * `test_lucas_two`
  * `test_lucas_nine`
  * `test_sum_series_function`
  * `test_sum_series_fail`
  * `test_sum_series_no_optional_params`
  * `test_sum_series_lucas_params`
  * `test_sum_series_random_optional_params`
* Modified `fibonacci` & `lucas` functions to pass the tests  
* Wrote `sum_series` function & modified to enable tests to pass.

## Collaboration & Credit

* Got help from TAs Anthony Beaver & Ben Hill
* Collaborated in Remo with:
  * Anthony Williams
  * Kevin Henry
  * Michael Hendricks
  * Garfield Grant

* [Code reference for help with Fibonacci sequence](https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/)

* [Code reference for help with Lucas numbers](https://www.geeksforgeeks.org/lucas-numbers/)
