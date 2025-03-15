from random import randint
from math import floor

def recursiveRandom(target,maxa,mina):
    halfmax = (maxa+mina)/2
    halfmax = int(halfmax)
    if target == maxa: 
        print("a is this ma g",maxa)
    elif target == halfmax: 
        print("a is this ma g",halfmax)
    elif target < int(halfmax): 
        recursiveRandom(target,int(halfmax),int(mina))
    elif target > int(halfmax): 
        recursiveRandom(target,int(maxa),int(halfmax))

def main():
    maxx = int(input("Enter a max number: "))
    a = randint(0,maxx)
    print("a is",a)
    recursiveRandom(a,maxx,0)
    print()
    print("  III     AAAAA   M   M       M   M    U   U  SSSSS   III   CCCC ")
    print("   I      A   A   MM MM       MM MM    U   U  S        I   C    ")
    print("   I      AAAAA   M M M       M M M    U   U  SSSSS    I   C    ")
    print("   I      A   A   M   M       M   M    U   U     S     I   C    ")
    print("  III     A   A   M   M       M   M     UUUU  SSSSS   III   CCCC ")
    #Playboi Carti fan seeyuh ho

if __name__ == "__main__":
    main()
