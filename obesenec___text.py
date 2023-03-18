hangman=['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("Zadaj slovo")
slovo=input()
dlzka_slova=len(slovo)
pokus=0
print(" \n" * 50)          
hadaj="_"*dlzka_slova
print(hadaj)
def hranie():
    global pokus, pismenko, hangman, dlzka_slova, hadaj
    print("Zadaj písmeno")
    pismeno=input()
    bolo=0

    for i in range(0,dlzka_slova):
        if slovo[i]==pismeno:
            hadaj=hadaj[:i]+pismeno+hadaj[i+1:]
            bolo=1
            
    if bolo:
        print(hadaj)
        print(hangman[pokus])
    else:
        pokus=pokus+1
        print(hadaj)
        print(hangman[pokus])

    if pokus==6:
        print("NEUHÁDOL SI, slovo bolo:", slovo)
        exit()

    if not "_" in hadaj:
        print("VYHRAL SI")
        exit()
    hranie()
        
hranie()
