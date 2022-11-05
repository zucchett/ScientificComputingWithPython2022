list = [(1,2,3),(4,4)]
normalized_list=[]

#check every element in the list
for item in list:
    normalized_item=()
    #normalize the vector with divided every number to the total sum
    for num in item:
        normalized_item = normalized_item + (num/sum(item),)
    #filling the result list
    normalized_list.append(normalized_item)

print(normalized_list)