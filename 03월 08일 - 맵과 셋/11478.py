str=input()

str_set=set()


for i in range(len(str)):
    for j in range(i,len(str)):
        str_set.add(str[i:j+1])
    
num=len(str_set)

print(num)

