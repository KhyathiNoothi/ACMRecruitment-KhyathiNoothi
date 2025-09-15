# Rotate array to the right by k steps (without using built-in rotate functions)

def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k > n

    # Step 1: Reverse the whole array
    reverse(nums, 0, n - 1)

    # Step 2: Reverse the first k elements
    reverse(nums, 0, k - 1)

    # Step 3: Reverse the rest
    reverse(nums, k, n - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print("Original array:", nums)
rotate_array(nums, k)
print("Array after rotating by", k, "steps:", nums)
