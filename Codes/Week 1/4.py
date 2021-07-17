a = [1,2,3,4,5,6,7,8,9]

s = 0
e = len(a) - 1

while s < e:
    temp = a[s]
    a[s] = a[e]
    a[e] = temp

    s+=1
    e-=1

print(a)