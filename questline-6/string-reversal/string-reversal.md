# String Reversal Challenge

## Task
Reverse a string using both iterative and recursive methods, without using built-in functions.

---

## Method 1: Iterative Approach

### How it works:
- We start with an empty string `reversed_str`.
- Loop through each character in the original string.
- Prepend each character to `reversed_str`.
- This creates the reversed version one character at a time.

### Example:
Original: A C M
Step 1: A
Step 2: C + A = CA
Step 3: M + CA = MCA

---

## Method 2: Recursive Approach

### How it works:
- Base case: if the string is empty, return it.
- Otherwise:
  - Call the same function on the rest of the string (`s[1:]`)
  - Append the first character (`s[0]`) to the result
- This builds the string from the end to the beginning as the recursion unwinds.

---
