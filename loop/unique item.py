list=['a','b','c','d','d','e','f']
repeated=set()

for i in list:
    if list.count(i)>1:
        print(f"Duplicate list item: {i}")
        break

