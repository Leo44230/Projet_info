from service.compte_service import CompteService
from dao.compte_dao import CompteDao

compte_service = CompteService()
compte_dao = CompteDao()


def test_creer_compte():
    compte = compte_service.creer_compte('TestPseudo', 'MotDePassePseudo')
    if compte.id:
        compte_dao.delete(compte)
    assert compte.id and compte.id > 0


def test_valid_pseudo_connu():
    compte = compte_service.creer_compte('TestPseudo', 'MotDePassePseudo')
    dispo = compte_service.pseudo_disponible('TestPseudo')
    compte_dao.delete(compte)
    assert not(dispo)


def test_valid_pseudo_inconnu():
    dispo = compte_service.pseudo_disponible('PseudoFantaisiste')
    assert dispo
