# Coding Questions

## 1. Explain how server-side rendering (SSR) works in React and what hydration problems might occur.

Discuss how **SSR** generates HTML on the server and sends it to the client. Explain potential **hydration issues**, such as mismatches between server-rendered markup and client-rendered React components.

## 2. What is React’s transition API (startTransition), and how does it help with prioritizing updates?

Explain how **startTransition** allows certain updates to be marked as low-priority, enabling React to keep the UI responsive while rendering non-urgent updates in the background.

## 3. Explain how Suspense for data fetching differs from Suspense for lazy-loaded components.

- Discuss the difference between **data fetching Suspense** (waiting for asynchronous data) and **component lazy-loading Suspense** (waiting for dynamic import of components).
- Highlight differences in usage, rendering behavior, and fallback handling.

## 4. Word Ladder II (Transformation Sequence)

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`.

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return **all the shortest transformation sequences** from `beginWord` to `endWord`, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words `[beginWord, s1, s2, ..., sk]`.

### Example 1:
- Input:
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]

- Output:
[["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]

- Explanation:
  - Two shortest transformation sequences exist:
    1. `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`
    2. `"hit" -> "hot" -> "lot" -> "log" -> "cog"`

### Example 2:
- Input:
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]

- Output:
[]

- Explanation: The `endWord` `"cog"` is not in `wordList`, so no valid sequence exists.

## 5. Palindrome Partitioning (Minimum Cuts)

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return the **minimum cuts** needed for a palindrome partitioning of `s`.

### Example 1:
- Input:
s = "aab"

- Output:
1

- Explanation: The palindrome partitioning `["aa","b"]` requires 1 cut.

### Example 2:
- Input:
s = "a"

- Output:
0


### Example 3:
- Input:
s = "ab"

- Output:
1


## 6. Candy Distribution

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`. You need to distribute candies to these children subject to:

- Each child must have at least **one candy**.
- Children with a **higher rating** get more candies than their neighbors.

Return the **minimum number of candies** needed to satisfy these conditions.

### Example 1:
- Input:
ratings = [1,0,2]

- Output:
5

- Explanation: Allocate candies `[2,1,2]` to the children.

### Example 2:
- Input:
ratings = [1,2,2]

- Output:
4

- Explanation: Allocate candies `[1,2,1]`. The third child gets 1 candy because the higher-rated neighbor rule is satisfied.