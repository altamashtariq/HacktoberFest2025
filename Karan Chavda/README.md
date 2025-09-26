# Coding Questions

## 1. How does code-splitting with React.lazy and Suspense work internally?

Explain how **React.lazy** and **Suspense** enable code-splitting. Discuss what happens internally when a component is loaded lazily, including how the rendering process is suspended until the module is fetched.

## 2. Why does React.StrictMode intentionally double-invoke certain lifecycle methods and effects in development?

Explain the reasoning behind **React.StrictMode** double-invoking lifecycle methods and effects during development. Include discussion on detecting side effects, potential pitfalls, and benefits for debugging.

## 3. What is prop drilling, and what are the architectural alternatives to avoid it?

- Define **prop drilling** in React applications.
- Discuss problems caused by deeply passing props through multiple layers.
- List architectural alternatives such as **Context API**, **Redux**, or **custom hooks** to avoid prop drilling.

## 4. Scrambled String

We can scramble a string `s` to get a string `t` using the following algorithm:

1. If the length of the string is 1, stop.
2. If the length of the string is > 1, do the following:
   - Split the string into two non-empty substrings at a random index. If the string is `s`, divide it into `x` and `y` where `s = x + y`.
   - Randomly decide to swap the two substrings or to keep them in the same order. After this step, `s` may become `s = x + y` or `s = y + x`.
   - Apply step 1 recursively on each of the two substrings `x` and `y`.
   
Given two strings `s1` and `s2` of the same length, return **true** if `s2` is a scrambled string of `s1`, otherwise return **false**.

### Example 1:
- Input:
s1 = "great", s2 = "rgeat"

- Output:
true

- Explanation: One possible scenario applied on `s1`:
  - "great" → "gr/eat" (divide at random index)
  - "gr/eat" → "gr/eat" (no swap)
  - "gr/eat" → "g/r / e/at" (divide recursively)
  - "g/r / e/at" → "r/g / e/at" (swap first substring)
  - "r/g / e/at" → "r/g / e/ a/t" (divide "at")
  - "r/g / e/ a/t" → "r/g / e/ a/t" (no swap)
  - Resulting string: `"rgeat"` which matches `s2`.

### Example 2:
- Input:
s1 = "abcde", s2 = "caebd"

- Output:
false


### Example 3:
- Input:
s1 = "a", s2 = "a"

- Output:
true


## 5. Distinct Subsequences

Given two strings `s` and `t`, return the number of **distinct subsequences** of `s` which equal `t`.

- The test cases are generated so that the answer fits in a 32-bit signed integer.

### Example 1:
- Input:
s = "rabbbit", t = "rabbit"

- Output:
3

- Explanation: There are 3 ways to generate `"rabbit"` from `s`:
  1. `"rab"bb"it"`
  2. `"ra"b"bbit"`
  3. `"rab"b"bit"`

### Example 2:
- Input:
s = "babgbag", t = "bag"

- Output:
5

- Explanation: There are 5 ways to generate `"bag"` from `s`:
  1. `"ba"b"g"bag`
  2. `"ba"bgba"g"`
  3. `"b"abgb"ag"`
  4. `ba"b"gb"ag"`
  5. `babg"bag"`

## 6. Maximum Profit with At Most Two Transactions

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day. Find the **maximum profit** you can achieve. You may complete at most **two transactions**.

- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### Example 1:
- Input:
prices = [3,3,5,0,0,3,1,4]

- Output:
6

- Explanation:
  - Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3.
  - Buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 3.
  - Total profit = 6.

### Example 2:
- Input:
prices = [1,2,3,4,5]

- Output:
4

- Explanation:
  - Buy on day 1 and sell on day 5, profit = 4.
  - Note: You cannot hold multiple transactions at the same time.

### Example 3:
- Input:
prices = [7,6,4,3,1]

- Output:
0

- Explanation: No transaction is done, so max profit = 0.