import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css('section#numerical-index tr a[href^="pep-"]')
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css(
            'section#pep-content h1.page-title::text'
        ).get().strip()

        yield PepParseItem(
            number=int(page_title.split()[1]),
            name=page_title.split(' – ')[-1],
            status=response.css(
                'dt:contains("Status") + dd > abbr::text'
            ).get().strip()
        )
