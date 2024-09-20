"""
>>> import timeutil

>>> timeutil.validate("")
False
>>> timeutil.validate("1000:12 p.m.")
False
>>> timeutil.validate("19:37 p.m.")
False
>>> timeutil.validate("13:45 pm")
False
>>> timeutil.validate("10:234 p.m.")
False
>>> timeutil.validate("10:2A p.m.")
False

"""

import doctest
doctest.testmod(verbose=True)