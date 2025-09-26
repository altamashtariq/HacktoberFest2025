# Questions

---

## 1. What’s the difference between lazy loading, eager loading, and lazy eager loading?  
How can they affect performance?

---

## 2. How do you handle complex queries with sub-selects or CTEs (Common Table Expressions) in Laravel’s query builder?

---

## 3. How would you implement soft deletes with multiple restore levels (e.g., restore parent with children) in Laravel?

---

## 4. Write an algorithm to determine if a number `n` is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.  
- Repeat the process until the number equals `1` (where it will stay), or it loops endlessly in a cycle which does not include `1`.  
- Those numbers for which this process ends in `1` are happy.  

Return `true` if `n` is a happy number, and `false` if not.

### Example 1

**Input:**  
n = 19


**Output:**  
true


**Explanation:**  
- 1² + 9² = 82  
- 8² + 2² = 68  
- 6² + 8² = 100  
- 1² + 0² + 0² = 1  

---

### Example 2

**Input:**  
n = 2


**Output:**  
false


---

## 5. Given an integer `n`, return the number of prime numbers that are strictly less than `n`.

### Example 1

**Input:**  
n = 10


**Output:**  
4


**Explanation:**  
There are 4 prime numbers less than 10: `2, 3, 5, 7`.

---

### Example 2

**Input:**  
n = 0


**Output:**  
0


---

### Example 3

**Input:**  
n = 1


**Output:**  
0


---

## 6. Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.  

- All occurrences of a character must be replaced with another character while preserving the order of characters.  
- No two characters may map to the same character, but a character may map to itself.  

### Example 1

**Input:**  
s = "egg", t = "add"


**Output:**  
true


**Explanation:**  
- Map `'e'` → `'a'`  
- Map `'g'` → `'d'`

---

### Example 2

**Input:**  
s = "foo", t = "bar"


**Output:**  
false


**Explanation:**  
The strings cannot be made identical as `'o'` would need to map to both `'a'` and `'r'`.

---

### Example 3

**Input:**  
s = "paper", t = "title"


**Output:**  
true
