li = ['a', 'b', 'c', 'd', 'e']
print(li)
var1 = 1
temp_var = []
for i in range(len(li)):
    temp_var1 = li[i] + li[var1]
    temp_var.append(temp_var1)
    var1 += 1
    if var1 == len(li):
        break
print(temp_var)
