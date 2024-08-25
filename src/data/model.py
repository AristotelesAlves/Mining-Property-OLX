import json
import os

def localArmazenamentoJSON(filename):
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

def salvarJson(data, name):

    localArmazenamentoJSON('./')

    with open(name, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Dados salvos em '{name}'")
