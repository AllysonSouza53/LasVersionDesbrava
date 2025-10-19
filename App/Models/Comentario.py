from Banco import Banco
from Helpers.TratamentoErros import Erros

class Comentario:
    ID = None
    Usuario = None
    IDPost = None
    Texto = None

    def __init__(self):
        self.TE = Erros()

    def setComentario(self, dados):
        """
        Recebe uma lista/tupla: [ID, IDUsuario, IDPost, Texto]
        """
        self.ID = dados[0]
        self.Usuario = dados[1]
        self.IDPost = dados[2]
        self.Texto = dados[3]

    def Salvar(self):
        if not self.Usuario or not str(self.Usuario).strip():
            self.TE.SetErro("Usuário do comentário vazio!")
        if not self.IDPost:
            self.TE.SetErro("Post não definido para comentar!")
        if not self.Texto or not self.Texto.strip():
            self.TE.SetErro("Texto do comentário vazio!")
        if self.TE.TemErros():
            return False
        try:
            colunas = "USUARIO,IDPOST,TEXTO"
            valores = [self.Usuario, self.IDPost, self.Texto]
            Banco.inserir("COMENTARIOS", colunas, valores)
            return True
        except Exception as e:
            self.TE.SetErro(f"Não foi possível salvar o comentário. Erro: {e}")
            return False

    def Pesquisar(self, rotulo, condicao):
        try:
            return Banco.consultar(f'{rotulo}', 'COMENTARIOS', f'{condicao}')
        except Exception as e:
            self.TE.SetErro(f"Não foi possível encontrar comentários. Erro: {e}")
            return False

    def Deletar(self):
        if not self.ID:
            self.TE.SetErro("ID do comentário não definido!")
            return False
        try:
            Banco.excluir('COMENTARIOS', f'ID = {self.ID}')
            return True
        except Exception as e:
            self.TE.SetErro(f"Não foi possível deletar comentário. Erro: {e}")
            return False

    def getComentario(self, condicao):
        Resultado = Banco.consultar('*', "COMENTARIOS", condicao)
        if not Resultado or Resultado is False:
            return False
        try:
            self.ID = Resultado[0][0]
            self.Usuario = Resultado[0][1]
            self.IDPost = Resultado[0][2]
            self.Texto = Resultado[0][3]
            return [self.ID, self.Usuario, self.IDPost, self.Texto]
        except Exception as e:
            self.TE.SetErro(f"Erro ao extrair dados do comentário: {e}")
            return False

    def ListarComentarios(self, condicao):
        Resultado = Banco.consultar('*', "COMENTARIOS", condicao)
        if not Resultado or Resultado is False:
            return False
        try:
            comentarios = []
            for linha in Resultado:
                ID = linha[0]
                Usuario = linha[1]
                IDPost = linha[2]
                Texto = linha[3]
                comentarios.append({
                    "ID": ID,
                    "Usuario": Usuario,
                    "IDPost": IDPost,
                    "Texto": Texto
                })
            return comentarios
        except Exception as e:
            self.TE.SetErro(f"Erro ao extrair dados do comentário: {e}")
            return False
