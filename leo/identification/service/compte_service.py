from dao.compte_dao import CompteDao
from business_model.compte import Compte
compte_dao = CompteDao()


class CompteService:

    def pseudo_disponible(self, pseudo):
        return not(compte_dao.get(pseudo))

    def creer_compte(self, pseudo, motdepasse):
        compte = Compte(pseudo, motdepasse)
        return compte_dao.create(compte)
