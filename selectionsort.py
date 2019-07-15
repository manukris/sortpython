array = [100, 197, 83, 65, 57, 44, 33, 25]

n = len(array)

for x in array:
    indexx = array.index(x)
    for y in array[indexx + 1:]:

        if x > y:
            indexy = array.index(y)
            t = array[indexx]
            array[indexx] = array[indexy]
            array[indexy] = t

print(array)









