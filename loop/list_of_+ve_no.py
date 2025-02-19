#count the list of +ve numbers and display the +ve num.

num=[-1,5,8,3,-8,-1,7,45,-68,-9,10,20,-43]
positive_num=0
pos_no=[]
for x in num:
    if x>0:
        positive_num+=1
        pos_no.append(x)

print(f"count of +ve num: {positive_num}")
print(f"+ve num: {pos_no}")