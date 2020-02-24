from transfermarkt_scrapper.buscador import Buscador

buscador = Buscador()

equipes = [
    {"nome": "csa", "url": "https://www.transfermarkt.com.br/centro-sportivo-alagoano-al-/startseite/verein/18545"},
    {"nome": "bahia", "url": "https://www.transfermarkt.com.br/ec-bahia/startseite/verein/10010"},
    {"nome": "confiança",
     "url": "https://www.transfermarkt.com.br/associacao-desportiva-confianca-se-/startseite/verein/3280"},
    {"nome": "fortaleza", "url": "https://www.transfermarkt.com.br/fortaleza-esporte-clube/startseite/verein/10870"},
    {"nome": "imperatriz",
     "url": "https://www.transfermarkt.com.br/sociedade-imperatriz-de-desportos-ma-/startseite/verein/23778"},
    {"nome": "river", "url": "https://www.transfermarkt.com.br/river-atletico-clube-pi-/startseite/verein/35388"},
    {"nome": "santa cruz", "url": "https://www.transfermarkt.com.br/santa-cruz-futebol-clube-pe-/startseite/verein/1785"},
    {"nome": "ceara", "url": "https://www.transfermarkt.com.br/ceara-sporting-club-ce-/startseite/verein/2029"},
    {"nome": "botafogo", "url": "https://www.transfermarkt.com.br/botafogo-futebol-clube-pb-/startseite/verein/17964"},
    {"nome": "america", "url": "https://www.transfermarkt.com.br/america-futebol-clube-rn-/startseite/verein/1751"},
    {"nome": "sport", "url": "https://www.transfermarkt.com.br/sport-club-do-recife/startseite/verein/8718"},
    {"nome": "abc", "url": "https://www.transfermarkt.com.br/abc-futebol-clube-rn-/startseite/verein/7209"},
    {"nome": "nautico", "url": "https://www.transfermarkt.com.br/clube-nautico-capibaribe/startseite/verein/2646"},
    {"nome": "crb", "url": "https://www.transfermarkt.com.br/clube-de-regatas-brasil-al-/startseite/verein/11449"},
    {"nome": "vitoria", "url": "https://www.transfermarkt.com.br/esporte-clube-vitoria/startseite/verein/2125"}
]

for equipe in equipes:
    jogadores = buscador.buscar_jogadores_por_equipe(equipe['url'])

    for jogador in jogadores:
        nome_empresario = buscador.buscar_empresario(jogador['url'])
        linha = "{}, {}, {}".format(equipe['nome'], jogador['nome'], nome_empresario)
        print(linha)
