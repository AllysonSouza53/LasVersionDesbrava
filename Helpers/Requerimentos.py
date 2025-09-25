import requests
import pandas as pd

def get_cidades_por_uf(uf = None):
    print("(:")
    uf = uf.strip().upper()
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()  # lança exceção se HTTP != 200
    municipios = resp.json()  # lista de objetos
    # extrair só os nomes
    nomes = [m['nome'] for m in municipios]
    return nomes


def get_escolas(uf: str, nome_cidade: str, arquivo_csv: str):
    df = pd.read_csv(arquivo_csv, sep=';', encoding='ISO-8859-1', dtype={32: str})
    escolas = df[(df['SG_UF'].str.upper() == uf.upper()) & (df['NO_MUNICIPIO'].str.upper() == nome_cidade.upper())]
    nomes = escolas['NO_ENTIDADE'].tolist()
    print(escolas)
    print(nomes)
    return nomes

def get_codigo_municipio(uf: str, nome_cidade: str):
    uf = uf.strip().upper()
    nome_cidade = nome_cidade.strip().lower()
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    municipios = resp.json()
    for m in municipios:
        if m['nome'].strip().lower() == nome_cidade:
            return m['id']
    return None