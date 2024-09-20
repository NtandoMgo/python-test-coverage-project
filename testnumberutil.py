"""
>>> from numberutil import aswords

 Test case 1: for zero
>>> aswords(0)
'zero'

 Test case 2: for a single digit number (covers the "units" path)
>>> aswords(5)
'five'

 Test case 3: for a number between 10 and 19 (covers the "teens" path)
>>> aswords(19)
'nineteen'

 Test case 4: for a multiple of 10 below 100 (covers the "tens" path)
>>> aswords(80)
'eighty'

 Test case 5: for a number in the range 21-99 (covers "tens and units" path)
>>> aswords(47)
'forty seven'

 Test case 6: exactly 100 (covers "hundreds" path without remainder)
>>> aswords(100)
'one hundred'

 Test case 7: number between 101 and 199 (covers "hundreds with remainder" path)
>>> aswords(105)
'one hundred and five'

 Test case 8: number in the range 200-999 (covers "hundreds with tens and units" path)
>>> aswords(342)
'three hundred and forty two'

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
