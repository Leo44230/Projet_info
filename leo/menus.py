menus ={"principal" : Menu_principal}
utilisateurs = {"leo" : "leo", "guillaume" : "guillaume", "romane" : "romane", "fath" : "fath", "david" : "david"}

class Menu:

    def __init__(self, nom = "MENU", message = "Effectuez votre choix :",  choix = [], fcts = []):
        self.nom = nom
        self.message = message
        self.entree_utilisateur = -1
        self.choix = choix
        self.fcts = fcts

    def display_menu(self):
        print('#' * 50)
        print(' ' * ((50 - (len(self.nom))) / 2) + self.nom)  
        print('#' * 50 + '\n')
        print(self.message + '\n')
        i = 0
        for i in range (len(self.choix)):
            print ('[' + str(i) + '] ' + self.choix[i])
            i+= 1

    def obtenir_choix(self):
        choix_utilisateur = input("\nEntrez un nombre entre 0 et " + str(len(self.choix) - 1) + ' : ')
        while ((type(choix_utilisateur) != int) or (choix_utilisateur not in [i for i in range (len(self.choix))])):
            print('\nChoix incorrect, veuillez recommencer !\n')
            choix_utilisateur = input("Entrez un nombre entre 0 et " + str    (len(self.choix) - 1) + ' : ')
        self.entree_utilisateur = choix_utilisateur
        return (choix_utilisateur)

    def exec_fonction(self):
        self.choix[self.entree_utilisateur]()

    def exec_menu(self):
        self.display_menu()
        self.obtenir_choix()
        self.exec_fonction()

class Menu_principal(Menu):

    def __init__(self):
        self.nom = "MENU PRINCIPAL"
        self.message = "Effectuez votre choix : "
        self.choix = ["Creer un compte", "S'identifier en tant qu'utilisateur", "S'identifier en tant qu'administrateur", "Quitter"]
        self.fcts = []

menu = Menu_principal()
menu.exec_menu()
