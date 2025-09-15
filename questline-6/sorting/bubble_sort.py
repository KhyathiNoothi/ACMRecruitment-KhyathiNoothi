# Bubble Sort implementation in Python

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
# Test the function
test_list = [5, 2, 9, 1, 5, 6]
print("Original list:", test_list)

bubble_sort(test_list)

print("Sorted list:", test_list)
