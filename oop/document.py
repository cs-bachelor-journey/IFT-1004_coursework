
class Document:
    def __init__(self, le_texte):
        self.texte = le_texte
    
    def transformer_en_majuscules(self):
        # Nous utilisons la mÃ©thode str.upper existante
        self.texte = self.texte.upper() 
        
    def chiffrer(self, cle):
        # Algorithme du chiffrement de CÃ©sar.
        # Voir: https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        nouveau_texte = ""
        
        for c in self.texte:
            if c in alphabet:
                index = alphabet.index(c)
                nouvel_index = (index + cle) % 26
                nouveau_texte += alphabet[nouvel_index]
            else:
                nouveau_texte += c
                
        self.texte = nouveau_texte
        
    def dechiffrer(self, cle):
        self.chiffrer(-cle)

    def __repr__(self):
        # Nous redÃ©finissons la mÃ©thode spÃ©ciale __repr__ pour indiquer Ã  Python 
        # comment reprÃ©senter un objet Document en une chaÃ®ne de caractÃ¨res
        return self.texte    
    
    
if __name__ == "__main__":
    d = Document("ceci est un texte!")
    print(d)
    
    d.chiffrer(8)
    print(d)
    
    d.dechiffrer(8)
    print(d)
    
    d.transformer_en_majuscules()
    print(d)