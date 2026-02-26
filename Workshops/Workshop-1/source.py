# Paul Kreischer - pck0010@auburn.edu
# SQA - Workshop 1

def performSub(a, b):

    return a-b

def performAdd(a, b):

    return a+b

def performMul(a, b):

    return a*b

def performDiv(a, b):

    if b == 0:
        return "Error: Divide by zero"
    return a/b

def performSqrt(a):

    if a < 0:
        return "Error: Square root of negative number"
    return a**0.5
