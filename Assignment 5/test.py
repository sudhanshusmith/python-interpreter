tuple_index_mapped_to = []
non_tuple_index = []
Data_len = len(Data)
for i in range (0,Data_len):
    if type(Data[i]) == tuple:
        print("The Final Value of",Data[i][0],"is",Data[Data[i][1]])
        tuple_index_mapped_to.append(Data[i][1])
    else:
        non_tuple_index.append(i)
        i = i + 1


# print(tuple_index_mapped_to)  # Intial collected list tuple_index_mapped_to
tuple_index_mapped_to.sort()   # sorting the list tuple_index_mapped_to
tuple_index_mapped_to = list(dict.fromkeys(tuple_index_mapped_to))  # deleting the duplicate from the list tuple_index_mapped_to
# print(non_tuple_index)
# print(tuple_index_mapped_to)
print()


print("Garbage Values are Here......................")
garbage_index = list(set(tuple_index_mapped_to) - set(non_tuple_index)) + list(set(non_tuple_index) - set(tuple_index_mapped_to))  # Code to get difference of two lists Using set()
# print("Garbage indexes are", garbage_index)
garbage_index_len = len(garbage_index)
for i in range (0,garbage_index_len):
    print("One of the Garbage Value in Data is",Data[garbage_index[i]],", Which is present at index",garbage_index[i])
