# Questions

---

## 1. What’s the difference between using Redis as a cache vs Redis as a session/store driver in Laravel?

---

## 2. How do you implement cache tags in Laravel?  
When should they be avoided?

---

## 3. Explain the difference between route caching, config caching, and view caching.  
What pitfalls can occur with each?

---

## 4. Shortest Palindrome

You are given a string `s`. You can convert `s` to a palindrome by adding characters in front of it.  

Return the shortest palindrome you can find by performing this transformation.

### Example 1

**Input:**  
s = "aacecaaa"


**Output:**  
"aaacecaaa"


---

### Example 2

**Input:**  
s = "abcd"


**Output:**  
"dcbabcd"


---

## 5. Kth Largest Element in an Array

Given an integer array `nums` and an integer `k`, return the `k`th largest element in the array.  

> Note: It is the `k`th largest element in sorted order, not the `k`th distinct element.  
> Try to solve it without sorting.

### Example 1

**Input:**  
nums = [3,2,1,5,6,4], k = 2


**Output:**  
5


---

### Example 2

**Input:**  
nums = [3,2,3,1,2,4,5,5,6], k = 4


**Output:**  
4


---

## 6. Combination Sum III

Find all valid combinations of `k` numbers that sum up to `n` such that the following conditions are true:

- Only numbers 1 through 9 are used.  
- Each number is used at most once.  
- Return a list of all possible valid combinations. The list must not contain duplicate combinations.  
- Combinations may be returned in any order.

### Example 1

**Input:**  
k = 3, n = 7


**Output:**  
[[1,2,4]]


**Explanation:**  
1 + 2 + 4 = 7. There are no other valid combinations.

---

### Example 2

**Input:**  
k = 3, n = 9


**Output:**  
[[1,2,6],[1,3,5],[2,3,4]]


**Explanation:**  
- 1 + 2 + 6 = 9  
- 1 + 3 + 5 = 9  
- 2 + 3 + 4 = 9  

No other valid combinations exist.

---

### Example 3

**Input:**  
k = 4, n = 1


**Output:**  
[]


**Explanation:**  
The smallest sum using 4 different numbers in the range [1,9] is 1 + 2 + 3 + 4 = 10.  
Since 10 > 1, there are no valid combinations.