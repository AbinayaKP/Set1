x=input()
y=input()
count=0
for num in range(x,y+1):
    if all(num%i!=0 for i in range(2,num)):
        count+=1
print(count)
    
