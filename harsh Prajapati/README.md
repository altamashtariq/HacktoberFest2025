# Coding Questions

---

## 1. Why Can React Context Cause Unnecessary Re-renders, and How Do You Prevent That?

---

## 2. Why Is It Often Recommended to Split Large Contexts into Multiple Smaller Contexts?

---

## 3. Compare React Context with Redux: What Problems Does Each Solve Differently?

---

## 4. N-Queens Puzzle – Count Distinct Solutions

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.  

Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.

### Example 1:
- Input: `n = 4`  
- Output: `2`  
- Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

### Example 2:
- Input: `n = 1`  
- Output: `1`

---

## 5. Kth Permutation Sequence

The set `[1, 2, 3, ..., n]` contains a total of `n!` unique permutations.  
By listing all permutations in order, return the kth permutation sequence given `n` and `k`.

### Example 1:
- Input: `n = 3, k = 3`  
- Output: `"213"`

### Example 2:
- Input: `n = 4, k = 9`  
- Output: `"2314"`

### Example 3:
- Input: `n = 3, k = 1`  
- Output: `"123"`

---

## 6. Validate Number

Given a string `s`, return whether `s` is a valid number.

**Valid numbers include:** `"2"`, `"0089"`, `"-0.1"`, `"+3.14"`, `"4."`, `"-.9"`, `"2e10"`, `"-90E3"`, `"3e+7"`, `"+6e-1"`, `"53.5e93"`, `"-123.456e789"`  
**Invalid numbers include:** `"abc"`, `"1a"`, `"1e"`, `"e3"`, `"99e2.5"`, `"--6"`, `"-+3"`, `"95a54e53"`

**Definitions:**
- An integer number followed by an optional exponent.
- A decimal number followed by an optional exponent.
- An integer: optional sign `'-'` or `'+'` followed by digits.
- A decimal: optional sign `'-'` or `'+'` followed by:
  - digits followed by `.`  
  - digits followed by `.` and more digits  
  - `.` followed by digits
- Exponent: `'e'` or `'E'` followed by an integer number.

**Examples:**

### Example 1:
- Input: `s = "0"`  
- Output: `true`

### Example 2:
- Input: `s = "e"`  
- Output: `false`

### Example 3:
- Input: `s = "."`  
- Output: `false`

---
