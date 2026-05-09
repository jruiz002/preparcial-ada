def fib(n: int) -> int:
    if n <= 1:
        return n
        
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        
    return b

# --- Tests ---
if __name__ == "__main__":
    tests = [
        (0, 0),
        (1, 1),
        (10, 55),
        (30, 832040)
    ]
    for n, expected in tests:
        result = fib(n)
        assert result == expected, f"Failed for fib({n}). Expected {expected}, got {result}"
        print(f"Passed: fib({n}) == {result}")
    print("All Exercise 2 tests passed successfully!")
