class Compte():
    
    def __init__(self) -> None:
        self.solde = 0
        self.nomCompte = ""
        self.numCompte =0
    
    def creeCompte(self):
        self.numCompte = int(input("Entrez le numero du compte  "))
        self.nomCompte = str(input("Entrez l'intitule du compte  "))
        self.solde = int(input("Entrez le solde initial  "))
        self.afficherCompte()
        
    def afficherCompte(self):
        print("Compte N°: ", self.numCompte)
        print("Intitule du Compte: ", self.nomCompte)
        print("Solde disponible : ", self.solde)
    
    def depot(self, montant):
        self.solde += montant
        self.afficheSolde()
    
    def retrait(self, montant):
        if (self.solde <= 500):
            print("Solde insuffisant, veiller deposer au moins 10000.00  UDS")
        else:
            self.solde -= montant
            self.afficheSolde()
    def afficheSolde(self):
        print("Votre solde est de ", self.solde)

com = Compte()

while True :
    print("_______________________________________")
    print("1. Creer un compte\n2. Depot\n3. Retrait\n4. Solde\n5. Quitter")
    
    choix = int(input("Selectionner une operation  "))
    
    if (choix == 1):
        com.creeCompte()
        
    elif (choix == 2):
        montant = float(input("Entrez le montant a deposer "))
        com.depot(montant)
        
    elif (choix == 3):
        montant = float(input("Entrez le montant a retirer "))
        com.retrait(montant)
    elif (choix == 4):
        com.afficheSolde()
        
    elif (choix == 5):
        exit()
    
        
        