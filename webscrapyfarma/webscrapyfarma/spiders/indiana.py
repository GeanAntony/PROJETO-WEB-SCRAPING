import scrapy

class IndianaSpider(scrapy.Spider):
    name = "indiana"
    allowed_domains = ["www.farmaciaindiana.com.br"]
    start_urls = ["https://www.farmaciaindiana.com.br/medicamentos?page=3"]

    def parse(self, response):
        #Captura os produtos e passa pra uma variavel products
        products = response.css("div.vtex-product-summary-2-x-nameContainer")


        # Itera pelos produtos para extrair o nome e o preço
        for product in products:
            name = product.css("h3 > span::text").get()
            price = product.css("span.price::text").get() 
            
            # Gera o item com o nome e o preço do produtoss
            if name and price:
                yield {
                    "name": name.strip(),
                    "price": price.strip()
                }
