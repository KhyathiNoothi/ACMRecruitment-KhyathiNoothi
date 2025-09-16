def is_binary_palindrome(num):
    binary_str = bin(num)[2:]
    return binary_str == binary_str[::-1]

# Example numbers
num1 = 9
num2 = 21

print(f"Number: {num1}, Binary: {bin(num1)[2:]}, Palindrome: {is_binary_palindrome(num1)}")
print(f"Number: {num2}, Binary: {bin(num2)[2:]}, Palindrome: {is_binary_palindrome(num2)}")
