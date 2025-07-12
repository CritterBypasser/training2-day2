#snack problem
n= int(input('enter n '))
k=int(input('enter k '))
add=0
max=0
taste=list(map(int, input().split()))
for i in range (k):
    add= add+ taste[i]
for i in range (n-k):
    max=add
    add=add+taste[i+k]-taste[i]
    if max < add:
        max=add
print(max)