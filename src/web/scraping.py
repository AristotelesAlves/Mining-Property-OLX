from selenium.webdriver.common.by import By

def scraping(driver, numero, imoveis):
    xpath = f'//*[@id="main-content"]/div[6]/section[{numero}]'
    if(driver.find_element(By.XPATH, xpath)):
        ponteiro = driver.find_element(By.XPATH, xpath)
        titulo = ponteiro.find_element(By.TAG_NAME, 'h2').text

        imoveis.append({"section": numero, "title": titulo})
