import time
from selenium.webdriver.common.by import By
from src.web.setup import setup
from src.data.model import salvarJson, salvarCSV
from datetime import datetime, timedelta

driver = setup()

imoveis = []
paginaAtual = 0
totalPagina = 100

try:
    for paginaAtual in range(totalPagina):
        url = f'https://www.olx.com.br/imoveis/venda/estado-ce?o={paginaAtual + 1}'
        
        driver.get(url)
        SequenciaNumerica = 1
        while True:
            try:
                xpath_section = f'//*[@id="main-content"]/div[6]/section[{SequenciaNumerica}]'
                
                ponteiro = driver.find_element(By.XPATH, xpath_section)
                titulo = ponteiro.find_element(By.XPATH, './/h2').text 
                
                valor = None
                try:
                    valor = ponteiro.find_element(By.XPATH, './/div[2]/div[1]/div[2]/h3').text
                    _, valor = valor.split(' ')
                except:
                    None

                quartos, banheiros, metros_quadrados, vagas_carro = None, None, None, None
                try:
                    lista = ponteiro.find_element(By.XPATH, './/div[2]/div[1]/div[1]/ul[1]')
                    quartos = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "quartos")]]').text.split('+')[0]
                    banheiros = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "banheiro")]]').text.split('+')[0]
                    metros_quadrados = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "metros quadrados")]]').text.split('m²')[0]
                    vagas_carro = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "vaga de garagem")]]').text.split('+')[0]
                except:
                    None

                cidade, bairro = None, None
                try:
                    endereço = ponteiro.find_element(By.XPATH, './/div[2]/div[2]/div/div/div[1]/p').text
                    cidade, bairro = endereço.split(',')
                except:
                    None

                dia, hora = None, None
                try:
                    dataPostagem = ponteiro.find_element(By.XPATH, './/div[2]/div[2]/div/div/div[2]/p').text
                    dia, hora = dataPostagem.split(',')
                    if dia == 'Hoje':
                        dia = datetime.now().strftime('%d-%m-%Y ')
                    elif dia == 'Ontem':
                        dia = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y ')
                    else:
                         dia = datetime.strptime(f"{dia} {hora}", '%d de %b %H:%M').strftime('%d-%m-%Y')
                except:
                    None

                imoveis.append({
                    "section": SequenciaNumerica,
                    "title": titulo,
                    "valor": valor,
                    "quartos": quartos,
                    "banheiros": banheiros,
                    "metros_quadrados": metros_quadrados,
                    "vagas_carro": vagas_carro,
                    "cidade": cidade,
                    "bairro": bairro,
                    "data de postagem": dia + hora
                })

                SequenciaNumerica += 1  

            except:
                break

        salvarJson(imoveis, paginaAtual)
        salvarCSV(imoveis, paginaAtual)
        imoveis = []
        paginaAtual += 1
        time.sleep(10)

except:
    None

driver.quit()

print('Acabou')
print('Acabou')
print('Acabou')
print('Acabou')
print('Acabou')
print('Acabou')
print('Acabou')
print('Acabou')
print('Acabou')
