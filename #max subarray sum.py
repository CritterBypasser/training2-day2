#max subarray sum- kadane's algo
arr=list(map(int, input().split()))
max=0
for k in range (len(arr)):
    add=0
    for i in range (k,len(arr)):
        add+=arr[i]
        if add> max:
            max=add
            
print(max)
 
sum=0
msum=0            
for i in range(len(arr)):
    sum=sum+arr[i]
    if sum<0:
        sum=0            
    if msum< sum:
        msum=sum    
print(msum)            