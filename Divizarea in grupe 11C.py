with open("c:/Users/Admin/Desktop/Lista clasei 11C.txt","r") as f:
    linii=list(f)
    f.close()
print("Nr.","Nume","Prenume","Nota","Limba", sep="\t")
for i, linie in enumerate(linii):
    print(i+1,":\t",linie,end=" ")
n=media=0
for linie in linii:
    campuri=linie.split()
    nota=int(campuri[2])
    n+=1
    media+=nota
a1=a2=0
print(nota,sep="\t")
print("Media a",n,"studenti e:",media/float(n))
m1=m2=0
grupe=[]
grupf=[]
for linie in linii:
    campuri=linie.split()
    if campuri[3]=="engleza":
        a1+=int(campuri[2])
        m1+=1
        grupe.extend([linie])
    if campuri[3]=="franceza":
        a2+=int(campuri[2])
        m2+=1
        grupf.extend([linie])
print("Media a studentilor din grupa engleza este:",round(a1/m1,2))
print("Media a studentilor din grupa franceza este:",round(a2/m2,2))
with open("c:/Users/Admin/Desktop/Grupa engleza.txt","w") as f:
    for i in grupe:
        f.write(i)
with open("c:/Users/Admin/Desktop/Grupa franceza.txt","w") as f:
    for i in grupf:
        f.write(i)

