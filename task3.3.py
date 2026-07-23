words = ["hi", "hello", "hey", "howdy"]

my_list=[
    x.upper()
    for x in words
    if len(x)>3 
    ]
print(my_list)


#learn comprehension first line is transform second is loop and third is filter