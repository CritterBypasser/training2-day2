#chheck subarray sum to input value, flag if they mmatch  
k=int(input('enter k '))
z=int(input('enter sum '))
print('enter numbers')
flag=0
add=0
arr=list(map(int, input().split()))
for i in range (k):
    add=add+arr[i]
    if add== z:
        flag+=1
for i in range (len(arr)-k):
    add=add+arr[k+i]-arr[i]
    if add== z:
        flag+=1
        
print(flag)    
    
    
    
