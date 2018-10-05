from vue.abstract_vue import AbstractVue


class Authentification(AbstractVue):

    def display_info(self):
        # a remplacer
        with open('assets/error.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())
