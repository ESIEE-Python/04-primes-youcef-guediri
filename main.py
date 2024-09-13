"youcef guediri"
from math import sqrt
#### Fonction secondaire
def isprime(p):
    """return True si un nombre p est premier
p: valeur entière"""
    if p in (0,1):
        return False
    for i in range(2,int(sqrt(p))+1):
        if(p%i)==0:
            return False
    return True
#### Fonction principale
def main():
    "fonction main qui fait appel à la fonction secondaire pour la tester sur une plage de 0 à 100"
    # vos appels à la fonction secondaire ici
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
