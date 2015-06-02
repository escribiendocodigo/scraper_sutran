# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SutranItem(scrapy.Item):
    # define the fields for your item here like:
    nro_papeleta = scrapy.Field()
    fecha_infraccion = scrapy.Field()
    infraccion = scrapy.Field()
    region = scrapy.Field()
    placa = scrapy.Field()
    conductor = scrapy.Field()
    licencia = scrapy.Field()
    estado_actual = scrapy.Field()
    pass