x=input()
if((x>='a' and x<='z') or (x>='A' and x<='Z'):
    if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
