# find the sum of the 2 jackfruits with the maximum weights
arr=list(map(int, input().split()))
jam=0
weight=list(map(int, input().split()))
weight.sort(reverse= True)
for i in range(arr[1]):
    jam=jam+weight[i]
print(jam)
