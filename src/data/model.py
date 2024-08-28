import json
import csv
from datetime import datetime



def DataHoraAtual():
    return datetime.now().strftime('%d-%m-%Y %H-%M')

def salvarJson(data):
    data_e_hora_atual = DataHoraAtual()
    with open(f'./file/json/imoveis-{data_e_hora_atual}.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def salvarCSV(imoveis):
    data_e_hora_atual = DataHoraAtual()
    with open(f'./file/csv/imoveis-{data_e_hora_atual}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id','descriçao','Tipo', 'valor', 'quartos', 'banheiros', 'metros_quadrados', 'vagas_carro', 'cidade','bairro','data de postagem']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for imovel in imoveis:
            writer.writerow(imovel)
