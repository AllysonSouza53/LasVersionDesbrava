import os

def ler_arquivo(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

def escrever_arquivo(caminho_arquivo, texto):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
            arquivo.write(texto)
    except Exception as e:
        print(f"Erro ao escrever no arquivo: {e}")

def adicionar_ao_arquivo(caminho_arquivo, texto):
    try:
        with open(caminho_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(texto)
    except Exception as e:
        print(f"Erro ao adicionar ao arquivo: {e}")

def ler_linhas(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            return arquivo.readlines()
    except Exception as e:
        print(f"Erro ao ler linhas do arquivo: {e}")

def deletar_arquivo(caminho_arquivo):
    try:
        os.remove(caminho_arquivo)
        print(f"Arquivo '{caminho_arquivo}' deletado com sucesso.")
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar arquivo: {e}")

def listar_arquivos_diretorio(diretorio):
    try:
        return os.listdir(diretorio)
    except FileNotFoundError:
        print(f"Diretório '{diretorio}' não encontrado.")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")