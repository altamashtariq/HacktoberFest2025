# Questions

---

## 1. How would you optimize Eloquent performance for a high-traffic application with millions of records?

---

## 2. How do you use chunking vs cursor-based iteration when processing large datasets?

---

## 3. How does Laravel’s CSRF protection work internally?  
Can you explain the `VerifyCsrfToken` middleware?

---

## 4. Contains Duplicate

Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1

**Input:**  
nums = [1,2,3,1]


**Output:**  
true


**Explanation:**  
The element `1` occurs at indices 0 and 3.

---

### Example 2

**Input:**  
nums = [1,2,3,4]


**Output:**  
false


**Explanation:**  
All elements are distinct.

---

### Example 3

**Input:**  
nums = [1,1,1,3,3,4,3,2,4,2]


**Output:**  
true


---

## 5. Contains Duplicate II

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

### Example 1

**Input:**  
nums = [1,2,3,1], k = 3


**Output:**  
true


---

### Example 2

**Input:**  
nums = [1,0,1,1], k = 1


**Output:**  
true


---

### Example 3

**Input:**  
nums = [1,2,3,1,2,3], k = 2


**Output:**  
false


---

## 6. Contains Duplicate III

You are given an integer array `nums` and two integers `indexDiff` and `valueDiff`.  

Find a pair of indices `(i, j)` such that:  
- `i != j`  
- `abs(i - j) <= indexDiff`  
- `abs(nums[i] - nums[j]) <= valueDiff`  

Return `true` if such a pair exists, or `false` otherwise.

### Example 1

**Input:**  
nums = [1,2,3,1], indexDiff = 3, valueDiff = 0


**Output:**  
true


**Explanation:**  
We can choose `(i, j) = (0, 3)`.  
- `i != j` → 0 != 3  
- `abs(i - j) <= indexDiff` → abs(0 - 3) <= 3  
- `abs(nums[i] - nums[j]) <= valueDiff` → abs(1 - 1) <= 0

---

### Example 2

**Input:**  
nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3


**Output:**  
false


**Explanation:**  
After trying all possible pairs `(i, j)`, no pair satisfies all three conditions.