# Questions

---

## 1. How do you prevent the N+1 query problem in Eloquent relationships beyond just `with()`?

---

## 2. What are the differences between `sync`, `database`, `Redis`, and `Beanstalkd` queue drivers in Laravel?

---

## 3. How does queue worker retry handling work?  
What happens if a job keeps failing?

---

## 4. Write a logic for reversing a linked list.

---

## 5. Course Schedule Problem

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`.  

You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.  

For example, the pair `[0, 1]` indicates that to take course `0` you have to first take course `1`.  

Return `true` if you can finish all courses. Otherwise, return `false`.

### Example 1

**Input:**  
numCourses = 2, prerequisites = [[1,0]]


**Output:**  
true


**Explanation:**  
There are a total of 2 courses to take.  
To take course 1 you should have finished course 0. So it is possible.

---

### Example 2

**Input:**  
numCourses = 2, prerequisites = [[1,0],[0,1]]


**Output:**  
false


**Explanation:**  
There are a total of 2 courses to take.  
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

---

## 6. Minimum Size Subarray Sum

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`.  

If there is no such subarray, return `0` instead.

### Example 1

**Input:**  
target = 7, nums = [2,3,1,2,4,3]


**Output:**  
2


**Explanation:**  
The subarray `[4,3]` has the minimal length under the problem constraint.

---

### Example 2

**Input:**  
target = 4, nums = [1,4,4]


**Output:**  
1


---

### Example 3

**Input:**  
target = 11, nums = [1,1,1,1,1,1,1,1]


**Output:**  
0