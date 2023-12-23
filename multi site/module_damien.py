def garder_chiffre(text):
    dico_chiffre = ["1","2","3","4","5","6","7","8","9",","]
    new_text = []
    for lettre in text:
        if lettre in dico_chiffre :
            new_text.append(lettre)
    prix = "".join(new_text)
    return prix
