import os
from selenium.webdriver.common.by import By
from src.web.setup import setup
from src.data.model import salvarJson, salvarCSV, DataHoraAtual
from src.data.extrator import extrator
from public.logoOLX import OLX
from public.minhaMarca import marca

def carregamentoPonteiro(SequenciaNumerica):
    
        if(SequenciaNumerica % 2 == 0):
            return '/'
        else:
            return '\\'


def main():
    
    driver = setup()
    imoveis = []
    
    print('\x1b[35m-----------------------------------------------------')
    print('Olá, Bem-vindo ao Mining Property OLX!')
    print('-----------------------------------------------------')
    
    urlUsuario = input('Digite a URL da página: ')
    totalPagina = int(input('Número de páginas: '))

    for paginaAtual in range(totalPagina):

        url = f"{urlUsuario}{paginaAtual + 1}"
        driver.get(url)

        SequenciaNumerica = 1

        while True:
            try:
                os.system('cls')
                print(OLX)
                print(f'\x1b[35mPagina {paginaAtual + 1} de {totalPagina} {carregamentoPonteiro(SequenciaNumerica)}')
                xpath_section = f'//*[@id="main-content"]/div[6]/section[{SequenciaNumerica}]'
                ponteiro = driver.find_element(By.XPATH, xpath_section)
                dados_imovel = extrator(ponteiro)
                dados_imovel.update({"id": SequenciaNumerica, "Tipo": 'casa'})
                imoveis.append(dados_imovel)
                SequenciaNumerica += 1
            except:
                break

    driver.quit()
    
    if imoveis:
        os.system('cls')
        salvarJson(imoveis)
        salvarCSV(imoveis)
        print()
        print(marca)
        print("Mining finalizado com sucesso!")
        print(f"Totalizando {len(imoveis)} anúncios")
        print()
        print("\x1b[35m|----------------------------------------------------------|")
        print(f"\x1b[35m| CSV salvo em ./file/csv/imoveis{DataHoraAtual()}.csv      |")
        print(f"| JSON salvo em ./file/json/imoveis{DataHoraAtual()}.json   |")
        print("\x1b[35m|----------------------------------------------------------|")
        print()
    else:
        print("Error: Nenhum dado encontrado!")

if __name__ == "__main__":
    main()
