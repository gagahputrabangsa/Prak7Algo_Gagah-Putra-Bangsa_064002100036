def main(n):
    if n %3==0:
        n**3 
        print ("hasilnya adalah",n**3)
    else:
        cek(num)
def cek(n):
    if n %3!=0:
        print ("false")
        exit(0)
num=int(input("masukan nilai: "))
main(num)