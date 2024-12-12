# Citim numarul si intervalul
numar = int(input("Enter the number: "))
start = int(input("Enter the starting value of the range: "))
sfarsit = int(input("Enter the ending value of the range: "))
multiplii=[] #o lista(un vector) in care stocam toti multiplii gasiti
for i in range(start, sfarsit+1):
    if i%numar==0:
        multiplii.append(i) #adauga elementul i(un multiplu al numarului) se adauga la lista multiplii
if multiplii:
    print(f"Multiplii lui {numar} între {start} și {sfarsit} sunt: {multiplii}")
else:
    print(f"Nu există multiplii ai lui {numar} în intervalul {start} până la {sfarsit}.")