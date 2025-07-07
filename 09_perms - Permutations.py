def permutations(array, counter=0):
    new_list = []
    if counter == len(array):
        new_list.append(array.copy())
    else:
        for i in range(counter, len(array)):
            array[counter], array[i] = array[i], array[counter]
            new_list.extend(permutations(array, counter + 1))
            array[counter], array[i] = array[i], array[counter]
 
    return new_list