import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Projeto_Final.settings')

from django.test import TestCase
from requests import get
from .views import scrapy


class ScrapyTestCase(TestCase):
    def test_scrapy(self):
        url = "https://www.terra.com.br"
        links = scrapy(url)
        print(links)

    def test_conexao(self):
        url = "https://www.terra.com.br"
        resp = get(url)
        self.assertTrue(resp.ok)

    def test_funcao(self):
        url = "https://www.terra.com.br"
        resp = get(url)
        resultado = scrapy(url)
        self.assertTrue(resultado)
