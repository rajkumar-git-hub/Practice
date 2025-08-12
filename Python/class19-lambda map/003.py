numbers=[18,31,8,11,7,55,232]

new_list=list(filter(lambda x :x % 2==0,numbers))
print(new_list)

new_list2=[]
# method-2 without filter
for num in numbers:
    if num%2==0:
        new_list2.append(num)

print(new_list2)

# method 3-

def even(n):
    if n%2==0:
        return n
    
print(list(filter(even,numbers)))

# method 4

print(list(filter(lambda x:x%2==0,[18,31,8,11,7,55,232])))


