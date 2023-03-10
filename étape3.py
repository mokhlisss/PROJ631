#import BinaryTree as bt



# Etape 3: Codage du texte
from étape1 import *
from étape2 import *

#création d'une classe Codage avec un paramètre de type BinaryTree et un paramètre de type dictionaire qui va stocker le codage utilisé pour chaque caractère et ce paramètre va nous servir ensuite à coder tout le texte par concaténation des codes de chacun de ses caractères


class Codage():

  def __init__(self, arbre):
    self.arbre = arbre
    self.codage = {}

  #on effectue un parcours en profondeur de notre arbre en mettant toujours le noeud racine comme paramètre de cette fonction
  def dic_codage_caractere(self, node, code_actuel=""):
    if node == None:
      return

    if node.getCaractere() != None:
      self.codage[node.getCaractere()] = code_actuel
    self.dic_codage_caractere(node.leftChild, code_actuel + "0")
    self.dic_codage_caractere(node.rightChild, code_actuel + "1")
    return self.codage
  
  

  def codage_texte(self,doc):
    #doc = self.arbre
    ch = {}
    with open(doc+".txt", 'r') as file:
      lines = file.readlines()
      for line in lines:
        for caractere in line:
          #ch += self.codage[caractere]
          #ch += self.codage
          ch.update(self.codage) #methode de concaténation de dictionnaires 
      file.close()
      return ch
      #print(ch)
