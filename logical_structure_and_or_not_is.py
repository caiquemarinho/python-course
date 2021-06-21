"""

Logical Structure: and, or, not, is.

Unary:
    - not
Binary:
    - and, or, is

Rules:

and -> Both values need to be True
or -> One of the values need to be True
not -> The boolean value is inverted, True turns into False and False becomes True.
is -> The value is compared to a second value.
"""

active = True
logged_in = False

if active and logged_in:
    print('Welcome!')
else:
    print('You need to activate your account. Please check your e-mail.')

