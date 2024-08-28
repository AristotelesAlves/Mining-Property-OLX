from selenium.webdriver.common.by import By
from datetime import datetime, timedelta

def extrator(ponteiro):

    dados = {}

    try:
        dados["descriçao"] = ponteiro.find_element(By.XPATH, './/h2').text
    except:
        dados["descriçao"] = None

    try:
        valor = ponteiro.find_element(By.XPATH, './/div[2]/div[1]/div[2]/h3').text
        dados["valor"] = valor.split(' ', 1)[-1]
    except:
        dados["valor"] = None

    try:
        lista = ponteiro.find_element(By.XPATH, './/div[2]/div[1]/div[1]/ul[1]')
        dados["quartos"] = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "quartos")]]').text.split('+')[0]
        dados["banheiros"] = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "banheiro")]]').text.split('+')[0]
        dados["metros_quadrados"] = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "metros quadrados")]]').text.split('m²')[0]
        dados["vagas_carro"] = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "vaga de garagem")]]').text.split('+')[0]
    except:
        dados.update({"quartos": None, "banheiros": None, "metros_quadrados": None, "vagas_carro": None})

    try:
        endereço = ponteiro.find_element(By.XPATH, './/div[2]/div[2]/div/div/div[1]/p').text
        if ',' in endereço:
            dados["cidade"], dados["bairro"] = endereço.split(',', 1)
        else:
            dados["cidade"] = endereço
            dados["bairro"] = None
    except:
        dados.update({"cidade": None, "bairro": None})

    try:
        dataPostagem = ponteiro.find_element(By.XPATH, './/div[2]/div[2]/div/div/div[2]/p').text
        dia, hora = dataPostagem.split(',')
        if dia == 'Hoje':
            dados["data de postagem"] = datetime.now().strftime('%d-%m-%Y ') + hora
        elif dia == 'Ontem':
            dados["data de postagem"] = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y ') + hora
        else:
            dia = datetime.strptime(f"{dia} {hora}", '%d de %b %H:%M').strftime('%d-%m-%Y')
            dados["data de postagem"] = dia + hora
    except:
        dados["data de postagem"] = None

    return dados