# Coding Questions

---

## 1. Why Can’t Hooks Be Called Conditionally or Inside Loops?

---

## 2. How Does useLayoutEffect Differ from useEffect, and What Real-World Issues Arise if You Use the Wrong One?

---

## 3. Explain Why Updating State with a Stale Closure is a Common Bug with Hooks

---

## 4. Longest Valid Parentheses

Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

### Example 1:
- Input: `s = "(()"`  
- Output: `2`  
- Explanation: The longest valid parentheses substring is `"()"`.

### Example 2:
- Input: `s = ")()())"`  
- Output: `4`  
- Explanation: The longest valid parentheses substring is `"()()"`.

### Example 3:
- Input: `s = ""`  
- Output: `0`

---

## 5. First Missing Positive

Given an unsorted integer array `nums`, return the smallest positive integer that is not present in `nums`.  
Implement an algorithm that runs in **O(n)** time and uses **O(1)** auxiliary space.

### Example 1:
- Input: `nums = [1,2,0]`  
- Output: `3`  
- Explanation: The numbers in the range `[1,2]` are all in the array.

### Example 2:
- Input: `nums = [3,4,-1,1]`  
- Output: `2`  
- Explanation: 1 is in the array but 2 is missing.

### Example 3:
- Input: `nums = [7,8,9,11,12]`  
- Output: `1`  
- Explanation: The smallest positive integer 1 is missing.

---

## 6. Wildcard Pattern Matching

Given an input string `s` and a pattern `p`, implement wildcard pattern matching with support for `'?'` and `'*'`:

- `'?'` Matches any single character.  
- `'*'` Matches any sequence of characters (including the empty sequence).  
- The matching should cover the entire input string (not partial).

### Example 1:
- Input: `s = "aa"`, `p = "a"`  
- Output: `false`  
- Explanation: `"a"` does not match the entire string `"aa"`.

### Example 2:
- Input: `s = "aa"`, `p = "*"`  
- Output: `true`  
- Explanation: `'*'` matches any sequence.

### Example 3:
- Input: `s = "cb"`, `p = "?a"`  
- Output: `false`  
- Explanation: `'?'` matches `'c'`, but the second letter `'a'` does not match `'b'`.
---
