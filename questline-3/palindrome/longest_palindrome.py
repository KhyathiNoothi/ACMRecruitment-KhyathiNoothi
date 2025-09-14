def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""

    start, max_length = 0, 1

    for i in range(len(s)):
        # Odd length palindrome
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

        # Even length palindrome
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_length:
                start = left
                max_length = right - left + 1
            left -= 1
            right += 1

    return s[start:start + max_length]

# Example usage:
if __name__ == "__main__":
    test_str = "babad"
    print("Longest Palindromic Substring:", longest_palindromic_substring(test_str))
