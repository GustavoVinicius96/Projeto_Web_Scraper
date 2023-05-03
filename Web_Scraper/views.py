import re
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render


def get_links(url, limit=10):
    links = []
    resposta = requests.get(url)
    tag = BeautifulSoup(resposta.text, "html.parser")
    Linkspagina = tag.find_all('a', href=True, limit=limit)
    for link in Linkspagina:
        links.append(link['href'])

    return links


def get_valid_links(links):
    valid_links = []
    for link in links:
        if re.findall(r'https?://(www\.)?([a-zA-z0-9]+\.)+(com|com.br)', str(link)):
            valid_links.append(link)

    return valid_links

def get_sublinks(links, limit=5):
    sublinks = []
    for link in links:
        lista_sublinks = []
        response = requests.get(link)
        tag = BeautifulSoup(response.text, "html.parser")
        link_tags = tag.find_all('a', href=True, limit=limit)
        for sublink in link_tags:
            lista_sublinks.append(sublink['href'])

        sublinks.extend(get_valid_links(lista_sublinks))

    return sublinks


def scrapy(url):
    lista_fixa = get_valid_links(get_links(url))
    lista_sublinks = get_sublinks(lista_fixa)

    # Adiciona os sublinks encontrados à lista fixa
    lista_fixa.extend(lista_sublinks)

    # Remove links repetidos
    lista_nova = list(set(lista_fixa))

    return lista_nova


def homepage(request):
    context = {}
    if request.method == "POST":
        url = request.POST.get('url', None)
        links = scrapy(url)
        context['links'] = links
    return render(request, 'home.html', context=context)
