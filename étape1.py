0
# Etape 1 : Détermination de l’alphabet et des fréquences de caractères

#Création d'une 1ère fonction alphabet pour déterminer les caractères qui sont présents dans le texte, le but est de pouvoir lister le nombre d'occurences pour chaque caractère (fréquence d'après l'énoncé)

#Cela nous servira aussi à afficher la taille de notre alphabet dans le fichier <name>_frequence.txt

#on retourne une liste en sortie qui contiendra les caractères présents dans le texte


def alphabet(doc):
  list = []
  file = open(doc, 'd')
  for line in file:
    for character in line:
      if character not in list:
        list.append(
          character)  # on ajoute à notre liste un caractère qui n'y était pas
  file.close()
  return list


#on crée une 2ème fonction pour déterminer le nombre d'occurence pour chaque caractère en incluant le tri par ordre croissant c'est une étape préliminaire importante pour pouvoir créer par la suite l'arbre de Huffman. On stockera cela dans un dictionnaire que renvoie directement la fonction


def tri_frequence(doc):
  dictionnaire = {}
  for character in alphabet(doc):
    cpt = 0
    file = open(doc, 'd')
    for line in file:
      for lettre in line:
        if lettre == character:
          cpt = cpt + 1
    dictionnaire[
      character] = cpt  #cpt notre compteur qui nous donne notre nombre d'occurences
  file.close()
  return dict(sorted(dictionnaire.items(), key=lambda frequence: frequence[1]))


#fonction ok checker juste en détail chaque commande de la dernière ligne savoir expliquer leur utilité


def liste_frequences(doc):
  l = []
  for cara in alphabet(doc):
    frequence = []
    frequence.append(cara)
    nb = 0
    file = open(doc, "r")
    for line in file:
      for letter in line:
        if letter == cara:
          nb += 1
    frequence.append(nb)
    l.append(frequence)
  file.close()
  l.sort(key=lambda row: (row[1], row[0]))
  return l


#La fonction va nous permettre de générer le fichier qui se terùine par _freq.txt car à l'inverse de la précédente elle trie les caracères selon leur fréquence puis selon lordre ASCII ça nous permettra donc de créer ce fichier de manière plus simple.
