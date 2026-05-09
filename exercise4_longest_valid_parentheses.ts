import assert from "node:assert";

export function longestValidParentheses(s: string): number {
    let maxLen = 0;
    const stack: number[] = [-1];

    for (let i = 0; i < s.length; i++) {
        if (s[i] === '(') {
            stack.push(i);
        } else {
            stack.pop();
            if (stack.length === 0) {
                stack.push(i);
            } else {
                maxLen = Math.max(maxLen, i - stack[stack.length - 1]);
            }
        }
    }

    return maxLen;
}

// --- Tests ---
assert.strictEqual(longestValidParentheses("(()"), 2);
assert.strictEqual(longestValidParentheses(")()())"), 4);
assert.strictEqual(longestValidParentheses(""), 0);
assert.strictEqual(longestValidParentheses("()(()"), 2);
assert.strictEqual(longestValidParentheses("(()())"), 6);
console.log("Exercise 4 tests passed successfully!");
