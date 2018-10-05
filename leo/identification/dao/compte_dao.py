from dao.connection import connection
import psycopg2
from business_model.compte import Compte


class CompteDao:

    def create(self, compte):
        cur = connection.cursor()
        try:
            cur.execute(
                "INSERT INTO account (pseudo, motdepasse) VALUES (%s, %s) RETURNING id;", (compte.pseudo, compte.motdepasse))

            compte.id = cur.fetchone()[0]
            # la transaction est enregistree en base
            connection.commit()
        except psycopg2.Error as error:
            # la transaction est annulee
            connection.rollback()
            raise error
        finally:
            cur.close()

        return compte

    def delete(self, compte):
        cur = connection.cursor()
        try:
            cur.execute(
                "delete from account where id=%s", (compte.id,))

            # la transaction est enregistree en base
            connection.commit()
        except psycopg2.Error as error:
            # la transaction est annulee
            connection.rollback()
            raise error
        finally:
            cur.close()

    def get(self, pseudo):
        with connection.cursor() as cur:
            cur.execute(
                "select id, pseudo, motdepasse from account where pseudo=%s", (pseudo,))

            found = cur.fetchone()
            if found:
                return Compte(found[1], found[2], found[0])

            return None
