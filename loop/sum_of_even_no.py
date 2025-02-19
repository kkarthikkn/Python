#sum,count,list of even_no

num=int(input("Enter the num: "))
even=0
even_no=[]
count=0
for x in range(1,num+1):
    if x%2==0:
        even_no.append(x)
        even+=x
        count+=1

print(f"eve no: {even_no}")
print(f"sum of even no: {even}")
print(f"count of even no: {count}")