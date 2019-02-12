x=raw_input()
y=raw_input()
def isIso(a,b):
    m={}
    r={}
    for i,c in enumerate(a):
        if c in m:
            if b[i]!=m[c]:
                print ("no")
            else:
               m[c]=b[i]
            if b[i] in r:
              if c!=r[b[i]]:
                  print("no")
              else:
                 r[b[i]]=c
    print("yes")
isIso(x,y)
   
