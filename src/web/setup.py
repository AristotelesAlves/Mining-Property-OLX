from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def setup():
    options = Options()
    options.add_argument("--headless")  # Opcional: para rodar o Chrome em modo headless
    options.add_argument("--no-sandbox")  # Necessário para ambientes de CI/CD
    options.add_argument("--disable-dev-shm-usage")  # Para evitar problemas de uso de memória
    options.add_argument("--log-level=0")  # Reduz o nível de log (só erros)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    return driver