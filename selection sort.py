def selectionsort(array):
    size=len(array)
    for ind in range(size):
        min_index = ind
        
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
                (array[ind], array[min_index]) = (array[min_index], array[ind])
    print(array)
array=[3,2,5,1,6,4,3,2,8,9,6,44,21,23,77,43]
selectionsort(array)
 
