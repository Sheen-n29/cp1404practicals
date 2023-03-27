# What did you see on line 1?
# Random integers ranging from 5 to 20, includes both end points as well

# What did you see on line 2?
# Odd numbers ranging from 3 to 10, includes startpoint but not the endpoint
# No it cannot produce a 4 because the random numbers are generated in increments of 2

# What did you see on line 3?
# Random float numbers ranging from 2.5 to 5.5, always consisting of around 13 decimal places

import random
# generates a random number between 1 - 100, includes both points
print(random.randint(1, 100))
