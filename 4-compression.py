import étape1 as fr
import étape2 as bt
import étape3 as cod
import ratio as cr
import os
#import Frequence as fr
#import Codage as cod
#import BinaryTree as bt
#import CompressionRatio as cr



print("\n----BIENVENUE DANS LE COMPRESSEUR DE FICHIER TXT----\n")

doc = str(input("Quel texte voulez-vous compresser ? "))
doc2 = doc+".txt"
while os.path.exists(doc2) == False:
    print("\nLe fichier à compresser n'est pas dans le bon dossier\n")
    doc = str(input("Quel texte voulez-vous compresser ? "))
    doc2 = doc+".txt"

taille_alphabet = str(len(fr.alphabet(doc2)))

with open(doc+"_freq.txt", "w") as file:
    file.write(taille_alphabet+"\n")
    l = fr.liste_frequences(doc2)
    for char in l:
        if char[0] == "\n":
            file.write("LINE FEED "+str(char[1])+"\n")
        elif char[0] == " ":
            file.write("SPACE "+str(char[1])+"\n")
        else:
            file.write(str(char[0])+" "+str(char[1])+"\n")

with open(doc+"_comp.bin", "wb") as file:
    c = cod.Codage(bt.BTree(doc2))
    dict_codage_caractere = c.dic_codage_caractere(c.arbre.get_root())
    compressed_text = c.codage_texte(doc)
    file.write(compressed_text)

print(f'''\nDictionnaire du codage de chaque caractère: {dict_codage_caractere}\n
Taux de compression atteint: {cr.ratio(doc2)}
Nombre moyen de bits de stockage d’un caractère: {cr.nb_bits_moyen(doc2)}\n
Texte compressé avec succès\n'''
)