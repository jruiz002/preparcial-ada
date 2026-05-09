def find_pairs(nums: list[int], target: int) -> list[tuple[int, int]]:
    counts = {}
    result = []
    
    for num in nums:
        complement = target - num
        if complement in counts:
            for _ in range(counts[complement]):
                result.append((complement, num))
                
        counts[num] = counts.get(num, 0) + 1
        
    return result

# --- Tests ---
if __name__ == "__main__":
    tests = [
        ([2, 7, 4, 1, 3], 5, [(2, 3), (4, 1)]),
        ([1, 2, 3], 10, []),
        ([5, 5, 3, 7], 10, [(5, 5), (3, 7)])
    ]
    for nums, target, expected in tests:
        result = find_pairs(nums, target)
        assert sorted(result) == sorted(expected), f"Failed for {nums} with target {target}. Expected {expected}, got {result}"
        print(f"Passed: nums={nums}, target={target} -> {result}")
    print("All Exercise 1 tests passed successfully!")
