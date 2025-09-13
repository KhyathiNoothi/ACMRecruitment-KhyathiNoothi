def second_largest(arr):
    largest = second = float('-inf')  
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:  
            second = num
    
    if second == float('-inf'):
        return None
    return second


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter numbers: ").split()))

result = second_largest(arr)

if result is None:
    print("No second largest number found.")
else:
    print("Second largest:", result)
