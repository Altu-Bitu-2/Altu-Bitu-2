from collections import Counter


t = int(input())


for i in range(t):
    n = int(input())   
    cloth_type = []
    for j in range(n):
        cloth_type.append(input().split()[1])


    num = 1
    result = Counter(cloth_type)
    for key in result:
        num *= result[key] + 1
    
    print(num - 1)