# given the hours of day shift and night shift, and the number of days they work, and the maximum hours they will work, find the amount to be paid if each hour of overtime costs $100
days=int(input())
morn=list(map(int,input().split()))
morn.sort()
night=list(map(int,input().split()))
night.sort(reverse=True)
timeMax=int(input())
print('morn')
print(morn)
print('night')
print(night)
extra=0

for i in range(days):
    if morn[i]+night[i] > timeMax:
        fee=abs(morn[i]+night[i]-timeMax)
        extra+=100*fee
        
print(extra)        
