


input_lst = []
result = []

num = int(input('insert number of input: '))        
for _ in range(num):
    inputt = input("insert the name: ")
    input_lst.append(inputt)
print (input_lst)

for j in input_lst:
    acron = ''
    for i in range(len(j)):
        if j[i].isupper():
            acron += j[i]
    result.append(acron)
    
for i in range(len(result)):
    swapped = False
    i=0
    while i < len(result)-1:
        if len(result[i])<len(result[i+1]):
            result[i],result[i+1]=result[i+1],result[i]
            swapped = True
        elif len(result[i]) == len(result[i+1]):
            if result[i] > result[i+1]:
                result[i],result[i+1]=result[i+1],result[i] 
        i += 1
    if swapped == False:
        break

print (result) 
