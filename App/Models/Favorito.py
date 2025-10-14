from App.Banco import Banco
from App.Helpers.TratamentoErros import Erros

class Favorito:
    ID = None
    Usuario = None
    PostID = None
    DataFavorito = None

    def __init__(self):
        self.TE = Erros()

    def setFavorito(self, dados):
        self.ID = dados[0]
        self.Usuario = dados[1]
        self.PostID = dados[2]
        self.DataFavorito = dados[3]

    def Salvar(self):
        if not self.Usuario or not self.Usuario.strip():
            self.TE.SetErro("Usuário vazio!")
        if not self.PostID:
            self.TE.SetErro("Post não definido para favoritar!")
        if self.TE.TemErros():
            return False
        try:
            colunas = "Usuario,PostID,DataFavorito"
            valores = [self.Usuario, self.PostID, self.DataFavorito]
            Banco.inserir("FAVORITOS", colunas, valores)
            return True
        except Exception as e:
            self.TE.SetErro(f"Não foi possível salvar o favorito. Erro: {e}")
            return False

    def Pesquisar(self, rotulo, condicao):
        try:
            return Banco.consultar(f'{rotulo}', 'FAVORITOS', f'{condicao}')
        except Exception as e:
            self.TE.SetErro(f"Não foi possível encontrar favoritos. Erro: {e}")
            return False

    def Deletar(self):
        if not self.ID:
            self.TE.SetErro("ID do favorito não definido!")
            return False
        try:
            Banco.excluir('FAVORITOS', f'ID = {self.ID}')
            return True
        except Exception as e:
            self.TE.SetErro(f"Não foi possível deletar favorito. Erro: {e}")
            return False

    def getFavorito(self, condicao):
        Resultado = Banco.consultar('*', "FAVORITOS", condicao)
        if not Resultado or Resultado is False:
            return False
        try:
            self.ID = Resultado[0][0]
            self.Usuario = Resultado[0][1]
            self.PostID = Resultado[0][2]
            self.DataFavorito = Resultado[0][3]
            return [self.ID, self.Usuario, self.PostID, self.DataFavorito]
        except Exception as e:
            self.TE.SetErro(f"Erro ao extrair dados do favorito: {e}")
            return False
