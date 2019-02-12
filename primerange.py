x=input()
y=input()
count=0
for num in range(x,y+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
            else:
                print(num)
                count+=1
print(count)
    
