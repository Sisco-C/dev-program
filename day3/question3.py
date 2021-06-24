import numpy
num_array = []
num = 5
for i in range(int(num)):
    n = input("num :")
    num_array.append(int(n))

print ('ARRAY: ',num_array)
num_array = numpy.array(num_array)   
print ('ARRAY SIZE:',num_array.size * num_array.itemsize)