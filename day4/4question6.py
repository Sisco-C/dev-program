# Write a Python program to sort a list of dictionaries using Lambda
list_of_nytbestsellers = [{"bookname"  : "Red, White And Royal Blue" , "Author" : "Casey Mc Quinston" , "number of pages" : 380},
{"bookname": "A Little Life", "Author" : "Hanya Yanigahara" , "number of pages" : 420},
{"bookname": "Queenie", "Author" : "Candice Carty Williams", "number of pages" : 450}]
sorted_list = sorted(list_of_nytbestsellers, key= lambda i:i["number of pages"])
print ("The list printed sorting by number of pages is: ", sorted_list)

