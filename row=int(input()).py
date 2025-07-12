row=int(input())
col=int(input())
flag=0
arr=[[0 for _ in range (row)] for _ in range(col)]
for i in range (row):
    arr[i]=list(map(int,input().split()))
for i in range (row):
    for j in range (col):
        if arr[i][j]<0:
            flag+=1
print(flag)            