from Models.DadosJogo import DadosJogo
from Helpers.TratamentoErros import Erros as E

class DadosJogosController:
    ID = None
    ID_ALUNO = None
    USUARIO_PROFISSIONAL = None
    NOME_JOGO = None
    FASE = None
    ID_NIVEL = None
    PONTUACAO = None
    PORCENTAGEM_COMPLETADA = None
    TEMPO_GASTO = None
    ACERTOS = None
    ERROS = None
    TENTATIVAS = None
    DATA_REGISTRO = None

    def __init__(self):
        self.Erros = E()
        self.DadosJogos = DadosJogo()

    # 🔹 Define os dados de um novo jogo
    def setNewDadoJogo(self, dados):
        (
            self.ID_ALUNO,
            self.USUARIO_PROFISSIONAL,
            self.NOME_JOGO,
            self.FASE,
            self.ID_NIVEL,
            self.PONTUACAO,
            self.PORCENTAGEM_COMPLETADA,
            self.TEMPO_GASTO,
            self.ACERTOS,
            self.ERROS,
            self.TENTATIVAS
        ) = dados

    # 🔹 Retorna os dados atuais do jogo em formato de lista
    def getDadoJogo(self):
        return [
            self.ID,
            self.ID_ALUNO,
            self.USUARIO_PROFISSIONAL,
            self.NOME_JOGO,
            self.FASE,
            self.ID_NIVEL,
            self.PONTUACAO,
            self.PORCENTAGEM_COMPLETADA,
            self.TEMPO_GASTO,
            self.ACERTOS,
            self.ERROS,
            self.TENTATIVAS,
            self.DATA_REGISTRO
        ]

    # 🔹 Busca um registro específico no banco de dados
    def setDadoJogo(self, condicao):
        dado = self.DadosJogos.getDadoJogo(condicao)
        if not dado:
            print("⚠️ Nenhum dado encontrado para o jogo.")
            return False

        (
            self.ID,
            self.ID_ALUNO,
            self.USUARIO_PROFISSIONAL,
            self.NOME_JOGO,
            self.FASE,
            self.ID_NIVEL,
            self.PONTUACAO,
            self.PORCENTAGEM_COMPLETADA,
            self.TEMPO_GASTO,
            self.ACERTOS,
            self.ERROS,
            self.TENTATIVAS,
            self.DATA_REGISTRO
        ) = dado

        return True

    # 🔹 Salva um novo registro no banco
    def SalvarDado(self):
        try:
            self.DadosJogos.setDadoJogo(self.getDadoJogo())
            resultado = self.DadosJogos.Salvar()
            return bool(resultado)
        except Exception as e:
            print(f"❌ Erro ao salvar dados do jogo: {e}")
            return False

    # 🔹 Pesquisa registros por aluno
    def PesquisarPorAluno(self, ID_ALUNO):
        resultado = self.DadosJogos.Pesquisar('*', f"ID_ALUNO = '{ID_ALUNO}'")
        if not resultado:
            return False
        return resultado

    # 🔹 Lista todos os dados com base em uma condição
    def setListaDadosJogos(self, condicao):
        lista = self.DadosJogos.ListarDadosJogos(condicao)
        return lista

    # 🔹 Exclui um registro específico
    def ExcluirDadoJogo(self):
        try:
            self.DadosJogos.Deletar(self.ID)
            return True
        except Exception as e:
            print(f"❌ Erro ao excluir dados do jogo: {e}")
            return False