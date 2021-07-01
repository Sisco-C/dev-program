def remove_duplicate(list):
    newlist = []
    for num in list:
            if num not in newlist:
                newlist.append(num)
    return newlist
#driver code
list = [3,3,3,3,1,3,2,6,7]
print(remove_duplicate(list))
 