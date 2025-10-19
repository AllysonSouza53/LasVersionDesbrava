from Banco import Banco
from Helpers.TratamentoErros import Erros

class DadosJogo:
    ID = None
    USUARIO_ALUNO = None
    USUARIO_PROFISSIONAL = None
    ID_JOGO = None
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
        [ID, USUARIO_ALUNO, USUARIO_PROFISSIONAL, ID_JOGO, ID_NIVEL, PONTUACAO,
         PORCENTAGEM_COMPLETADA, TEMPO_GASTO, ACERTOS, ERROS, TENTATIVAS, DATA_REGISTRO]
        """
        (
            self.ID,
            self.USUARIO_ALUNO,
            self.USUARIO_PROFISSIONAL,
            self.ID_JOGO,
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
        # Validações básicas
        if not self.USUARIO_ALUNO or not str(self.USUARIO_ALUNO).strip():
            self.TE.SetErro("Usuário aluno não informado!")
        if not self.USUARIO_PROFISSIONAL or not str(self.USUARIO_PROFISSIONAL).strip():
            self.TE.SetErro("Usuário profissional não informado!")
        if not self.ID_JOGO:
            self.TE.SetErro("Jogo não definido!")
        if not self.PONTUACAO:
            self.TE.SetErro("Pontuação não definida!")
        if self.TE.TemErros():
            return False

        try:
            colunas = "USUARIO_ALUNO,USUARIO_PROFISSIONAL,ID_JOGO,ID_NIVEL,PONTUACAO,PORCENTAGEM_COMPLETADA,TEMPO_GASTO,ACERTOS,ERROS,TENTATIVAS"
            valores = [
                self.USUARIO_ALUNO,
                self.USUARIO_PROFISSIONAL,
                self.ID_JOGO,
                self.ID_NIVEL,
                self.PONTUACAO,
                self.PORCENTAGEM_COMPLETADA,
                self.TEMPO_GASTO,
                self.ACERTOS,
                self.ERROS,
                self.TENTATIVAS
            ]
            Banco.inserir("DADOS_JOGOS", colunas, valores)
            return True
        except Exception as e:
            self.TE.SetErro(f"Erro ao salvar dados do jogo: {e}")
            return False

    def Pesquisar(self, rotulo, condicao):
        try:
            return Banco.consultar(rotulo, 'DADOS_JOGOS', condicao)
        except Exception as e:
            self.TE.SetErro(f"Erro ao pesquisar dados do jogo: {e}")
            return False

    def Deletar(self, id):
        try:
            Banco.excluir('DADOS_JOGOS', f'ID = {id}')
            return True
        except Exception as e:
            self.TE.SetErro(f"Erro ao deletar dado do jogo: {e}")
            return False

    def getDadoJogo(self, condicao):
        resultado = Banco.consultar('*', "DADOS_JOGOS", condicao)
        if not resultado or resultado is False:
            return False
        try:
            return resultado[0]  # retorna a primeira linha completa
        except Exception as e:
            self.TE.SetErro(f"Erro ao extrair dados do jogo: {e}")
            return False

    def ListarDadosJogos(self, condicao):
        resultado = Banco.consultar('*', "DADOS_JOGOS", condicao)
        if not resultado or resultado is False:
            return False
        try:
            dados = []
            for linha in resultado:
                dados.append({
                    "ID": linha[0],
                    "USUARIO_ALUNO": linha[1],
                    "USUARIO_PROFISSIONAL": linha[2],
                    "ID_JOGO": linha[3],
                    "ID_NIVEL": linha[4],
                    "PONTUACAO": linha[5],
                    "PORCENTAGEM_COMPLETADA": linha[6],
                    "TEMPO_GASTO": linha[7],
                    "ACERTOS": linha[8],
                    "ERROS": linha[9],
                    "TENTATIVAS": linha[10],
                    "DATA_REGISTRO": linha[11]
                })
            return dados
        except Exception as e:
            self.TE.SetErro(f"Erro ao listar dados do jogo: {e}")
            return False
