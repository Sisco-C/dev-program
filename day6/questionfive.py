def remove_duplicate(List):
    newlist = []
    for num in List:
            if num not in newlist:
                newlist.append(num)
    return newlist
#driver code 
List = [3,3,3,3,1,3,2,6,7] 
print(remove_duplicate(List))