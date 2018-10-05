from vue.abstract_vue import AbstractVue


class Bienvenue(AbstractVue):

    def display_info(self):
        print('Bienvenue {}, content de vous savoir parmi nous !'.format(
            AbstractVue.session.user.pseudo))
