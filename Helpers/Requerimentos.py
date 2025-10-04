import requests
import pandas as pd

class Cidades:
    def __init__(self):
        pass

    def get_cidades_por_uf(self, uf):
        print("DEBUG - Valor recebido de UF:", repr(uf))
        if not uf:  # se for None ou vazio
            print("UF não informada!")
            return []

        uf = uf.strip().upper()
        url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{uf}/municipios"
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        municipios = resp.json()
        return [m['nome'] for m in municipios]

    def get_codigo_municipio(self,uf: str, nome_cidade: str):
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


class Escolas:
    def __init__(self):
        self.url = 'https://448294cd-b66b-4878-b5b5-9e1623ce0ee7-00-2fuf8fe4rqnbi.riker.replit.dev'

    def Get(self, uf, cidade):
        try:
            resp = requests.get(f'{self.url}/{uf.upper().strip()}/municipios/{cidade.upper().strip()}/escolas', timeout=10)
            if resp.status_code == 200:
                return resp.json()
            return []
        except requests.exceptions.RequestException as e:
            print("Erro ao buscar escolas:", e)
            return None

    def GetPorEscola(self, uf, cidade, escola):
        try:
            resp = requests.get(f'{self.url}/{uf.upper().strip()}/municipios/{cidade.upper().strip()}/escolas/{escola.upper().strip()}', timeout=10)
            if resp.status_code == 200:
                return resp.json()
            return []
        except requests.exceptions.RequestException as e:
            print("Erro ao buscar escola:", e)
            return []

    def Post(self, id, uf, cidade, escola):
        novaescola = {
            'id': id,
            'uf': uf.upper().strip(),
            'cidade': cidade.upper().strip(),
            'escola': escola.upper().strip()
        }
        try:
            resp = requests.post(f'{self.url}/{uf.upper().strip()}/municipios/{cidade.upper().strip()}/escolas', json=novaescola, timeout=10)
            resp.raise_for_status()
            print("Escola adicionada com sucesso!")
            return resp.json()
        except requests.exceptions.RequestException as e:
            print("Erro ao adicionar escola:", e)
            return None

    def Update(self, id, uf, cidade, escola):
        atualizando = {
            'id': id,
            'uf': uf.upper().strip(),
            'cidade': cidade.upper().strip(),
            'escola': escola.upper().strip()
        }
        try:
            resp = requests.put(f'{self.url}/{uf.upper().strip()}/municipios/{cidade.upper().strip()}/escolas/{escola.upper().strip()}', json=atualizando, timeout=10)
            resp.raise_for_status()
            print("Atualizado com sucesso!")
            return resp.json()
        except requests.exceptions.RequestException as e:
            print("Erro ao atualizar escola:", e)
            return None

    def Delete(self, uf, cidade, escola):
        try:
            resp = requests.delete(f'{self.url}/{uf.upper().strip()}/municipios/{cidade.upper().strip()}/escolas/{escola.upper().strip()}', timeout=10)
            resp.raise_for_status()
            print("Escola deletada com sucesso!")
            return resp.status_code
        except requests.exceptions.RequestException as e:
            print("Erro ao deletar escola:", e)
            return None

class Perfis:
    def __init__(self):
        self.url = 'https://448294cd-b66b-4878-b5b5-9e1623ce0ee7-00-2fuf8fe4rqnbi.riker.replit.dev'

    def Get(self):
        try:
            resp = requests.get(f'{self.url}/Perfis', timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            print("Erro ao buscar perfis:", e)
            return None

    def GetPorUsuario(self, usuario):
        try:
            resp = requests.get(f'{self.url}/Perfis/{usuario}', timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar perfil do usuário {usuario}:", e)
            return None

    def Post(self, CPF, usuario, imagem):
        perfil_data = {
            'usuario': usuario,
            'CPF': CPF,
            'imagem': imagem
        }
        try:
            resp = requests.post(f'{self.url}/Perfil', json=perfil_data, timeout=10)
            resp.raise_for_status()
            print("Perfil adicionado com sucesso!")
            return resp.json()
        except requests.exceptions.RequestException as e:
            print("Erro ao adicionar perfil:", e)
            return None

    def Update(self, CPF, usuario, imagem):

        perfil_alterado = {
            'usuario': usuario,
            'CPF': CPF,
            'imagem': imagem
        }
        try:
            resp = requests.put(f'{self.url}/Perfis/{usuario}', json=perfil_alterado, timeout=10)
            resp.raise_for_status()
            print("Perfil atualizado com sucesso!")
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao atualizar perfil do usuário {usuario}:", e)
            return None

    def Delete(self, usuario):
        try:
            resp = requests.delete(f'{self.url}/Perfis/{usuario}', timeout=10)
            resp.raise_for_status()
            print("Perfil deletado com sucesso!")
            return resp.status_code
        except requests.exceptions.RequestException as e:
            print(f"Erro ao deletar perfil do usuário {usuario}:", e)
            return None

class Posts:
    def __init__(self):
        self.url = 'https://448294cd-b66b-4878-b5b5-9e1623ce0ee7-00-2fuf8fe4rqnbi.riker.replit.dev'

    def Get(self):
        try:
            resp = requests.get(f'{self.url}/Posts', timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            print("Erro ao buscar posts:", e)
            return None

    def GetPorUsuario(self, usuario):
        try:
            resp = requests.get(f'{self.url}/Posts/{usuario}', timeout=10)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar posts do usuário {usuario}:", e)
            return None

    def Post(self, id, usuario, imagem, legenda):
        post_data = {
            'id': id,
            'usuario': usuario,
            'legenda': legenda,
            'imagem': imagem
        }
        try:
            resp = requests.post(f'{self.url}/Posts', json=post_data, timeout=10)
            resp.raise_for_status()
            print("Post adicionado com sucesso!")
            return resp.json()
        except requests.exceptions.RequestException as e:
            print("Erro ao adicionar post:", e)
            return None

    def Update(self, id, usuario, imagem, legenda):
        post_alterado = {
            'usuario': usuario,
            'legenda': legenda,
            'imagem': imagem
        }
        try:
            resp = requests.put(f'{self.url}/Posts/{id}', json=post_alterado, timeout=10)
            resp.raise_for_status()
            print("Post atualizado com sucesso!")
            return resp.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao atualizar post id {id}:", e)
            return None

    def Delete(self, id):
        try:
            resp = requests.delete(f'{self.url}/Posts/{id}', timeout=10)
            resp.raise_for_status()
            print("Post deletado com sucesso!")
            return resp.status_code
        except requests.exceptions.RequestException as e:
            print(f"Erro ao deletar post id {id}:", e)
            return None