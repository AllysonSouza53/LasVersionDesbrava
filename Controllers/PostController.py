from Models.Post import Post
from Helpers.TratamentoErros import Erros as E

class PostController:
    ID = None
    Usuario = None
    Arquivo = None
    Legenda = None
    def __init__(self):
        self.Erros = E()
        self.Post = Post()


    def setNewPost(self, app):
        pass

    def getPost(self):
        return [
            self.ID,
            self.Usuario,
            self.Arquivo,
            self.Legenda
        ]

    def setPost(self, condicao):
        post = self.Post.getPost(condicao)

        if not post:
            print("⚠️ Nenhum post encontrado.")
            return False

        (
            self.ID,
            self.Usuario,
            self.Arquivo,
            self.Legenda
        ) = post
        return True

    def Postar(self):
        try:
            self.Post.setPost(self.getPost())
            resultado = self.Post.Salvar()
            if resultado:
                return True
            return False
        except Exception as e:
            return e

    def PesquisarPorUsuario(self, usuario):
        Resultado = self.Post.Pesquisar('*',f'USUARIO = {usuario}')
        if not Resultado:
            return False
        return Resultado
