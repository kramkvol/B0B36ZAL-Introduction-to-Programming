from operator import index
 
 
def polyEval (polynom, x):
    result = 0
    index = 0
    for number in polynom:
        result += number * (x**index)
        index += 1
    return result
 
def polySum (poly1, poly2):
    new_poly_len = 0
    poly_result = list()
    new_poly1 = poly1
    new_poly2 = poly2
    counter = 1
    print(len(poly1) - len(poly2))
    if len(poly1) >= len(poly2):
        new_poly_len = len(poly1)
        while counter <= len(poly1) - len(poly2):
            new_poly2.append(0)  
        counter += 1 
    else:
        new_poly_len = len(poly2)
        while counter <= len(poly2) - len(poly1):
            new_poly1.append(0)  
        counter += 1
         
    for i in range(0, new_poly_len, 1):
        poly_result.append(0)
        poly_result[i] = poly1[i] + poly2[i]
        print(poly_result[i])
            
    for j in range(new_poly_len-1, 0, -1):
        if float(poly_result[j]) == 0.0:
           poly_result.pop(j)
        else:
           break
    return poly_result
    
def polyMultiply (poly1, poly2):
    poly_result_len = len(poly1) + len(poly2) - 1
    poly_result = [0] * poly_result_len
     
    for i, poly_1 in enumerate (poly1):
        for j, poly_2 in enumerate (poly2):
            poly_result [i + j] += poly_1 * poly_2
    return poly_result