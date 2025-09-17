# Given a string s, find the length of the longest substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# This uses Sliding Window technique with two pointers to track the current substring without repeating characters.

def length_of_longest_substring(s):
    char_index = {}
    max_length = 0
    start = 0

    for end, char in enumerate(s):
        # If seen and in current window, move start pointer
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        char_index[char] = end
        # Update max length
        max_length = max(max_length, end - start + 1)
    return max_length

# Example:
s1 = "abcabcbb"  # Output: 3 ("abc")
s2 = "bbbbb"     # Output: 1 ("b")
print(length_of_longest_substring(s1))
print(length_of_longest_substring(s2))
