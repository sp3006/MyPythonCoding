my_list_1 = [1,None,2,None,4,5,None, None]

new_non_none=[]

for i in range(len(my_list_1)):
        for j in range(len(my_list_1)): 
            if my_list_1[i] == None:
                my_list_1[i] = my_list_1[i-1]
print(my_list_1)
