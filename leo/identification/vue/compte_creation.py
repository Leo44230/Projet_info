from vue.abstract_vue import AbstractVue
from vue.bienvenue import Bienvenue
from service.compte_service import CompteService
from PyInquirer import Separator, prompt, Validator, ValidationError


class PasswordValidator(Validator):
    def validate(self, document):
        ok = len(document.text) > 5
        if not ok:
            raise ValidationError(
                message='Votre mot de passe doit faire au moins 6 caracteres',
                cursor_position=len(document.text))  # Move cursor to end


questions = [
    {
        'type': 'input',
        'name': 'pseudonyme',
        'message': 'Quel est votre pseudonyme ?',

    },
    {
        'type': 'password',
        'name': 'mot de passe',
        'message': 'Quel est votre mot de passe ?',
        'validate': PasswordValidator
    }
]


compte_service = CompteService()


class CreationCompte(AbstractVue):

    def make_choice(self):
        answers = prompt(questions)

        if compte_service.pseudo_disponible(answers['pseudonyme']):
            user = compte_service.creer_compte(
                answers['pseudonyme'], answers['mot de passe'])

            AbstractVue.session.user = user

            return Bienvenue()
        else:
            print('{} est deja utilise, merci d\'en choisir un autre ;) '.format(
                answers['pseudonyme']))
            return self.make_choice()
