# Coding Questions

## 1. Why does React 18 introduce automatic batching, and how does it change behavior compared to older versions?

Explain the purpose of **automatic batching** in React 18 and how it allows multiple state updates to be grouped together automatically. Discuss differences compared to React 17 and earlier versions where batching was limited to certain contexts (like event handlers).

## 2. How does React prevent tearing in concurrent rendering when using shared state?

Describe how React manages **concurrent rendering** to prevent tearing, ensuring that shared state is consistent across multiple updates. Include discussion of techniques like **state lanes** and **prioritized updates**.

## 3. What is the difference between blocking rendering and interruptible rendering, and why does it matter for user experience?

- Define **blocking rendering** (synchronous rendering) and **interruptible rendering** (concurrent rendering).
- Explain why interruptible rendering improves **responsiveness** and **perceived performance**.
- Provide examples of situations where blocking rendering can cause jank.

## 4. Word Break II

Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

- Note: The same word in the dictionary may be reused multiple times in the segmentation.

### Example 1:
- Input:
s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]

- Output:
["cats and dog", "cat sand dog"]


### Example 2:
- Input:
s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]

- Output:
["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]

- Explanation: Dictionary words can be reused.

### Example 3:
- Input:
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]

- Output:
[]


## 5. Find Minimum in Rotated Sorted Array II

Suppose an array of length `n` sorted in ascending order is rotated between 1 and `n` times. For example:

- `[0,1,4,4,5,6,7]` might become `[4,5,6,7,0,1,4]` if rotated 4 times.
- Rotating `[a[0], a[1], ..., a[n-1]]` 1 time results in `[a[n-1], a[0], ..., a[n-2]]`.

Given the sorted rotated array `nums` that **may contain duplicates**, return the **minimum element** of the array. Optimize for the fewest operation steps.

### Example 1:
- Input:
nums = [1,3,5]

- Output:
1


### Example 2:
- Input:
nums = [2,2,2,0,1]

- Output:
0


## 6. Maximum Profit with At Most k Transactions

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day, and an integer `k`. Find the **maximum profit** you can achieve. You may complete at most `k` transactions (buy at most `k` times and sell at most `k` times).

- Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

### Example 1:
- Input:
k = 2, prices = [2,4,1]

- Output:
2

- Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 2.

### Example 2:
- Input:
k = 2, prices = [3,2,6,5,0,3]

- Output:
7

- Explanation: 
  - Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 4.
  - Buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3.
  - Total profit = 7.