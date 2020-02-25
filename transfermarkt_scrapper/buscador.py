import requests

from bs4 import BeautifulSoup


def buscar_jogadores_por_equipe(url_equipe):
    resposta = requests.get(url_equipe, headers={'User-Agent': 'Mozilla/5.0'}).content
    bs = BeautifulSoup(resposta, features="html.parser")

    lista_jogadores = []

    jogadores = bs.select("table.items td.posrela a.spielprofil_tooltip")
    for jogador in jogadores:
        if not jogador.text == "":
            url = jogador.get("href")
            if url.startswith("/"):
                url = "https://www.transfermarkt.com.br" + url

            lista_jogadores.append({"nome": jogador.text, "url": url})

    del lista_jogadores[1::2]
    return lista_jogadores


def buscar_empresario(url_jogador):
    resposta = requests.get(url_jogador, headers={'User-Agent': 'Mozilla/5.0'}).content
    bs = BeautifulSoup(resposta, features="html.parser")

    nome_empresarios = bs.select(".dataValue > a")
    for ancora in nome_empresarios:
        if "berater" in ancora.get("href"):
            return ancora.text

    return "N/A"
