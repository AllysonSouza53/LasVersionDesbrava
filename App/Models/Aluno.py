from Banco import Banco
from Helpers.TratamentoErros import Erros

class Aluno:
    RE = None
    Nome = None
    Usuario = None
    Escola = None
    DataNascimento = None
    Genero = None
    Turma = None
    ProfissionalResponsavel = None
    UF = None
    Cidade = None
    Diagnostico = None
    Observacao = None
    NivelLeitura = None
    NivelEscrita = None
    FASETRILHA = None

    def __init__(self):
        self.Erros = Erros()


    def setAluno(self, dados):
        self.RE = dados[0] if dados[0] else None
        self.Nome = dados[1] if dados[1] else None
        self.Usuario = dados[2] if dados[2] else None
        self.Escola = dados[3] if dados[3] else None
        self.DataNascimento = dados[4] if dados[4] else None
        self.Genero = dados[5] if dados[5] else None
        self.Turma = dados[6] if dados[6] else None
        self.ProfissionalResponsavel = dados[7] if dados[7] else None
        self.UF = dados[8] if dados[8] else None
        self.Cidade = dados[9] if dados[9] else None
        self.Diagnostico = dados[10] if dados[10] else None
        self.Observacao = dados[11] if dados[11] else None
        self.NivelLeitura = dados[12] if dados[12] else None
        self.NivelEscrita = dados[13] if dados[13] else None
        self.FASETRILHA = dados[14] if dados[14] else None
        print(self.ProfissionalResponsavel)

    def getAluno(self, RE):
        Resultado = Banco.consultar('*','ALUNOS',f"RE = {RE}")
        if not Resultado or Resultado is False:
            self.Erros.SetErro('Aluno não encontrado')
            print(self.Erros.GetErros())
            return False

        try:
            self.RE = Resultado[0][0]
            self.Nome = Resultado[0][1]
            self.Usuario = Resultado[0][2]
            self.Escola = Resultado[0][3]
            self.DataNascimento = Resultado[0][4]
            self.Genero = Resultado[0][5]
            self.Turma = Resultado[0][6]
            self.ProfissionalResponsavel = Resultado[0][7]
            self.UF = Resultado[0][8]
            self.Cidade = Resultado[0][9]
            self.Diagnostico = Resultado[0][10]
            self.Observacao = Resultado[0][11]
            self.NivelLeitura = Resultado[0][12]
            self.NivelEscrita = Resultado[0][13]
            self.FASETRILHA = Resultado[0][14]

            return [
                self.RE, self.Nome, self.Usuario, self.Escola, self.DataNascimento, self.Genero, self.Turma, self.ProfissionalResponsavel,
                self.UF, self.Cidade, self.Diagnostico, self.Observacao, self.NivelLeitura, self.NivelEscrita, self.FASETRILHA
            ]
        except Exception as e:
            self.Erros.SetErro(f'Não foi possivel achar realizar essa operação. Erro:{e}')
            return False

    def Cadastrar(self):
        self.Erros.LimpeErros()
        if not self.RE:
            self.Erros.SetErro('O resgistro não deve ser vazio')

        if not self.Nome:
            self.Erros.SetErro('O nome não deve ser vazio')

        if not self.Usuario:
            self.Erros.SetErro('O usuario não deve ser vazio')

        if not self.Escola:
            self.Erros.SetErro('A escola não pode ser vazia')

        if not self.DataNascimento:
            self.Erros.SetErro('A data de nascimento não pode ser vazia')

        if not self.Genero:
            self.Erros.SetErro('O gênero não pode ser vazio')

        if not self.Turma:
            self.Erros.SetErro('A turma não pode ser vazia')

        if not self.ProfissionalResponsavel:
            self.Erros.SetErro('O profissional responsável não pode ser vazio')

        if not self.UF:
            self.Erros.SetErro('A UF não pode ser vazia')
        elif len(self.UF) != 2:
            self.Erros.SetErro('UF inválida, deve conter 2 caracteres')

        if not self.Cidade:
            self.Erros.SetErro('A cidade não pode ser vazia')

        # Campos opcionais, mas pode-se checar consistência
        if not self.Diagnostico:
            self.Diagnostico = ''
        if not self.Observacao:
            self.Observacao = ''
        if not self.NivelLeitura:
            self.NivelLeitura = 0
        if not self.NivelEscrita:
            self.NivelEscrita = 0

        # Se houver erros acumulados, não tenta salvar
        if self.Erros.TemErros():
            print("Erros encontrados:", self.Erros.GetErros())
            return False

        try:
            colunas = "RE,NOME,USUARIO,ESCOLA,DATANASCIMENTO,GENERO,TURMA,PROFISSIONALRESPONSAVEL,UF,CIDADE,DIAGNOSTICO,OBSERVACOES,NIVELDELEITURA,NIVELDEESCRITA,FASETRILHA"
            valores = [
                self.RE,
                self.Nome,
                self.Usuario,
                self.Escola,
                self.DataNascimento,
                self.Genero,
                self.Turma,
                self.ProfissionalResponsavel,
                self.UF,
                self.Cidade,
                self.Diagnostico,
                self.Observacao,
                self.NivelLeitura,
                self.NivelEscrita,
                self.FASETRILHA
            ]
            Banco.inserir("ALUNOS", colunas, valores)
            return True
        except Exception as e:
            self.Erros.SetErro(f'Não foi possível salvar o aluno. Erro: {e}')
            print(self.Erros.GetErros())
            return False

    def Atualizar(self):
        try:
            valores = [
                f"NOME = '{self.Nome}'",
                f"USUARIO = '{self.Usuario}'",
                f"ESCOLA = '{self.Escola}'",
                f"DATANASCIMENTO = '{self.DataNascimento}'",
                f"GENERO = '{self.Genero}'",
                f"TURMA = '{self.Turma}'",
                f"PROFISSIONALRESPONSAVEL = '{self.ProfissionalResponsavel}'",
                f"UF = '{self.UF}'",
                f"CIDADE = '{self.Cidade}'",
                f"DIAGNOSTICO = '{self.Diagnostico}'" if self.Diagnostico else "DIAGNOSTICO = NULL",
                f"OBSERVACOES = '{self.Observacao}'" if self.Observacao else "OBSERVACOES = NULL",
                f"NIVELDELEITURA = {self.NivelLeitura}" if self.NivelLeitura else "NIVELDELEITURA = NULL",
                f"NIVELDEESCRITA = {self.NivelEscrita}" if self.NivelEscrita else "NIVELDEESCRITA = NULL",
                f"FASETRILHA = {self.FASETRILHA}" if self.FASETRILHA else "FASETRILHA = NULL"
            ]
            Banco.editar('ALUNOS', valores, f"RE = {self.RE}")
            return True
        except Exception as e:
            print(f'Erro ao atualizar aluno: {e}')
            self.Erros.SetErro(f'Não foi possivel atualizar a aluno. Erro: {e}')
            return False

    def Pesquisar(self, rotulo, condicao):
        try:
            return Banco.consultar(f'{rotulo}', 'ALUNOS', f'{condicao}')
        except Exception as e:
            self.Erros.SetErro(f'Não foi possivel encontar. Erro:{e}')
            return False

    def Deletar(self):
        try:
            Banco.excluir('ALUNOS', f"RE = '{self.RE}'")
            return True
        except Exception as e:
            self.Erros.SetErro(f'Não foi possivel encontar. Erro:{e}')
            return False
