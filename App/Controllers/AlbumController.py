from Models.Album import Album
from Helpers.TratamentoErros import Erros

class AlbumController:
    ID = None
    Nome = None
    Usuario = None
    Albuns = None

    def __init__(self):
        self.Erros = Erros()
        self.Album = Album()

    def setNewAlbum(self, app):
        self.Usuario = app.ProfissionalControle.Usuario
        self.Nome = app.NomeAlbumTextField.text

    def getAlbum(self):
        return [
            self.ID,
            self.Nome,
            self.Usuario
        ]

    def setAlbum(self, condicao):
        album = self.Album.getAlbum(condicao)
        if not album:
            print("⚠️ Nenhum álbum encontrado.")
            return False

        self.ID, self.Nome, self.Usuario = album
        return True

    def Salvar(self):
        try:
            self.Album.setAlbum(self.getAlbum())
            resultado = self.Album.Salvar()
            if resultado:
                self.ID = self.Album.Pesquisar('ID', f"USUARIO = '{self.Usuario}' ORDER BY ID DESC")[0][0]
                self.Albuns.Album(
                    self.ID,
                    self.Usuario
                )
                return True
            return False
        except Exception as e:
            print(f"Erro ao salvar álbum: {e}")
            return False

    def ListarAlbumPorUsuario(self, usuario):
        try:
            Resultado = self.Album.Pesquisar('*', f"USUARIO = '{usuario}' ORDER BY ID DESC")
            if not Resultado:
                return []

            lista = []
            for alb in Resultado:
                lista.append({
                    "id": alb[0],
                    "nome": alb[1],
                    "usuario": alb[2]
                })
            return lista
        except Exception as e:
            print(f"Erro ao listar álbuns do usuário {usuario}: {e}")
            return []

    def PesquisarPorID(self, id):
        Resultado = self.Album.Pesquisar('*', f'ID = {id}')
        if not Resultado:
            return False
        return Resultado

    def ListarAlbumPorID(self, ids):
        lista = []
        for id in ids:
            Resultado = self.PesquisarPorID(id)
            if Resultado and isinstance(Resultado, list):
                for alb in Resultado:
                    try:
                        lista.append({
                            "id": alb[0],
                            "nome": alb[1],
                            "usuario": alb[2]
                        })
                    except IndexError:
                        print(f"⚠️ Dados incompletos para o álbum com ID {id}.")
                        pass
        return lista