from time import sleep

from transfermarkt_scrapper import buscador

equipes = [
    {"nome": "CSA", "url": "https://www.transfermarkt.com.br/centro-sportivo-alagoano-al-/startseite/verein/18545"},
    {"nome": "Bahia", "url": "https://www.transfermarkt.com.br/ec-bahia/startseite/verein/10010"},
    {"nome": "Confiança", "url": "https://www.transfermarkt.com.br/associacao-desportiva-confianca-se-/startseite/verein/3280"},
    {"nome": "Fortaleza", "url": "https://www.transfermarkt.com.br/fortaleza-esporte-clube/startseite/verein/10870"},
    {"nome": "Imperatriz", "url": "https://www.transfermarkt.com.br/sociedade-imperatriz-de-desportos-ma-/startseite/verein/23778"},
    {"nome": "River", "url": "https://www.transfermarkt.com.br/river-atletico-clube-pi-/startseite/verein/35388"},
    {"nome": "Santa Cruz", "url": "https://www.transfermarkt.com.br/santa-cruz-futebol-clube-pe-/startseite/verein/1785"},
    {"nome": "Ceará", "url": "https://www.transfermarkt.com.br/ceara-sporting-club-ce-/startseite/verein/2029"},
    {"nome": "Botafogo", "url": "https://www.transfermarkt.com.br/botafogo-futebol-clube-pb-/startseite/verein/17964"},
    {"nome": "América", "url": "https://www.transfermarkt.com.br/america-futebol-clube-rn-/startseite/verein/1751"},
    {"nome": "Sport", "url": "https://www.transfermarkt.com.br/sport-club-do-recife/startseite/verein/8718"},
    {"nome": "ABC", "url": "https://www.transfermarkt.com.br/abc-futebol-clube-rn-/startseite/verein/7209"},
    {"nome": "Náutico", "url": "https://www.transfermarkt.com.br/clube-nautico-capibaribe/startseite/verein/2646"},
    {"nome": "CRB", "url": "https://www.transfermarkt.com.br/clube-de-regatas-brasil-al-/startseite/verein/11449"},
    {"nome": "Vitoria", "url": "https://www.transfermarkt.com.br/esporte-clube-vitoria/startseite/verein/2125"}
]

arquivo = open("resultado.csv", "w")

arquivo.write("equipe;jogador;agente\n")

for equipe in equipes:
    jogadores = buscador.buscar_jogadores_por_equipe(equipe['url'])

    for jogador in jogadores:
        try:
            nome_empresario = buscador.buscar_empresario(jogador['url'])
        except:
            print("Esperando alguns segundos para tentar novamente")
            sleep(10)
            nome_empresario = buscador.buscar_empresario(jogador['url'])

        linha = "{};{};{}".format(equipe['nome'], jogador['nome'], nome_empresario)
        arquivo.write(linha+"\n")
        arquivo.flush()
        print(linha)
