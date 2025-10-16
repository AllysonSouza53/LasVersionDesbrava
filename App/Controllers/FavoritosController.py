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
        self.PostID = app.post_id
        self.Usuario = app.ControlePerfil.Usuario
        self.AlbumID = None

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
        print(favorito)
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

    def setListaFavoritos(self, condicao):
        lista = self.Favoritos.ListarFavoritos(condicao)
        return lista

    def Desfavoritar(self):
        try:
            self.setFavorito(f"ID_POST = {self.PostID} AND USUARIO = '{self.Usuario}'")
            self.Favoritos.Deletar()
            return True
        except Exception as e:
            print(e)
            return False

