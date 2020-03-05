from time import sleep

from transfermarkt_scrapper import buscador


def escreve_levantamento_equipes(lista_equipes, nome_arquivo_csv):
    arquivo = open(nome_arquivo_csv, "w")

    arquivo.write("equipe;jogador;agente\n")

    for equipe in lista_equipes:
        jogadores = buscador.buscar_jogadores_por_equipe(equipe['url'])

        print(equipe['nome'].upper() + ":")

        for jogador in jogadores:
            try:
                nome_empresario = buscador.buscar_empresario(jogador['url'])
            except:
                print("Esperando alguns segundos para tentar novamente")
                sleep(60)
                nome_empresario = buscador.buscar_empresario(jogador['url'])

            linha = "{};{};{}".format(equipe['nome'], jogador['nome'], nome_empresario)
            arquivo.write(linha + "\n")
            arquivo.flush()
            print("\t" + jogador['nome'])

    arquivo.close()


equipes_cne = [
    {"nome": "ABC", "url": "https://www.transfermarkt.com.br/abc-futebol-clube-rn-/startseite/verein/7209"},
    {"nome": "América", "url": "https://www.transfermarkt.com.br/america-futebol-clube-rn-/startseite/verein/1751"},
    {"nome": "Botafogo", "url": "https://www.transfermarkt.com.br/botafogo-futebol-clube-pb-/startseite/verein/17964"},
    {"nome": "Bahia", "url": "https://www.transfermarkt.com.br/ec-bahia/startseite/verein/10010"},
    {"nome": "Ceará", "url": "https://www.transfermarkt.com.br/ceara-sporting-club-ce-/startseite/verein/2029"},
    {"nome": "Confiança",
     "url": "https://www.transfermarkt.com.br/associacao-desportiva-confianca-se-/startseite/verein/3280"},
    {"nome": "CRB", "url": "https://www.transfermarkt.com.br/clube-de-regatas-brasil-al-/startseite/verein/11449"},
    {"nome": "CSA", "url": "https://www.transfermarkt.com.br/centro-sportivo-alagoano-al-/startseite/verein/18545"},
    {"nome": "Fortaleza", "url": "https://www.transfermarkt.com.br/fortaleza-esporte-clube/startseite/verein/10870"},
    {"nome": "Imperatriz",
     "url": "https://www.transfermarkt.com.br/sociedade-imperatriz-de-desportos-ma-/startseite/verein/23778"},
    {"nome": "Náutico", "url": "https://www.transfermarkt.com.br/clube-nautico-capibaribe/startseite/verein/2646"},
    {"nome": "River", "url": "https://www.transfermarkt.com.br/river-atletico-clube-pi-/startseite/verein/35388"},
    {"nome": "Santa Cruz",
     "url": "https://www.transfermarkt.com.br/santa-cruz-futebol-clube-pe-/startseite/verein/1785"},
    {"nome": "Sport", "url": "https://www.transfermarkt.com.br/sport-club-do-recife/startseite/verein/8718"},
    {"nome": "Vitoria", "url": "https://www.transfermarkt.com.br/esporte-clube-vitoria/startseite/verein/2125"}
]

equipes_a = [
    {"nome": "Athletico", "url": "https://www.transfermarkt.com.br/clube-atletico-paranaense/startseite/verein/679"},
    {"nome": "Atlético (GO)", "url": "https://www.transfermarkt.com.br/atletico-goianiense/startseite/verein/15172"},
    {"nome": "Atlético (MG)", "url": "https://www.transfermarkt.com.br/atletico-mineiro/startseite/verein/330"},
    {"nome": "Botafogo (RJ)",
     "url": "https://www.transfermarkt.com.br/botafogo-fr-rio-de-janeiro/startseite/verein/537"},
    {"nome": "Bragantino",
     "url": "https://www.transfermarkt.com.br/clube-atletico-bragantino-sp-/startseite/verein/8793"},
    {"nome": "Corinthians", "url": "https://www.transfermarkt.com.br/corinthians-sao-paulo/startseite/verein/199"},
    {"nome": "Coritiba", "url": "https://www.transfermarkt.com.br/coritiba-fc/startseite/verein/776"},
    {"nome": "Flamengo (RJ)", "url": "https://www.transfermarkt.com.br/flamengo-rio-de-janeiro/startseite/verein/614"},
    {"nome": "Fluminense (RJ)",
     "url": "https://www.transfermarkt.com.br/fluminense-football-club/startseite/verein/2462"},
    {"nome": "Goiás", "url": "https://www.transfermarkt.com.br/goias-esporte-clube/startseite/verein/3197"},
    {"nome": "Grêmio",
     "url": "https://www.transfermarkt.com.br/gremio-foot-ball-porto-alegrense/startseite/verein/210"},
    {"nome": "Internacional",
     "url": "https://www.transfermarkt.com.br/sc-internacional-porto-alegre/startseite/verein/6600"},
    {"nome": "Palmeiras", "url": "https://www.transfermarkt.com.br/se-palmeiras-sao-paulo/startseite/verein/1023"},
    {"nome": "Santos", "url": "https://www.transfermarkt.com.br/fc-santos/startseite/verein/221"},
    {"nome": "São Paulo", "url": "https://www.transfermarkt.com.br/fc-sao-paulo/startseite/verein/585"},
    {"nome": "Vasco", "url": "https://www.transfermarkt.com.br/vasco-da-gama-rio-de-janeiro/startseite/verein/978"}
]

equipes_b = [
    {"nome": "América (MG)", "url": "https://www.transfermarkt.com.br/america-futebol-clube-mg-/startseite/verein/2863"},
    {"nome": "Avaí", "url": "https://www.transfermarkt.com.br/avai-futebol-clube-sc-/startseite/verein/2035"},
    {"nome": "Botafogo (SP)", "url": "https://www.transfermarkt.com.br/botafogo-futebol-clube-sp-/startseite/verein/9030"},
    {"nome": "Brasil de Pelotas", "url": "https://www.transfermarkt.com.br/gremio-esportivo-brasil-rs-/startseite/verein/10560"},
    {"nome": "Chapecoense", "url": "https://www.transfermarkt.com.br/associacao-chapecoense-de-futebol/startseite/verein/17776"},
    {"nome": "Cruzeiro", "url": "https://www.transfermarkt.com.br/ec-cruzeiro-belo-horizonte/startseite/verein/609"},
    {"nome": "Cuiabá", "url": "https://www.transfermarkt.com.br/cuiaba-esporte-clube-mt-/startseite/verein/28022"},
    {"nome": "Figueirense", "url": "https://www.transfermarkt.com.br/figueirense-futebol-clube/startseite/verein/4064"},
    {"nome": "Guarani", "url": "https://www.transfermarkt.com.br/guarani-futebol-clube-sp-/startseite/verein/1755"},
    {"nome": "Juventude", "url": "https://www.transfermarkt.com.br/esporte-clube-juventude/startseite/verein/10492"},
    {"nome": "Oeste", "url": "https://www.transfermarkt.com.br/oeste-futebol-clube-sp-/startseite/verein/21829"},
    {"nome": "Operário (PR)", "url": "https://www.transfermarkt.com.br/operario-ferroviario-esporte-clube-pr-/startseite/verein/27214"},
    {"nome": "Paraná", "url": "https://www.transfermarkt.com.br/parana-clube/startseite/verein/309"},
    {"nome": "Ponte Preta", "url": "https://www.transfermarkt.com.br/associacao-atletica-ponte-preta/startseite/verein/1134"},
    {"nome": "Sampaio Corrêa", "url": "https://www.transfermarkt.com.br/sampaio-correa-futebol-clube-ma-/startseite/verein/3319"},
]

# escreve_levantamento_equipes(equipes_cne, 'equipes_cne.csv')
# escreve_levantamento_equipes(equipes_a, 'equipes_a.csv')
escreve_levantamento_equipes(equipes_b, 'equipes_b.csv')
