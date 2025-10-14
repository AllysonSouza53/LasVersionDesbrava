from App.Models.Favorito import Favorito
from App.Helpers.TratamentoErros import Erros as E

class FavoritosController:
    ID = None
    Usuario = None
    PostID = None
    AlbumID = None

    def __init__(self):
        self.Erros = E()
        self.Favoritos = Favorito()

    def setNewFavorito(self, app):
        pass

    def getFavorito(self):
        return [
            self.ID,
            self.Usuario,
            self.PostID,
            self.AlbumID
        ]

    def setFavorito(self, condicao):
        favorito = self.Favoritos.getFavorito(condicao)

        if not favorito:
            print("⚠️ Nenhum favorito encontrado.")
            return False

        (
            self.ID,
            self.Usuario,
            self.PostID,
            self.AlbumID
        ) = favorito
        return True

    def Favoritar(self):
        try:
            self.Favoritos.setFavorito(self.getFavorito())
            resultado = self.Favoritos.Salvar()
            if resultado:
                return True
            return False
        except Exception as e:
            return e

    def PesquisarPorUsuario(self, usuario):
        Resultado = self.Favoritos.Pesquisar('*', f'USUARIO = {usuario}')
        if not Resultado:
            return False
        return Resultado
