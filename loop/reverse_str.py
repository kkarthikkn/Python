#reverse string

str=input("Enter string: ")
rev_str=""

#for_loop
for char in str:
    rev_str=char+rev_str
print(f"reverse using for loop: {rev_str}")

#--------------------------------------------------
#slice_method
slice=str[::-1]
print(f"reverse through slicing: {slice}")

#--------------------------------------------------
#stack_method  ----> FILO

stack=list(str)
reverse_str=""

while stack:
    reverse_str+=stack.pop()

print(f"Reversed using stack method: {reverse_str}")

