list = [(2,4),(7,9),(6,9),(4,1)]
return_max = max(list,key=lambda item:item[1])[1]
return_min = min(list,key=lambda item:item[1])[1]
print("Maximum and minimum values of the said list of tuples:",return_max,return_min)
