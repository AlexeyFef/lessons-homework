import math
def square(a):
    if a % 1 == 0:
        return(a*a)
    else:
        return(math.ceil(a*a))