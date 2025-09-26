# Coding Questions

---

## 1. What is React Fiber, and How Does it Improve Rendering Compared to the Older Stack Reconciler?

---

## 2. Explain the Difference Between Synchronous Rendering and Concurrent Rendering in React

---

## 3. How Does React’s Reconciliation Algorithm Determine Whether to Update, Reuse, or Discard a Component Subtree?

---

## 4. Split an Array of Integers into Two Parts

**Problem:**  
Given an array of integers, split it into two parts.  
Return two arrays as a result.  
You may decide how to split the array based on its values.

### Example 1:
- Input: `[23, 87, 45, 12, 56, 78, 34]`  
- Output: `[23, 45, 12, 34], [87, 56, 78]`

### Example 2:
- Input: `[5, 99, 12, 37, 64, 20, 50, 8]`  
- Output: `[5, 12, 37, 20, 8], [99, 64, 50]`

### Example 3:
- Input: `[88, 14, 72, 9, 55, 41, 63, 30]`  
- Output: `[14, 9, 41, 30], [88, 72, 55, 63]`

---

## 5. Solve a System of Two Linear Equations

**Problem:**  
Write a program that can solve any system of two linear equations with two variables `x` and `y`.

The general form is:  
a1x + b1y = c1
a2x + b2y = c2

markdown
Copy code

**Requirements:**
- Take six numbers as input: `a1, b1, c1, a2, b2, c2`.  
- Solve for `x` and `y` (e.g., using Cramer’s Rule).  
- Print in the format:  
x = <value>
y = <value>

- Handle cases with no unique solution (parallel or same lines).

### Example 1:
- Input: `a1 = 2, b1 = 3, c1 = 12, a2 = 3, b2 = 2, c2 = 13`  
- Output:  
x = 3.0
y = 2.0

### Example 2 (No unique solution):
- Input: `a1 = 2, b1 = 4, c1 = 8, a2 = 1, b2 = 2, c2 = 4`  
- Output:  
No unique solution (lines may be parallel or same)


---

## 6. Extract Letters from Words and Sort

**Problem:**  
From the list of words, create a list of the letters that make up those words.  
Also, sort the resulting list.

### Example 1:
- Input: `words = ["cat","dog","bat","rat"]`  
- Output: `["c","a","t","d","o","g","b","r"]`

### Example 2:
- Input: `words = ["elephant","Lion","Call","puppy"]`  
- Output: `["e","l","e","p","h","a","n","t","i","o","n","c","l","u","p","y"]`

---