"""
>>> from numberutil import aswords

 Test1: test for 0
>>> aswords(0)
'zero'

 Test2: test for single digit number
>>> aswords(5)
'five'

 Test3: test for a number below 20 and double digit
>>> aswords(19)
'nineteen'

 Test4: test for a multiple of 10 below 100
>>> aswords(70)
'seventy'

 Test5: test for a 21 < number 99
>>> aswords(34)
'thirty four'

 Test6: test for exactly 100
>>> aswords(100)
'one hundred'

Test7: test for a 101 < number < 999
>>> aswords(342)
'three hundred and forty two'

Test8: test for 999
>>> aswords(999)
'nine hundred and ninety nine'

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
