import time
from selenium.webdriver.common.by import By
from src.web.setup import setup
from src.data.model import salvarJson, salvarCSV

driver = setup()
driver.get("https://www.olx.com.br/imoveis/venda/estado-ce/regiao-de-juazeiro-do-norte-e-sobral?o=2")

time.sleep(5)

imoveis = []

try:
    SequenciaNumerica = 1
    while True:
        try:
            xpath_section = f'//*[@id="main-content"]/div[6]/section[{SequenciaNumerica}]'
            ponteiro = driver.find_element(By.XPATH, xpath_section)

            titulo = ponteiro.find_element(By.XPATH, './/h2').text 

            try:
                valor = ponteiro.find_element(By.XPATH, './/div[2]/div[1]/div[2]/h3').text
            except:
                valor = None

            try:
                lista = ponteiro.find_element(By.XPATH, './/div[2]/div[1]/div[1]/ul[1]')
            
                quartos = None
                banheiros = None
                metros_quadrados = None
                vagas_carro = None
                
                quartos = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "quartos")]]').text
                banheiros = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "banheiro")]]').text         
                metros_quadrados = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "metros quadrados")]]').text    
                vagas_carro = lista.find_element(By.XPATH, './/span[@aria-label[contains(., "vaga de garagem")]]').text
                
            except:
                print('Erro ao capturar informações adicionais:')

            try:
                endereço = ponteiro.find_element(By.XPATH, './/div[2]/div[2]/div/div/div[1]/p').text
            except:
                print('Erro ao capturar informações adicionais:')

            try:
                dataPostagem = ponteiro.find_element(By.XPATH, './/div[2]/div[2]/div/div/div[2]/p').text
            except:
                print('Erro ao capturar informações adicionais:')


            imoveis.append({
                "section": SequenciaNumerica,
                "title": titulo,
                "valor": valor,
                "quartos": quartos,
                "banheiros": banheiros,
                "metros_quadrados": metros_quadrados,
                "vagas_carro": vagas_carro,
                "endereço":endereço,
                "data de postagem":dataPostagem
            })

            SequenciaNumerica += 1  

        except:
            break

    salvarJson(imoveis)
    salvarCSV(imoveis)

except Exception as e:
    print(f"Erro geral: {e}")

driver.quit()
