"""
>>> from palindrome import is_palindrome

# Test 1: Empty string (should return True)
>>> is_palindrome('')
True

# Test 2: Single character (should return True)
>>> is_palindrome('a')
True

# Test 3: Simple palindrome (even length, should return True)
>>> is_palindrome('abba')
True

# Test 4: Simple palindrome (odd length, should return True)
>>> is_palindrome('racecar')
True

# Test 5: Non-palindrome (even length, should return False)
>>> is_palindrome('abcd')
False

# Test 6: Non-palindrome (odd length, should return False)
>>> is_palindrome('abcbaX')
False

# Test 7: Palindrome with spaces and mixed case (should return False due to spaces and case sensitivity)
>>> is_palindrome('A Granny at SCHOOL')
False

# Test 8: Palindrome with punctuation (should return False because the function doesn't ignore punctuation)
>>> is_palindrome('A man, a plan, a canal, Panama')
False

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
