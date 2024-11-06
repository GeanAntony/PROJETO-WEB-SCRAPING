import scrapy
import requests
import re

class PachecoSpider(scrapy.Spider):
    name = "pacheco"
    allowed_domains = ["www.drogariaspacheco.com.br"]
    start_urls = ["https://www.drogariaspacheco.com.br/medicamentos"]

    def parse(self, response):
        # Seleciona cada item de produto individualmente
        products = response.css("ul > li")

        for product in products:
            # Extrai o nome do medicamento
            name = product.css("div.descricao-prateleira > a::text").get()
            
            # Extrai o preço do medicamento
            price = product.css("a.valor-por::text").get()

            # Limpa o valor do preço
            price_cleaned = re.sub(r"[^\d,\.]", "", price) if price else None

            # Verifica se nome e preço foram extraídos com sucesso antes de gerar o item
            if name and price_cleaned:
                yield {
                    "name": name.strip(),
                    "price": price_cleaned,
                }