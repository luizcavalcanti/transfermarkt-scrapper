import unittest

from transfermarkt_scrapper import buscador


class TestBuscadorEquipe(unittest.TestCase):

    def test_deve_retornar_lista_de_jogadores_por_equipe(self):
        resultado = buscador.buscar_jogadores_por_equipe(
            "https://www.transfermarkt.com.br/centro-sportivo-alagoano-al-/startseite/verein/18545")  # csa
        esperado = [
            {'nome': 'Caíque', 'url': 'https://www.transfermarkt.com.br/caique/profil/spieler/384159'},
            {'nome': 'Thiago Rodrigues', 'url': 'https://www.transfermarkt.com.br/thiago-rodrigues/profil/spieler/76139'},
        ]
        self.assertListEqual(esperado, resultado[:2])


if __name__ == "__main__":
    unittest.main()
