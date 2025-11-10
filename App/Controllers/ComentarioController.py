from Models.Comentario import Comentario
from Helpers.TratamentoErros import Erros as E

class ComentarioController:
    ID = None
    Usuario = None
    IDPost = None
    Texto = None

    def __init__(self):
        self.Erros = E()
        self.Comentario = Comentario()

    # 🔹 Define novo comentário
    def setNewComentario(self, app):
        self.Usuario = app.ControlePerfil.Usuario
        self.IDPost = app.post_id
        self.Texto = app.tf.text

    # 🔹 Retorna o comentário atual em formato de lista
    def getComentario(self):
        return [
            self.ID,
            self.Usuario,
            self.IDPost,
            self.Texto
        ]

    # 🔹 Busca um comentário específico
    def setComentario(self, condicao):
        comentario = self.Comentario.getComentario(condicao)

        if not comentario:
            print("⚠️ Nenhum comentário encontrado.")
            return False

        (
            self.ID,
            self.Usuario,
            self.IDPost,
            self.Texto
        ) = comentario
        print(comentario)
        return True

    # 🔹 Salva um novo comentário no banco
    def Comentar(self):
        try:
            self.Comentario.setComentario(self.getComentario())
            resultado = self.Comentario.Salvar()
            if resultado:
                return True
            return False
        except Exception as e:
            return e

    def PesquisarPorUsuario(self, usuario):
        Resultado = self.Comentario.Pesquisar('*', f"USUARIO = '{usuario}'")
        if not Resultado:
            return False
        return Resultado

    def setListaComentarios(self, condicao):
        lista = self.Comentario.ListarComentarios(condicao)
        return lista

    def ExcluirComentario(self):
        try:
            self.setComentario(f"ID = {self.ID}")
            self.Comentario.Deletar()
            return True
        except Exception as e:
            print(e)
            return False
