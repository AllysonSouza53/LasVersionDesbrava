from App.Models.Aluno import Aluno
from App.Helpers.TratamentoErros import Erros


class AlunoController:
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

    def __init__(self):
        self.Erros = Erros()
        self.Aluno = Aluno()

    def setCadastro(self):
        pass

    def getAluno(self):
        return [
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
            self.NivelEscrita
        ]

    def setAluno(self, aluno):
        aluno = self.Aluno.getAluno(self.Usuario)

        if not aluno:
            self.Erros.SetErro('Aluno não encontrado')
            if self.Erros.TemErros():
                return self.Erros.GetErros()
            else:
                pass

        (
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
            self.NivelEscrita
        ) = aluno
        return True

    def ListarAlunosPorProfissional(self, profissional):
        dados_brutos = self.Aluno.Pesquisar('*', f"PROFISSIONALRESPONSAVEL = '{profissional}'")
        if not dados_brutos:
            return []
        colunas = [
            "RE", "Nome", "Usuario", "Escola", "DataNascimento", "Genero",
            "Turma", "ProfissionalResponsavel", "UF", "Cidade", "Diagnostico",
            "Observacao", "NivelLeitura", "NivelEscrita"
        ]
        lista_dicionarios = []
        for linha in dados_brutos:
            aluno_dict = {colunas[i]: linha[i] for i in range(len(colunas))}
            lista_dicionarios.append(aluno_dict)
        return lista_dicionarios

    def Salvar(self):
        try:
            if not self.Aluno.getAluno(self.Usuario):
                self.Aluno.Cadastrar()
                return None
            else:
                self.Aluno.Atualizar()
                return None
        except Exception as e:
            self.Erros.SetErro(f'Não foi possivel salvar aluno. Erro{e}')
            return self.Erros.GetErros()