# Coding Questions

---

## 1. How Do Keys Affect the Reconciliation Process, and Why Might Using Array Indices as Keys Cause Bugs?

---

## 2. How Does React Internally Keep Track of Multiple useState and useEffect Calls Within the Same Component?

---

## 3. Explain the Difference Between Mounting Effects vs Updating Effects in React’s Hook System

---

## 4. Write a Logic for Sudoku Solver

---

## 5. N-Queens Puzzle

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.  

Given an integer `n`, return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively. You may return the answer in any order.

### Example 1:
- Input: `n = 4`  
- Output: `[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]`  
- Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

### Example 2:
- Input: `n = 1`  
- Output: `[["Q"]]`

---

## 6. Find All Concatenated Substrings

You are given a string `s` and an array of strings `words`. All strings in `words` are of the same length.  

A concatenated string is a string that exactly contains all the strings of any permutation of `words` concatenated.  

Return an array of the starting indices of all concatenated substrings in `s`. You may return the answer in any order.

### Example 1:
- Input: `s = "barfoothefoobarman"`, `words = ["foo","bar"]`  
- Output: `[0,9]`  
- Explanation: The substring starting at 0 is `"barfoo"` (permutation of `["bar","foo"]`). The substring starting at 9 is `"foobar"` (permutation of `["foo","bar"]`).

### Example 2:
- Input: `s = "wordgoodgoodgoodbestword"`, `words = ["word","good","best","word"]`  
- Output: `[]`  
- Explanation: There is no concatenated substring.

### Example 3:
- Input: `s = "barfoofoobarthefoobarman"`, `words = ["bar","foo","the"]`  
- Output: `[6,9,12]`  
- Explanation: 
  - Substring starting at 6: `"foobarthe"`  
  - Substring starting at 9: `"barthefoo"`  
  - Substring starting at 12: `"thefoobar"`

---
