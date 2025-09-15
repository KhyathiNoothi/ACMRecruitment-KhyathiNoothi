# String Reversal using Iterative and Recursive methods
# Without using built-in functions

# Iterative method
def reverse_iterative(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Prepend each character
    return reversed_str

# Recursive method
def reverse_recursive(s):
    if len(s) == 0:
        return s
    return reverse_recursive(s[1:]) + s[0]

# Test string
test_string = "ACMRecruit"

# Testing both methods
print("Original String:", test_string)
print("Reversed (Iterative):", reverse_iterative(test_string))
print("Reversed (Recursive):", reverse_recursive(test_string))
