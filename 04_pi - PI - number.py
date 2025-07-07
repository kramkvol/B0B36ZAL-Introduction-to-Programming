def leibnizPi(iterations):
    pi = 0
    counter = 1
    divider = 1
    while counter <= iterations:
        fraction = 4 / divider
        if counter % 2 == 0:
            pi = pi - fraction
        else:
            pi = pi + fraction
        divider += 2
        counter += 1
    return pi
 
def nilakanthaPi(iterations):
    denominator = 2
    result = 3.0
    counter = 1
    while counter < iterations:
        expression = 4 / (denominator * (denominator + 1) * (denominator + 2))
        if counter % 2 != 0:
            result += expression
        else:
            result -= expression
        denominator += 2
        counter += 1
    return result
 
 
def newtonPi(init):
    import math
    x1 = init
    while True:
        number =  x1 - (math.sin(x1) / math.cos(x1))
        if number == x1:
            return round(number, 14)
        x1 = number
 
def newtonPi(init):
    import math
    x1 = init
    while True:
        number =  x1 - (math.sin(x1) / math.cos(x1))
        if number == x1:
            return round(number, 14)
        x1 = number