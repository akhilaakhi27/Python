dict={}
strl=input("Enter a string:")
for n in strl:
    keys=dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n]=1
print("Character frequency: ")
for k,v in dict.items():
    print(k,v)
