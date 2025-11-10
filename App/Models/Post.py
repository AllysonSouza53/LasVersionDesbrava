from Banco import Banco
from Helpers.TratamentoErros import Erros

class Post:
    ID = None
    Usuario = None
    Arquivo = None
    Legenda = None

    def __init__(self):
        self.TE = Erros()

    def setPost(self, dados):
        self.Usuario = dados[1]
        self.Legenda = dados[3]

    def Salvar(self):
        """
        Valida e insere o post no banco de dados.
        """
        print("== Iniciando Salvar Post ==")
        print("Dados recebidos:", self.Usuario, self.Legenda)

        # Validações básicas
        if not self.Usuario or not self.Usuario.strip():
            print("Erro: Usuário vazio")
            self.TE.SetErro("Usuário vazio!")

        if not self.Legenda or not self.Legenda.strip():
            print("Erro: Legenda vazia")
            self.TE.SetErro("Legenda vazia!")

        print("Erros acumulados até aqui:", self.TE.GetErros())

        if self.TE.TemErros():
            print("Abandonando Salvar Post porque há erros")
            return False

        try:
            print("Tentando inserir post no banco...")
            colunas = "USUARIO,LEGENDA"
            valores = [self.Usuario, self.Legenda]
            Banco.inserir("POST", colunas, valores)
            print("Post inserido com sucesso!")
            return True
        except Exception as e:
            print("Erro ao inserir post no banco:", e)
            self.TE.SetErro(f"Não foi possível salvar o post. Erro: {e}")
            return False

    def Pesquisar(self, rotulo, condicao):
        try:
            return Banco.consultar(f'{rotulo}', 'POST', f'{condicao}')
        except Exception as e:
            self.TE.SetErro(f"Não foi possível encontrar posts. Erro: {e}")
            return False

    def Deletar(self):
        """
        Deleta um post do banco com base no ID.
        """
        try:
            if not self.ID:
                self.TE.SetErro("ID do post não definido!")
                return False
            Banco.excluir('POST', f'ID = {self.ID}')
            print("Post deletado com sucesso!")
            return True
        except Exception as e:
            self.TE.SetErro(f"Não foi possível deletar post. Erro: {e}")
            print(f"Erro ao deletar post: {e}")
            return False

    def getPost(self, condicao):
        """
        Busca um post específico e preenche os atributos da instância.
        """
        Resultado = Banco.consultar('*', "POST", condicao)

        if not Resultado or Resultado is False:
            print("Nenhum post encontrado ou erro na consulta.")
            return False

        try:
            self.ID = Resultado[0][0]
            self.Usuario = Resultado[0][1]
            self.Arquivo = Resultado[0][2]
            self.Legenda = Resultado[0][3]

            return [self.ID, self.Usuario, self.Arquivo, self.Legenda]

        except Exception as e:
            print(f"Erro ao extrair dados do post: {e}")
            return False
