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
    assert sorted(find_pairs([2, 7, 4, 1, 3], 5)) == sorted([(2, 3), (4, 1)])
    assert find_pairs([1, 2, 3], 10) == []
    assert sorted(find_pairs([5, 5, 3, 7], 10)) == sorted([(5, 5), (3, 7)])
    print("Exercise 1 tests passed successfully!")
