#non-repeated first char

string=input("enter the str: ")

for ch in string:
    if string.count(ch)==1:
        print(f" non-repeated first char:{ch}")
        break #for_optimization (otherwise it will check the entire string)