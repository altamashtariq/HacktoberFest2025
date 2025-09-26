# Coding Questions

## 1. How does React’s useReducer differ from Redux reducers in terms of execution and scope?

Explain the differences in execution context, state management, and scope between **React’s `useReducer`** and **Redux reducers**.

## 2. Why can passing callbacks through props sometimes be better than using context?

Discuss scenarios where passing callbacks via props is preferred over using **React Context**, including performance and component isolation considerations.

## 3. Explain the concept of controlled vs uncontrolled components and when uncontrolled components may be preferable.

- Define **controlled** and **uncontrolled components** in React.
- Explain the differences in how state is managed.
- Provide situations where **uncontrolled components** are more suitable.

## 4. Text Justification

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

- You should pack your words in a **greedy approach**; that is, pack as many words as you can in each line.
- Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.
- Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
- For the last line of text, it should be **left-justified**, and no extra space is inserted between words.

**Note:**
- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed `maxWidth`.
- The input array `words` contains at least one word.

### Example 1:
- Input:
words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

- Output:
[
"This is an",
"example of text",
"justification. "
]


### Example 2:
- Input:
words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16

- Output:
[
"What must be",
"acknowledgment ",
"shall be "
]

- Explanation: 
  - The last line is left-justified: `"shall be    "`.
  - A line with only one word is also left-justified.

### Example 3:
- Input:
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20

- Output:
[
"Science is what we",
"understand well",
"enough to explain to",
"a computer. Art is",
"everything else we",
"do "
]


## 5. Minimum Window Substring

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring** of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `""`.

- The test cases will be generated such that the answer is **unique**.

### Example 1:
- Input:
s = "ADOBECODEBANC", t = "ABC"

- Output:
"BANC"

- Explanation: The minimum window substring `"BANC"` includes 'A', 'B', and 'C' from string `t`.

### Example 2:
- Input:
s = "a", t = "a"

- Output:
"a"

- Explanation: The entire string `s` is the minimum window.

### Example 3:
- Input:
s = "a", t = "aa"

- Output:
""

- Explanation: Both 'a's from `t` must be included in the window. Since the largest window of `s` only has one 'a', return empty string.

## 6. Maximal Rectangle in Binary Matrix

Given a `rows x cols` binary matrix filled with 0's and 1's, find the **largest rectangle containing only 1's** and return its area.

### Example 1:
- Input:
matrix = [
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]

- Output:
6

- Explanation: The maximal rectangle is shown in the above picture.

### Example 2:
- Input:
matrix = [["0"]]

- Output:
0


### Example 3:
- Input:
matrix = [["1"]]

- Output:
1
