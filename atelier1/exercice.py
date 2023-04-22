# Je souhaite représenter la fonction affine a*x+b.
# Sachant que la valeur de a est donnée par l'utilisateur

#Vlad
def lineaire(b,x):
    string_a = input('Quelle est la valeur de a ?')
    a = int(string_a)
    reponse = a * x + b
    return reponse

resultat=lineaire(3,3)
print(resultat)

#Hugo
def FonctionAffine(a, x, b):
    return a * x + b

a = float(input("Entrez la valeur de a : "))
x = 3.3 # valeur de x
b = 2 # valeur de b
resultat = FonctionAffine(a, x, b)
print("Le résultat de la fonction affine ax+b: ", resultat)

