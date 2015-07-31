# -*- coding: utf-8 -*-

import scrapy

class Products(scrapy.Item):
    """item parser class"""
    def __init__(self):
        """initial some constants"""
        self.start_url = ["www.dxomark.com/http://www.dxomark.com/Lenses#year=1987%2C2015&price=0%2C13000&xDataType=year&yDataType=global&viewMode=list"]
        self.allow_domains = ["dxomark.com"]
        self.name = "dxospider"
        self.brand = ["Canon", "Panasonic", "Samsung", "Konica Minolta", "Nikon", "Leica", "Carl Zeiss",
                      "Richo", "Tamron", "Pentax", "Samyang", "Fujifilm", "Sony", "Olympus", "Sigma", "Kenko Tokina",
                      "Schneider Kreuznach", "Lensbaby", "Lomograph", "Mitakon", "Noktor", "Voigtlander"]

    def parse(self, response):
        """get items"""
        for sel in response.xpath():


