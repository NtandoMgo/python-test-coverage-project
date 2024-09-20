"""
>>> from numberutil import aswords

# Test1: test for 0
>>> aswords(0)
'zero'

# Test2: test for single digit number
>>> aswords(5)
'five'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
