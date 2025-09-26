# Questions

---

## 1. How does Laravel handle request lifecycle from HTTP request to response?  
(Explain middleware stack, kernel, and dispatcher).

---

## 2. What is the difference between singleton binding and scoped binding in the service container?

---

## 3. How do you implement polymorphic many-to-many relationships in Eloquent?  
Provide a real-world example.

---

## 4. Given a text file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

You may assume that a valid phone number must appear in one of the following two formats:  
- `(xxx) xxx-xxxx`  
- `xxx-xxx-xxxx`  

(x means a digit)

You may also assume each line in the text file must not contain leading or trailing white spaces.

### Example

Assume that `file.txt` has the following content:

987-123-4567
123 456 7890
(123) 456-7890


**Output:**
987-123-4567
(123) 456-7890


---

## 5. Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.  
You may assume all four edges of the grid are surrounded by water.

### Example 1

**Input:**
grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]


**Output:**
1


---

### Example 2

**Input:**
grid = [
["1","1","0","0","0"],
["1","1","0","0","0"],
["0","0","1","0","0"],
["0","0","0","1","1"]
]


**Output:**
3


---

## 6. Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.

### Example 1

**Input:**
left = 5, right = 7


**Output:**
4


---

### Example 2

**Input:**
left = 0, right = 0


**Output:**
0


---

### Example 3

**Input:**
left = 1, right = 2147483647


**Output:**
0
