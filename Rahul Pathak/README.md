# Questions

---

## 1. How do you implement custom validation rules using the Validator class and Rule objects?

---

## 2. What’s the difference between feature tests and unit tests in Laravel?  
When is Dusk preferable?

---

## 3. How would you design a multi-tenancy system in Laravel?  
(separate DB per tenant vs shared DB with `tenant_id`)

---

## 4. Basic Calculator I

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it and return the result.  

> Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as `eval()`.

### Example 1

**Input:**  
s = "1 + 1"


**Output:**  
2


---

### Example 2

**Input:**  
s = " 2-1 + 2 "


**Output:**  
3


---

### Example 3

**Input:**  
s = "(1+(4+5+2)-3)+(6+8)"


**Output:**  
23


---

## 5. Implement a Stack using Two Queues

Implement a last-in-first-out (LIFO) stack using only **two queues**.  
The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:  

- `void push(int x)` Pushes element `x` to the top of the stack.  
- `int pop()` Removes the element on the top of the stack and returns it.  
- `int top()` Returns the element on the top of the stack.  
- `boolean empty()` Returns `true` if the stack is empty, `false` otherwise.  

**Notes:**  
- You must use only standard operations of a queue (push to back, peek/pop from front, size, and isEmpty).  
- You may simulate a queue using a list or deque if necessary.

### Example

**Input:**  
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]


**Output:**  
[null, null, null, 2, 2, false]


**Explanation:**  
```text
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // returns 2
myStack.pop(); // returns 2
myStack.empty(); // returns False
6. Basic Calculator II
Given a string s which represents an expression, evaluate the expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid.

All intermediate results will be in the range of [-2³¹, 2³¹ - 1].

You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1
Input:

s = "3+2*2"
Output:
7
Example 2
Input:

s = " 3/2 "
Output:
1
Example 3
Input:

s = " 3+5 / 2 "
Output:
5

If you want, I can **compile all your Laravel and coding question sets into a single, fully formatted Markdown document** for a complete interview-ready collection. This would include theoretical questions, algorithms, and data structure problems together. Do you want me to do that?