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
const tests = [
    { input: "(()", expected: 2 },
    { input: ")()())", expected: 4 },
    { input: "", expected: 0 },
    { input: "()(()", expected: 2 },
    { input: "(()())", expected: 6 }
];

for (const { input, expected } of tests) {
    const result = longestValidParentheses(input);
    assert.strictEqual(result, expected, `Failed for input "${input}". Expected ${expected}, got ${result}`);
    console.log(`Passed: longestValidParentheses("${input}") === ${result}`);
}
console.log("All Exercise 4 tests passed successfully!");
