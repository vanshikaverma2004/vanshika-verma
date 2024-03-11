list = [1,2,3,1,2,4,5,4,6,2]
print("list before", list)
temp_list = []

for i in list:
    if i not in temp_list:
        temp_list.append(i)
        
list = temp_list

print("list after removing duplicates", list)