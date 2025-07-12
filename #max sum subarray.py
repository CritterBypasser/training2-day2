#max sum subarray
sum=0
msum=0  
arr=list(map(int, input().split()))          
for i in range(len(arr)):
    sum=sum+arr[i]
    startIdx=i
    maxStart=0
    if sum==0 and maxStart==0:
        maxStart=startIdx
    if sum<0:
        sum=0
        startIdx=0
        maxStop=i-1            
    if sum> msum:
        msum=sum
        maxStop=i    
print(msum)
print('from')
print(maxStart)
print('to')
print(maxStop)            