f=open("/Users/Admin/Desktop/caractere.txt","w")
f.write("andreea")
f.close()

f=open("/Users/Admin/Desktop/caractere.txt","r")
m=f.read()
print(m)
f.close()

#x-numarul de vocale
vocale=[]
x=0
for i in range(0,len(m)):
    if m[i]=="a" or m[i]=="o" or m[i]=="u" or m[i]=="e" or m[i]=="i" or m[i]=="A" or m[i]=="O" or m[i]=="U" or m[i]=="E" or m[i]=="I":
        x+=1
        vocale.extend(m[i])

f=open("/Users/Admin/Desktop/vocale.txt","w")
f.write("andreea")
f.close()
print("Numarul de vocale: ",x,"Vocalele sunt: ",vocale)