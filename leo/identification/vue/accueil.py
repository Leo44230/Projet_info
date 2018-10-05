from vue.session import Session
from vue.compte_authentification import Authentification
from vue.compte_creation import CreationCompte
from vue.abstract_vue import AbstractVue
from PyInquirer import Separator, prompt


questions = [
    {
        'type': 'list',
        'name': 'authentification',
        'message': 'What do you want to do?',
        'choices': [
            'Me creer un compte',
            Separator(),
            'Me connecter',
        ]
    }
]


class Accueil(AbstractVue):

    def display_info(self):
        with open('assets/banner.txt', 'r', encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(questions)
        if reponse['authentification'] == 'Me connecter':
            return Authentification()
        else:
            return CreationCompte()
