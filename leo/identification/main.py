
from vue.accueil import Accueil


if __name__ == '__main__':

    # on demarre sur l'ecran accueil
    current_vue = Accueil()

    # tant qu'on a un ecran a afficher, on continue
    while current_vue:
        # on affiche une bordure pour separer les vue
        with open('assets/border.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
        # les infos a afficher
        current_vue.display_info()
        # le choix que doit saisir l'utilisateur
        current_vue = current_vue.make_choice()

    with open('assets/cat.txt', 'r', encoding="utf-8") as asset:
        print(asset.read())
