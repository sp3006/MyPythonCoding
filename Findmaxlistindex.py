def findmaxindexlist(input_list):
    maximum = list[0]
    index =0
    for i, num in enumerate(input_list):
        if num > maximum :
            maximum = num
            index = i
    return [index , maximum]
