my_list = [10, 20, 30, 40]

it = iter(my_list)   

while True:
    try:
        item = next(it)   
        print(item)
    except StopIteration: 
        break