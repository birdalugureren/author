import scrapy

class VikiSoz(scrapy.Spider):
    name = 'vikisoz'
    start_urls = ['https://tr.wikiquote.org/wiki/Kategori:Ki%C5%9Filer-A']

    def parse(self,response):
        for href in response.css('div.mw-category-group a::attr(href)'):
            yield response.follow(href, self.parse_author)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        yield {
            'text': extract_with_css('div.mw-parser-output li::text'),
        }

