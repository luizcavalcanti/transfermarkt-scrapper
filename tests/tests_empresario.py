import unittest

from main import Buscador


class TestBuscadorEmpresario(unittest.TestCase):

    def test_deve_retornar_nome_do_agente_quando_houver_caso_1(self):
        buscador = Buscador()
        retorno = buscador.buscar_empresario("https://www.transfermarkt.com.br/osvaldo/profil/spieler/76191")
        self.assertEqual("FPS Management & ...", retorno)

    def test_deve_retornar_nome_do_agente_quando_houver_caso_2(self):
        buscador = Buscador()
        retorno = buscador.buscar_empresario(
            "https://www.transfermarkt.com.br/wellington-paulista/profil/spieler/51716")
        self.assertEqual("Planet Soccer", retorno)

    def test_deve_retornar_na_quando_nao_houver_informacao_de_agente(self):
        buscador = Buscador()
        retorno = buscador.buscar_empresario("https://www.transfermarkt.com.br/marcelo-boeck/profil/spieler/27346")
        self.assertEqual("N/A", retorno)

    def test_deve_retornar_na_quando_o_agente_for_sem_agente_caso_1(self):
        buscador = Buscador()
        retorno = buscador.buscar_empresario("https://www.transfermarkt.com.br/felipe-alves/profil/spieler/189682")
        self.assertEqual("sem agente", retorno)

    def test_deve_retornar_na_quando_o_agente_for_sem_agente_caso_2(self):
        buscador = Buscador()
        retorno = buscador.buscar_empresario("https://www.transfermarkt.com.br/michel/profil/spieler/435186")
        self.assertEqual("sem agente", retorno)


if __name__ == "__main__":
    unittest.main()
