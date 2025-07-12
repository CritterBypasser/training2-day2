#jackfruit
arr=list(map(int, input().split()))
jam=0
weight=list(map(int, input().split()))
weight.sort(reverse= True)
for i in range(arr[1]):
    jam=jam+weight[i]
print(jam)