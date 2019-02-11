x=raw_input()
y=raw_input()
print x
for i in x,y:
	print i
	if(x[i]==y[i]):
		count=0
	else:
		count+=1
    if(count==1):
	    print("yes")
    else:
	    print("no")
