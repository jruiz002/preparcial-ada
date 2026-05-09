def largest_rectangle(heights: list[int]) -> int:
    stack = []  # stores indices
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        h = heights[i] if i < n else 0
        
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        stack.append(i)
        
    return max_area

# --- Tests ---
if __name__ == "__main__":
    assert largest_rectangle([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle([2, 4]) == 4
    assert largest_rectangle([1]) == 1
    assert largest_rectangle([0, 0, 0]) == 0
    assert largest_rectangle([6, 2, 5, 4, 5, 1, 6]) == 12
    print("Exercise 3 tests passed successfully!")
