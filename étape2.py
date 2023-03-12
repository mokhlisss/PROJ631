import Frequence as fr

#Etape 2: Construction de l’arbre

#on crée dans un 1er temps une classe pour les noeuds ce sera nécessaire pour créer la classe BTree qui va nous permettre de construire l'arbre de Huffman


class BNode():

  def __init__(self, frequence, label=None, leftChild=None, rightChild=None):
    self.frequence = frequence
    self.label = label
    self.leftChild = leftChild
    self.rightChild = rightChild

  def getOccurence(self):
    return self.freq

  def getCaractere(self):
    return self.label

  def getLeft(self):
    return self.leftChild

  def getRight(self):
    return self.rightChild


class BTree():

  def __init__(self, doc):

    self.doc = doc

    #on créé une liste de noeuds où chaque noeud contient le caractère et sa fréquence pour le document en question
    node_list = [
      BNode(frequence=label)
      for label, frequence in fr.dict_frequences(doc).items()
    ]

    while len(node_list) > 1:
      #on trie la liste pour chaque itération en focntion des fréquences dans l'ordre croissant
      node_list = sorted(node_list, key=lambda node: node.frequence)
      left_node = node_list.pop(0)
      right_node = node_list.pop(0)
      parent_node = BNode(left_node.getOccurence() + right_node.getOccurence())
      parent_node.leftChild = left_node
      parent_node.rightChild = right_node
      node_list.append(parent_node)

    #le noeud racine de l'arbre sera donc le premier élément de la liste node_list
    self.root = node_list[0]

  def get_root(self):
    return self.root
