# Coding Questions

---

## 1. Why Does React Use the Virtual DOM Instead of Directly Manipulating the Real DOM, and What Are Its Trade-offs?

---

## 2. What Are Render Phases and Commit Phases in React Fiber?

---

## 3. Why Is React’s Rendering Not Always "Fast," and What Kind of Operations Can Still Make React Apps Slow?

---

## 4. Convert Integer to Roman Numeral

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| :--- | :--- |
| I | 1 |
| V | 5 |
| X | 10 |
| L | 50 |
| C | 100 |
| D | 500 |
| M | 1000 |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol (e.g., 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX). Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), 900 (CM).
- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times, use the subtractive form.

### Example 1:
- Input: `num = 3749`  
- Output: `"MMMDCCXLIX"`

### Example 2:
- Input: `num = 58`  
- Output: `"LVIII"`

### Example 3:
- Input: `num = 1994`  
- Output: `"MCMXCIV"`

---

## 5. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.  
If there is no common prefix, return an empty string `""`.

### Example 1:
- Input: `strs = ["flower","flow","flight"]`  
- Output: `"fl"`

### Example 2:
- Input: `strs = ["dog","racecar","car"]`  
- Output: `""`  
- Explanation: There is no common prefix among the input strings.

---

## 6. Three Sum Problem

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets.

### Example 1:
- Input: `nums = [-1,0,1,2,-1,-4]`  
- Output: `[[-1,-1,2],[-1,0,1]]`

### Example 2:
- Input: `nums = [0,1,1]`  
- Output: `[]`

### Example 3:
- Input: `nums = [0,0,0]`  
- Output: `[[0,0,0]]`

---
