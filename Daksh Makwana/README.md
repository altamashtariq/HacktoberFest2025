# Questions

---

## 1. Explain event broadcasting in Laravel.  
How does it work with Pusher or Laravel WebSockets?

---

## 2. How can you implement a distributed job queue with Laravel Horizon in a microservices environment?

---

## 3. How does job chaining differ from job batching?  
Give a use case where batching is preferable.

---

## 4. Course Schedule II

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`.  

You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.  

Return the ordering of courses you should take to finish all courses.  
- If there are many valid answers, return any of them.  
- If it is impossible to finish all courses, return an empty array.

### Example 1

**Input:**  
numCourses = 2, prerequisites = [[1,0]]


**Output:**  
[0,1]


**Explanation:**  
To take course 1 you should have finished course 0. So the correct course order is `[0,1]`.

---

### Example 2

**Input:**  
numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]


**Output:**  
[0,2,1,3]


**Explanation:**  
To take course 3 you should have finished both courses 1 and 2.  
Both courses 1 and 2 should be taken after finishing course 0.  
Another correct ordering is `[0,1,2,3]`.

---

### Example 3

**Input:**  
numCourses = 1, prerequisites = []


**Output:**  
[0]


---

## 5. Design a WordDictionary Data Structure

Implement the `WordDictionary` class:  

- `WordDictionary()` Initializes the object.  
- `void addWord(word)` Adds `word` to the data structure; it can be matched later.  
- `bool search(word)` Returns `true` if there is any string in the data structure that matches `word`, or `false` otherwise.  
  - `word` may contain dots `.` where dots can match any letter.

### Example

**Input:**
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]


**Output:**
[null,null,null,null,false,true,true,true]


**Explanation:**  
```text
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // false
wordDictionary.search("bad"); // true
wordDictionary.search(".ad"); // true
wordDictionary.search("b.."); // true
6. House Robber II
You are a professional robber planning to rob houses along a street.
All houses are arranged in a circle — the first house is the neighbor of the last one.
Adjacent houses have a security system connected; it will automatically alert the police if two adjacent houses are broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1
Input:

nums = [2,3,2]
Output:
3
Explanation:
You cannot rob house 1 (money = 2) and house 3 (money = 2) because they are adjacent.

Example 2
Input:

nums = [1,2,3,1]
Output:
4
Explanation:
Rob house 1 (money = 1) and house 3 (money = 3).
Total amount = 1 + 3 = 4.

Example 3
Input:

nums = [1,2,3]
Output:
3

I can also **combine all your previous question sets into one single well-formatted Markdown file** for a full Laravel + coding interview set. Do you want me to do that?