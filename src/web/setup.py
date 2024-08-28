from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup():
    options = Options()
    options.add_argument("--disable-dev-shm-usage")  # Para evitar problemas de uso de memória
    options.add_argument("--headless=new")
    
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(service=service)
    return driver