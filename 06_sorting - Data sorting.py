def sortNumbers(array, type):
    try:    
        if type == "ASC":
            for last in range(len(array)-1, 0, -1):
                for i in range(last):
                    if array[i] > array[i+1]:
                        array[i], array[i + 1] = array[i + 1], array[i]
            return array
        elif type == "DESC":
            for last in range(len(array)-1, 0, -1):
                for i in range(last):
                    if array[i] < array[i+1]:
                        array[i], array[i + 1] = array[i + 1], array[i]
            return array
        else: 
            raise ValueError
    except ValueError:
        return "ValueError('Invalid input data')"   
 
def sortData(array1, array2, type):  
    if type == "ASC" and len(array1) == len(array2):
        for last in range(len(array1)-1, 0, -1):
            for i in range(last):
                if array1[i] > array1[i+1]:
                    array1[i], array1[i + 1] = array1[i + 1], array1[i]
                    array2[i], array2[i + 1] = array2[i + 1], array2[i]
        return array2
    elif type == "DESC" and len(array1) == len(array2):
        for last in range(len(array1)-1, 0, -1):
            for i in range(last):
                if array1[i] < array1[i+1]:
                    array1[i], array1[i + 1] = array1[i + 1], array1[i]
                    array2[i], array2[i + 1] = array2[i + 1], array2[i]
        return array2       
    else: 
        raise ValueError('Invalid input data')   