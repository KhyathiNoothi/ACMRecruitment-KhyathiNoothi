def rotate(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k > n
    return nums[-k:] + nums[:-k]

# Example test
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    result = rotate(nums, k)
    print("Original array:", nums)
    print(f"Array after rotating by {k} steps:", result)
