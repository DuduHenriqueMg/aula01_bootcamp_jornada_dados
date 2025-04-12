import csv
import os

def ler_csv(caminho_arquivo: str) -> list:
    dados: list = []
   
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)

        for linha in leitor_csv:
            dados.append(linha)
       
    return dados     
            
def processar_dados(lista: list) -> dict:
    dicionario_processado: dict = {}
    
    for item in lista:
        dicionario_processado[item["Categoria"]] =  {key: value for key,value in item.items() if key != 'Categoria'}
        
    return dicionario_processado

def calcular_total_vendas(dicionario_processado: dict) -> dict:
    totais_categoria: dict = {}
    
    for key, value in dicionario_processado.items():
        totais_categoria[key] = float(value['Quantidade']) * float(value['Venda'])
        
    return totais_categoria

def main() -> None:
    caminho_arquivo: str = os.path.join(os.path.dirname(__file__), 'datasets/vendas.csv')
    vendas: list = ler_csv(caminho_arquivo)
    vendas_processadas: dict = processar_dados(vendas)
    totais_categoria: dict = calcular_total_vendas(vendas_processadas)
    
    for key, value in totais_categoria.items():
        print(f"O valor total de vendas da categoria {key} foi de {value:.2f}")
        
if __name__ == "__main__":
    main()