# -*- coding: utf-8 -*-
"""
jump2python-02_2_string_datatype-(5)-advanced_string_formatting.py
# 고급 문자열 포매팅, p.63
# format method
"""
# Using idex {0}, {1}, ...
print( "I eat {0} apples.".format(3) ) # 0th value in format is replaced.
# I eat 3 apples.

print( "I eat {0} apples.".format("five") )
# I eat five apples.

number = 3
"I eat {0} apples.".format( number )
# 'I eat 3 apples.'

number = "five"
"I eat {0} apples.".format( number )
# 'I eat five apples.'

# 
number = 10
day = "three"
"I ate {0} apples. So I was sick for {1} days.".format( number, day )
# 'I ate 10 apples. So I was sick for three days.'

number = "ten"
day = 3
"I ate {0} apples. So I was sick for {1} days.".format( number, day )
# 'I ate ten apples. So I was sick for 3 days.'

# Using {variable}..., e.g. {name}
# The following causes KeyError.
# "I ate {number} apples. So I was sick for {day} days.".format( number, day )
# KeyError: 'number'

"I ate {number} apples. So I was sick for {day} days.".format( number=10, day=3 )
# 'I ate 10 apples. So I was sick for 3 days.'

# Mixing index {0} & {variable}...
"I ate {0} apples. So I was sick for {day} days.".format(10, day=3)
# 'I ate 10 apples. So I was sick for 3 days.'

# Align left :<
"{0:<10}".format("hi")
#'hi        '

# Align right :>
"{0:>10}".format("hi")
# '        hi'

# Align center
"{0:^10}".format("hi")
#'    hi    '

# Filling in spaces...
#   Put a character BEFORE <>^
"{0:=^10}".format("hi")
# Fill in space with = & align center
# '====hi===='

"{0:!<10}".format("hi")
# Fill in space with ! & align left
# 'hi!!!!!!!!'

"{0:_>10}".format("hi")
# '________hi'

# Floating point
y = 3.14159265359
"{0:0.4f}".format( y )
# '3.1416'

"{0:10.4f}".format(y)
# '    3.1416'

# '{' or '}'
"{{ and }}".format()
# '{ and }'
# Note it's not \{ and \}, but {{ and }}    # GREP
#"\{ and \}".format()                       # GREP
# KeyError: ' and \\'                       # GREP
