def maximum_minimum_in_tuple_list(class_nytbestsellers):
    return_max = max(class_nytbestsellers,key=lambda item:item[1])[1]
    return_min = min(class_nytbestsellers,key=lambda item:item[1])[1]
    return return_max, return_min
    nytbestsellers= [('Queenie', 450), ('A little Life', 900), ('Red White Royal Blue', 380), ('Of Mice And Men', 470), ('Skin Of THe Night', 543)]
print("Maximum and minimum values of the said list of tuples:")
print(maximum_minimum_in_tuple_list(class_nytbestsellers))