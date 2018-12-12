
L_Index = {}
command = ['DROP','ACCEPT']
content = 1
key = '192'
L_Index[key] = [command[0],content]

key = '193'
content +=1
L_Index[key] = [command[0],content]
print(L_Index)

key = '192'
value = command[1]
if key in L_Index:
    if value != L_Index[key][0]:
        L_Index[key][0] = value
    else:
        print('***')
else:
    L_Index[key] = [value,2]

print(L_Index)