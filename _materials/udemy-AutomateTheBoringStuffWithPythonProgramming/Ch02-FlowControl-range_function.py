# Ch02-FlowControl-range_function.py
# This is an example for the range() function and a for statement.
#
# https://automatetheboringstuff.com/chapter2/
# The Starting, Stopping, and Stepping Arguments to range()

for i in range(12,16):
    print(i)
# Expected results
# 12
# 13
# 14
# 15

# count from zero to eight by intervals of two
for i in range(0,10,2):
    print(i)
# Expected results
# 0
# 2
# 4
# 6
# 8

for i in range(5,-1,-1):
    print(i)
# Expected results
# 5
# 4
# 3
# 2
# 1
# 0
