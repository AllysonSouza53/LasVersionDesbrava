from Models.Aluno import Aluno
from Helpers.TratamentoErros import Erros
from kivymd.app import MDApp

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
    app = None

    def __init__(self):
        self.Erros = Erros()
        self.Aluno = Aluno()
        self.app = MDApp.get_running_app()

    def setCadastro(self,app):
        if 'RAAlunosTextField' in app.ids:
            self.RE = app.ids.RAAlunosTextField.text 
        else:
            self.RE = app.RA
            
        self.Nome = app.ids.NomeAlunosTextField.text
        self.Usuario = app.ids.UsuarioAlunosTextField.text
        listadata = app.ids.DataNascimentoAlunosTextField.text.split('/')
        self.DataNascimento = f'{listadata[2]}-{listadata[1]}-{listadata[0]}'
        self.Genero = app.ids.GeneroAlunosTextField.text
        self.Turma = app.ids.TurmaAlunosTextField.text
        self.ProfissionalResponsavel = app.ControleProfissional.CPF
        self.UF = app.ids.UFAlunosTextField.text
        self.Cidade = app.ids.CidadeAlunosTextField.text
        self.Escola = app.ids.EscolaAlunosTextField.text
        self.Diagnostico = app.ids.DiagnosticoAlunosTextField.text
        self.Observacao = app.ids.ObservacaoAlunosTextField.text
        self.NivelLeitura = app.ids.NivelLeituraAlunosTextField.text
        self.NivelEscrita = app.ids.NivelEscritaAlunosTextField.text

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

    def setAluno(self, RE):
        aluno = self.Aluno.getAluno(RE)

        if not aluno:
            self.Erros.SetErro('Aluno não encontrado')
            if self.Erros.TemErros():
                return False
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
            if not self.Aluno.getAluno(self.RE):
                self.Aluno.setAluno(self.getAluno())
                print('Cadastro')
                self.Aluno.Cadastrar()
                return None
            else:
                self.Aluno.setAluno(self.getAluno())
                self.Aluno.Atualizar()
                print('Atualiza')
                return None
        except Exception as e:
            self.Erros.SetErro(f'Não foi possivel salvar aluno. Erro{e}')
            print(f'Erro Controller.{e}')
            return self.Erros.GetErros()
        
    def ExcluirAluno(self):
        try:
            if self.Aluno.Deletar():
                return True
            else:
                return False
        except Exception as e:
            self.Erros.SetErro(f'Não foi possivel excluir aluno. Erro:{e}')
            return False
        