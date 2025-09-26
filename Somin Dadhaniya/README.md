# Questions

---

## 1. How does Laravel’s Service Container resolve dependencies when multiple bindings exist for the same interface?

---

## 2. Explain how facades in Laravel work internally. How do they resolve underlying classes from the container?

---

## 3. What’s the difference between using `app()->make()`, dependency injection, and facades?

---

## 4. Reverse bits of a given 32 bits signed integer.

### Example 1

**Input:**  
n = 43261596


**Output:**  
964176192


**Explanation:**  

| Integer   | Binary                                |
|-----------|---------------------------------------|
| 43261596  | 00000010100101000001111010011100       |
| 964176192 | 00111001011110000010100101000000       |

---

### Example 2

**Input:**  
n = 2147483644


**Output:**  
1073741822


**Explanation:**  

| Integer    | Binary                                |
|------------|---------------------------------------|
| 2147483644 | 01111111111111111111111111111100       |
| 1073741822 | 00111111111111111111111111111110       |

---

## 5. Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### Example 1

**Input:**  
nums = [1,2,3,4,5,6,7], k = 3


**Output:**  
[5,6,7,1,2,3,4]


**Explanation:**  
- Rotate 1 step to the right: `[7,1,2,3,4,5,6]`  
- Rotate 2 steps to the right: `[6,7,1,2,3,4,5]`  
- Rotate 3 steps to the right: `[5,6,7,1,2,3,4]`

---

### Example 2

**Input:**  
nums = [-1,-100,3,99], k = 2


**Output:**  
[3,99,-1,-100]


**Explanation:**  
- Rotate 1 step to the right: `[99,-1,-100,3]`  
- Rotate 2 steps to the right: `[3,99,-1,-100]`

---

## 6. Given a positive integer `n`, write a function that returns the number of set bits in its binary representation (also known as the **Hamming weight**).

### Example 1

**Input:**  
n = 11


**Output:**  
3


**Explanation:**  
The input binary string `1011` has a total of three set bits.

---

### Example 2

**Input:**  
n = 128


**Output:**  
1


**Explanation:**  
The input binary string `10000000` has a total of one set bit.

---

### Example 3

**Input:**  
n = 2147483645


**Output:**  
30


**Explanation:**  
The input binary string `1111111111111111111111111111101` has a total of thirty set bits.