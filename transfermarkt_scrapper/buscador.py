from selenium import webdriver


class Buscador:

    def buscar_jogadores_por_equipe(self, url_equipe):
        browser = webdriver.Firefox()
        browser.get(url_equipe)
        lista_jogadores = []

        jogadores = browser.find_elements_by_css_selector("table.items td.posrela a.spielprofil_tooltip")
        for jogador in jogadores:
            if not jogador.text == "":
                lista_jogadores.append({"nome": jogador.text, "url": jogador.get_property("href")})

        browser.quit()
        return lista_jogadores

    def buscar_empresario(self, url_jogador):
        browser = webdriver.Firefox()
        browser.get(url_jogador)

        resultado = "N/A"
        nome_empresarios = browser.find_elements_by_css_selector(".dataValue > a")
        for ancora in nome_empresarios:
            if "berater" in ancora.get_property("href"):
                resultado = ancora.text

        browser.quit()
        return resultado
