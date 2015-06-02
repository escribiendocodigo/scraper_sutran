# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver

from scraper_sutran.items import SutranItem


class SutranSpider(scrapy.Spider):
    name = 'sutran'
    allowed_domains = ['sutran.gob.pe']
    start_urls = (
        'http://www.sutran.gob.pe/portal/index.php/devolucion-licencias-de-conducir-pnp',
    )

    def __init__(self):
        self.driver = webdriver.Firefox()

    def parse(self, response):
        #listando todos los registros
        url = response.url + '?limit50=0'
        self.driver.get(url)
        time.sleep(2.5)

        trs = self.driver.find_elements_by_css_selector('tr.fabrik_row')

        for tr in trs:
            c = 0
            item = SutranItem()
            tds = tr.find_elements_by_css_selector('td.fabrik_element')

            for td in tds:
                if c == 1:
                    item['nro_papeleta'] = td.text
                if c == 2:
                    item['fecha_infraccion'] = td.text
                if c == 3:
                    item['infraccion'] = td.text
                if c == 4:
                    item['region'] = td.text
                if c == 5:
                    item['placa'] = td.text
                if c == 6:
                    item['conductor'] = td.text
                if c == 7:
                    item['licencia'] = td.text
                if c == 8:
                    item['estado_actual'] = td.text

                c += 1

            yield item

        self.driver.close()