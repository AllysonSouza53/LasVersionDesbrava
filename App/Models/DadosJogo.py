from Banco import Banco
from Helpers.TratamentoErros import Erros

class DadosJogo:
    ID = None
    ID_ALUNO = None
    USUARIO_PROFISSIONAL = None
    NOME_JOGO = None
    ID_FASE = None
    ID_NIVEL = None
    PONTUACAO = None
    PORCENTAGEM_COMPLETADA = None
    TEMPO_GASTO = None
    ACERTOS = None
    ERROS = None
    TENTATIVAS = None
    DATA_REGISTRO = None

    def __init__(self):
        self.TE = Erros()

    def setDadoJogo(self, dados):
        """
        Recebe uma lista/tupla:
        [ID, ID_ALUNO, USUARIO_PROFISSIONAL, NOME_JOGO, ID_FASE, ID_NIVEL, 
         PONTUACAO, PORCENTAGEM_COMPLETADA, TEMPO_GASTO, ACERTOS, ERROS, 
         TENTATIVAS, DATA_REGISTRO]
        """
        (
            self.ID,
            self.ID_ALUNO,
            self.USUARIO_PROFISSIONAL,
            self.NOME_JOGO,
            self.ID_FASE,
            self.ID_NIVEL,
            self.PONTUACAO,
            self.PORCENTAGEM_COMPLETADA,
            self.TEMPO_GASTO,
            self.ACERTOS,
            self.ERROS,
            self.TENTATIVAS,
            self.DATA_REGISTRO
        ) = dados

    def Salvar(self):
        """Insere um novo registro de dados do jogo no banco de dados."""

        # Validações básicas
        if not self.ID_ALUNO or not str(self.ID_ALUNO).strip():
            self.TE.SetErro("Usuário aluno não informado!")
        if not self.USUARIO_PROFISSIONAL or not str(self.USUARIO_PROFISSIONAL).strip():
            self.TE.SetErro("Usuário profissional não informado!")
        if not self.NOME_JOGO or not str(self.NOME_JOGO).strip():
            self.TE.SetErro("Nome do jogo não informado!")
        if not self.ID_FASE:
            self.TE.SetErro("Fase do jogo não definida!")
        if not self.PONTUACAO:
            self.TE.SetErro("Pontuação não definida!")
        if self.TE.TemErros():
            return False

        try:
            colunas = (
                "ID_ALUNO, USUARIO_PROFISSIONAL, NOME_JOGO, ID_FASE, ID_NIVEL, "
                "PONTUACAO, PORCENTAGEM_COMPLETADA, TEMPO_GASTO, ACERTOS, ERROS, TENTATIVAS"
            )
            valores = [
                self.ID_ALUNO,
                self.USUARIO_PROFISSIONAL,
                self.NOME_JOGO,
                self.ID_FASE,
                self.ID_NIVEL,
                self.PONTUACAO,
                self.PORCENTAGEM_COMPLETADA,
                self.TEMPO_GASTO,
                self.ACERTOS,
                self.ERROS,
                self.TENTATIVAS,
            ]
            Banco.inserir("DADOS_JOGOS", colunas, valores)
            return True
        except Exception as e:
            self.TE.SetErro(f"Erro ao salvar dados do jogo: {e}")
            return False

    def Pesquisar(self, rotulo, condicao):
        """Pesquisa dados do jogo conforme condição."""
        try:
            return Banco.consultar(rotulo, 'DADOS_JOGOS', condicao)
        except Exception as e:
            self.TE.SetErro(f"Erro ao pesquisar dados do jogo: {e}")
            return False

    def Deletar(self, id):
        """Deleta um registro específico pelo ID."""
        try:
            Banco.excluir('DADOS_JOGOS', f'ID = {id}')
            return True
        except Exception as e:
            self.TE.SetErro(f"Erro ao deletar dado do jogo: {e}")
            return False

    def getDadoJogo(self, condicao):
        """Retorna o primeiro registro que atende à condição."""
        resultado = Banco.consultar('*', "DADOS_JOGOS", condicao)
        if not resultado or resultado is False:
            return False
        try:
            return resultado[0]
        except Exception as e:
            self.TE.SetErro(f"Erro ao extrair dados do jogo: {e}")
            return False

    def ListarDadosJogos(self, condicao):
        """Retorna uma lista de dicionários com todos os dados dos jogos que atendem à condição."""
        resultado = Banco.consultar('*', "DADOS_JOGOS", condicao)
        if not resultado or resultado is False:
            return False
        try:
            dados = []
            for linha in resultado:
                dados.append({
                    "ID": linha[0],
                    "ID_ALUNO": linha[1],
                    "USUARIO_PROFISSIONAL": linha[2],
                    "NOME_JOGO": linha[3],
                    "ID_FASE": linha[4],
                    "ID_NIVEL": linha[5],
                    "PONTUACAO": linha[6],
                    "PORCENTAGEM_COMPLETADA": linha[7],
                    "TEMPO_GASTO": linha[8],
                    "ACERTOS": linha[9],
                    "ERROS": linha[10],
                    "TENTATIVAS": linha[11],
                    "DATA_REGISTRO": linha[12]
                })
            return dados
        except Exception as e:
            self.TE.SetErro(f"Erro ao listar dados do jogo: {e}")
            return False
