import os
import shutil

def criar_diretorio(caminho):
    try:
        os.makedirs(caminho, exist_ok=True)
        print(f"Diretório '{caminho}' criado ou já existia.")
    except Exception as e:
        print(f"Erro ao criar diretório: {e}")

def deletar_diretorio(caminho):
    try:
        shutil.rmtree(caminho)
        print(f"Diretório '{caminho}' deletado com sucesso.")
    except FileNotFoundError:
        print(f"Diretório '{caminho}' não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar diretório: {e}")

def listar_diretorios(caminho):
    try:
        return [item for item in os.listdir(caminho) if os.path.isdir(os.path.join(caminho, item))]
    except Exception as e:
        print(f"Erro ao listar diretórios: {e}")

def listar_arquivos(caminho):
    try:
        return [item for item in os.listdir(caminho) if os.path.isfile(os.path.join(caminho, item))]
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")

def mover_diretorio(origem, destino):
    try:
        shutil.move(origem, destino)
        print(f"Diretório movido de '{origem}' para '{destino}'.")
    except Exception as e:
        print(f"Erro ao mover diretório: {e}")

def copiar_diretorio(origem, destino):
    try:
        shutil.copytree(origem, destino)
        print(f"Diretório copiado de '{origem}' para '{destino}'.")
    except Exception as e:
        print(f"Erro ao copiar diretório: {e}")