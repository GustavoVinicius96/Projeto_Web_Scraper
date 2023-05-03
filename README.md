# Projeto Final Python - Web Scraper

Esse projeto é um Web Scraper desenvolvido em Python utilizando Django e a biblioteca BeautifulSoup.

## Instalação

1. Certifique-se de ter o Python 3 instalado.
2. Clone o repositório do projeto:

   ```
   git clone https://github.com/seu-usuario/projeto-final.git
   ```
3. Instale as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```
4. Execute o servidor localmente:

   ```
   python manage.py runserver
   ```

## Como utilizar

1. Acesse a URL `http://localhost:8000/` no navegador.
2. Digite a URL do site que deseja fazer o Web Scraper e clique no botão "Pesquisar".
3. O Web Scraper irá retornar uma lista com os links encontrados na página inicial e nas 5 primeiras páginas de cada link válido.

## Como testar

1. Execute o comando:

   ```
   python manage.py test
   ```
2. Serão executados 3 testes:
   - Teste de conexão com a URL digitada.
   - Teste da função `scrapy`.
   - Teste da página `home.html`.

## Código

### `views.py`

Esse arquivo contém as funções utilizadas no Web Scraper, como `get_links`, `get_valid_links`, `get_sublinks` e `scrapy`, além da função `homepage` utilizada para renderizar a página inicial do projeto.

### `home.html`

Esse arquivo contém o código HTML utilizado na página inicial do projeto.

### `Test_Web_Scraper.py`

Esse arquivo contém os testes automatizados do projeto, incluindo o teste de conexão, teste da função `scrapy` e teste da página `home.html`.

## Tecnologias utilizadas

- Python 3
- Django
- BeautifulSoup
- HTML
- Bootstrap

## Autor

- Gustavo Vinicius Carvalho do Santos
- gkg001@hotmail.com / gustavoviniciuscarvalho@hotmail.com
- Github: GustavoVinicius96

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
