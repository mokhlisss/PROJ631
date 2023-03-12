import Frequence as fr
import Codage as cd
import BinaryTree as bt

def volume_initial(doc):
    nb_octet=0
    d1 = fr.dict_frequences(doc)
    for caractere in d1:
        nb_octet += d1[caractere]
    return nb_octet

def volume_finale(doc):
    nb_bit = 0
    cod = cd.Codage(bt.BTree(doc))
    d1 = fr.dict_frequences(doc)
    d2 = cod.dic_codage_caractere(cod.arbre.get_root())
    for caractere in d2:
        nb_bit += len(d2[caractere]) * d1[caractere]
    nb_octet = nb_bit/8
    return nb_octet

def ratio(doc):
    taux = 1 - volume_finale(doc)/volume_initial(doc)
    return round(taux, 3)

def nb_bits_moyen(doc):
    sm = 0
    cod = cd.Codage(bt.BTree(doc))
    d = cod.dic_codage_caractere(cod.arbre.get_root())
    for cle in d:
        sm += len(d[cle])
    bit_moyen = sm/len(fr.alphabet(doc))
    return round(bit_moyen, 3)