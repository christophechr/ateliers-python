# create function using built_in functions

# nombre :
# int = nombre entier
# float = nombre à virgule

def addition(nombre1, nombre2):
    résultat = nombre1 + nombre2
    return résultat
    
def main():
    résultatAddition = addition(1, 2)
    
    print(résultatAddition)

    print("Test")

    inputData = input("Donnez un nombre : ")

    print(inputData)


if __name__ == '__main__':
    main()