def formatacao(
    titulo, valor_imovel, banheiros, quartos, vaga_carro, condominio, iptu, metro_quadrado, rua, cep, bairro, cidade, numero, data_postagem
    ):

    resultado = {
        'titulo': titulo,
        'valor_imovel': valor_imovel,
        'banheiros': banheiros,
        'quartos': quartos,
        'vaga_carro': vaga_carro,
        'condominio': condominio,
        'iptu': iptu,
        'metro_quadrado': metro_quadrado,
        'rua': rua,
        'cep': cep,
        'bairro': bairro,
        'cidade': cidade,
        'numero': numero,
        'data_postagem': data_postagem,
    }
    
    return resultado
