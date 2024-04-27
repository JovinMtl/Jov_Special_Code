def getIndex(chaine:str, sous_chaine:str):
    """THis one will return the index of last caracter of 
    sous_chaine which is in a chaine.
    
    RETURNS index or 0
    """

    worth = True
    length_chaine = len(chaine)
    i=0 #counter for chaine
    j=0 #counter for sous_chaine
    found = 0 #the number of occurence
    while (worth and (i < length_chaine) and (j < len(sous_chaine))):
        if sous_chaine[j] == chaine[i]:
            i += 1
            j += 1
            found += 1
        else:
            i += 1
    if (len(sous_chaine) == found):
        return i
    else:
        return 0
