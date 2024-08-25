
import time

from src.web.setup import setup
from src.data.model import salvarJson

from selenium.webdriver.common.by import By

driver = setup()
 
driver.get("https://www.olx.com.br/imoveis/venda/estado-ce/regiao-de-juazeiro-do-norte-e-sobral?o=2")

time.sleep(5)

imoveis = []

try:
    SequenciaNumerica = 1
    while True:
        try:
            xpath = f'//*[@id="main-content"]/div[6]/section[{SequenciaNumerica}]'
            ponteiro = driver.find_element(By.XPATH, xpath)
            titulo = ponteiro.find_element(By.TAG_NAME, 'h2').text
            imoveis.append({"section": SequenciaNumerica, "title": titulo})

            SequenciaNumerica += 1  

        except Exception as e:
            break

    salvarJson(imoveis, 'tentativa01')

except Exception as e:
    print(f"Erro geral: {e}")

driver.quit()
