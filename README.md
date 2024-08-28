# Mining Property OLX

## Descrição

O projeto **Mining Property OLX** é uma ferramenta de mineração de dados que coleta informações de imóveis listados no site OLX. Utilizando o Selenium para automação de navegador, o script percorre as páginas fornecidas pelo usuário e extrai dados sobre imóveis, salvando-os em formatos JSON e CSV.

## Funcionalidades

- Coleta de dados de imóveis de várias páginas da OLX.
- Extração de informações como descrição, valor, quartos, banheiros, metros quadrados, vagas de garagem, cidade, bairro e data de postagem.
- Salvamento dos dados coletados em arquivos JSON e CSV.

## Requisitos

Antes de executar o projeto, você precisa instalar as dependências necessárias. Certifique-se de ter o Python instalado.

### Dependências

- Selenium
- WebDriver Manager

## Configuração

Clone o repositório:

```bash
git clone https://github.com/seuusuario/mining-property-olx.git
cd mining-property-olx
```

Instale as dependências:

```bash
pip install selenium webdriver-manager
```

## Uso

Execute o script principal:

```bash
python main.py
```

Siga as instruções fornecidas pelo script:

1. Digite a URL da página da OLX que deseja minerar. Por exemplo: `https://www.olx.com.br/imoveis/venda/casas/estado-ce?o=10`
2. Informe o número de páginas que deseja percorrer a partir da URL fornecida.

O script abrirá o navegador, percorrerá as páginas fornecidas e coletará as informações dos imóveis. Após a coleta, ele salvará os dados em arquivos JSON e CSV na pasta `./file/`.

## Estrutura do Projeto

- `main.py`: Script principal que configura o navegador, coleta dados e salva os resultados.
- `src/web/setup.py`: Configuração e inicialização do navegador usando Selenium.
- `src/data/model.py`: Funções para salvar dados em JSON e CSV e para obter a data e hora atual.
- `src/data/extrator.py`: Funções para extrair dados dos imóveis usando XPath.

## Contato

Para mais informações, entre em contato com seu-email@dominio.com.

---

Certifique-se de substituir `https://github.com/seuusuario/mining-property-olx.git` e `arystotelys@gmail.com.com` com as informações específicas do seu repositório e detalhes de contato.
