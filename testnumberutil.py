"""
>>> from numberutil import aswords

# Test1: test for 0
>>> aswords(0)
'zero'

# Test2: test for single digit number
>>> aswords(5)
'five'

# Test3: test for a number below 20 and double digit
>>> aswords(19)
'nineteen'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
