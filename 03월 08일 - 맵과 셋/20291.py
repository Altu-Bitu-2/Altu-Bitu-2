n=int(input())
list=[]
split_list=[]
dic={}


for i in range(n):
    list.append(input())
    split_list.append(list[i].split('.')[1])


for j in range(n):
    if split_list[j] not in dic:
        dic[split_list[j]]=1
    else:
        dic[split_list[j]]+=1

num_list=list(dic.keys())
num_list.sort()

for k in num_list:
    print(k,dic[k])



