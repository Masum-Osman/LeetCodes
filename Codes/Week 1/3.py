a = [1,2,3,4,5,6,7,8,9]
res = []

n = len(a)

for i in range(n , 0, -1):
    res.append(i)
    a.pop()

print(res)