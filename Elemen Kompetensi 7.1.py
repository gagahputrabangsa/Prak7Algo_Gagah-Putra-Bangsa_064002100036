print("@@@@@   @@@@@@   @@@@@   @@@@@@   @    @")
print("@       @    @   @       @    @   @    @")
print("@ @@@   @@@@@@   @ @@@   @@@@@@   @@@@@@")
print("@   @   @    @   @   @   @    @   @    @")
print("@@@@@   @    @   @@@@@   @    @   @    @\n")
 


def faktorial(n):
    faktorial = 1
    
    for i in range(1,n + 1):
        faktorial = faktorial*i
    print("Faktorial dari",n,"adalah",faktorial)
num = int(input("nilai: "))
faktorial(num)