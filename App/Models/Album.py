from Banco import Banco
from Helpers.TratamentoErros import Erros

class Album:
    ID = None
    Nome = None
    Usuario = None

    def __init__(self):
        self.TE = Erros()

    def setAlbum(self, dados):
        """
        Define os dados do álbum a partir de uma lista:
        [ID, Nome, Usuario]
        """
        self.Nome = dados[1]
        self.Usuario = dados[2]

    def Salvar(self):
        """
        Salva o álbum no banco de dados.
        """
        if not self.Usuario or not self.Usuario.strip():
            self.TE.SetErro("Usuário vazio!")
        if not self.Nome or not self.Nome.strip():
            self.TE.SetErro("Nome do álbum vazio!")

        if self.TE.TemErros():
            return False

        try:
            colunas = "NOME,USUARIO"
            valores = [self.Nome, self.Usuario]
            Banco.inserir("ALBUNS", colunas, valores)
            return True
        except Exception as e:
            self.TE.SetErro(f"Não foi possível salvar o álbum. Erro: {e}")
            return False

    def Pesquisar(self, rotulo, condicao):
        try:
            return Banco.consultar(f'{rotulo}', 'ALBUNS', f'{condicao}')
        except Exception as e:
            self.TE.SetErro(f"Não foi possível encontrar álbuns. Erro: {e}")
            return False

    def Deletar(self):
        try:
            if not self.ID:
                self.TE.SetErro("ID do álbum não definido!")
                return False
            Banco.excluir('ALBUNS', f'ID = {self.ID}')
            return True
        except Exception as e:
            self.TE.SetErro(f"Não foi possível deletar álbum. Erro: {e}")
            return False

    def getAlbum(self, condicao):
        Resultado = Banco.consultar('*', "ALBUNS", condicao)
        if not Resultado or Resultado is False:
            return False

        try:
            self.ID = Resultado[0][0]
            self.Nome = Resultado[0][1]
            self.Usuario = Resultado[0][2]
            return [self.ID, self.Nome, self.Usuario]
        except Exception as e:
            self.TE.SetErro(f"Erro ao extrair dados do álbum: {e}")
            return False
