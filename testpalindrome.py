# test_palindrome.py
# Test suite for palindrome module

"""
>>> import palindrome

# Test 1: Empty string (should return True)
>>> palindrome.is_palindrome('')
True

# Test 2: Single character (should return True)
>>> palindrome.is_palindrome('a')
True

# Test 3: Simple palindrome (even length)
>>> palindrome.is_palindrome('abba')
True

# Test 4: Simple palindrome (odd length)
>>> palindrome.is_palindrome('racecar')
True

# # Test 5: Non-palindrome
# >>> palindrome.is_palindrome('abcd')
# False

# Test 6: Non-palindrome with mixed case
>>> palindrome.is_palindrome('A Granny at SCHOOL')
False

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
