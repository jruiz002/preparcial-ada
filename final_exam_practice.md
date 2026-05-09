# Final Exam Practice: Coding challenge

---

## Exercise 1 (Python) — Improve This Algorithm

The function below finds all pairs in a list that sum to a target value.

```python
def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result.append((nums[i], nums[j]))
    return result
```

**Tasks:**
1. Analyze the time and space complexity of the implementation above.
2. Rewrite it to achieve O(n) time complexity.
3. Analyze the complexity of your new version.

**Tests:**
```python
assert sorted(find_pairs([2, 7, 4, 1, 3], 5)) == sorted([(2, 3), (4, 1)])
assert find_pairs([1, 2, 3], 10) == []
assert sorted(find_pairs([5, 5, 3, 7], 10)) == sorted([(5, 5), (3, 7)])
```

---

## Exercise 2 (Python) — Improve This Algorithm

The function below computes the n-th Fibonacci number.

```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

**Tasks:**
1. Analyze the time and space complexity of the implementation above.
2. Rewrite it using dynamic programming (bottom-up) to achieve O(n) time and O(1) space.
3. Analyze the complexity of your new version.

**Tests:**
```python
assert fib(0) == 0
assert fib(1) == 1
assert fib(10) == 55
assert fib(30) == 832040
```

---

## Exercise 3 (Python) — Write the Algorithm

Given a list of non-negative integers representing histogram bar heights (each bar has width 1), compute the area of the largest rectangle that fits entirely within the histogram.

**Input:** `heights: list[int]`  
**Output:** `int`

**Constraints:** O(n) time required. Include a brief justification of your approach and its complexity.

**Tests:**
```python
assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle([2, 4]) == 4
assert largest_rectangle([1]) == 1
assert largest_rectangle([0, 0, 0]) == 0
assert largest_rectangle([6, 2, 5, 4, 5, 1, 6]) == 12
```

---

## Exercise 4 (TypeScript) — Write the Algorithm

Given a string `s` containing only `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.

**Input:** `s: string`  
**Output:** `number`

**Constraints:** O(n) time required. Include a brief justification of your approach and its complexity.

**Tests (using Node.js `assert`):**
```typescript
import assert from "node:assert";

assert.strictEqual(longestValidParentheses("(()"), 2);
assert.strictEqual(longestValidParentheses(")()())"), 4);
assert.strictEqual(longestValidParentheses(""), 0);
assert.strictEqual(longestValidParentheses("()(()"), 2);
assert.strictEqual(longestValidParentheses("(()())"), 6);
```

## Exercise 5 — Data Structure Selection

A real-time multiplayer game needs to display a live leaderboard. Players' scores update frequently (multiple times per second), and the system must always be able to instantly retrieve the top 10 players. The player base can grow to hundreds of thousands of users.

**Task:** Choose a data structure (or combination of structures) to support this system. Your answer must address:

1. Which data structure(s) you would use and why.
2. The time complexity of a score update and a top-10 query under your design.
3. One concrete tradeoff your choice introduces and how you would handle it.

There is no single correct answer. Grading is based on the clarity of your reasoning and the coherence between your choice and the constraints.

---

## Exercise 6 — Algorithm Selection

You are building a navigation feature for a delivery app. The app operates in a mid-sized city and must compute the fastest route between two locations on a road network. The network has around 50,000 intersections and 120,000 road segments. Each segment has a travel time that can change throughout the day (rush hour, incidents). Routes are requested continuously by many drivers at the same time.

**Task:** Choose an algorithm or algorithmic strategy to handle route computation. Your answer must address:

1. Which algorithm you would use and why it fits this scenario.
2. How you would handle the fact that edge weights change over time.
3. One alternative algorithm you considered and why you ruled it out.

There is no single correct answer. Grading is based on the clarity of your reasoning and the coherence between your choice and the constraints.