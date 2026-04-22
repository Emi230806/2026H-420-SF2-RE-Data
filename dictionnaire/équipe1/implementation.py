class Dictionnaire():
    def __init__(self, donnees = None):
        self.donnees = dict(donnees) if donnees else {}

    def obtenir(self, cle, valeur_defaut=None):
        # .get()
        return self.donnees.get(cle, valeur_defaut)

    def copier(self):
        # .copy()
        return self.donnees.copy()

    def supprimer(self, cle):
        # .pop()
        return self.donnees.pop(cle, None)

    def vider(self):
        # .clear()
        self.donnees.clear()

    def cles(self):
        # .keys()
        return list(self.donnees.keys())

    def valeurs(self):
        # .values()
        return list(self.donnees.values())

    def elements(self):
        # .items()
        return list(self.donnees.items())

    def mettre_a_jour(self, autre_dict):
        # .update()
        self.donnees.update(autre_dict)+

    def afficher(self):
        return self.donnees