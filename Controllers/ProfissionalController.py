from Models.Profissional import Profissional
from Helpers.TratamentoErros import Erros as E

class ProfissionalControler:
    Profissional = None
    CPF = None
    Nome = None
    Usuario = None
    Profissao = None
    DataNascimento = None
    UF = None
    Cidade = None
    Escola = None
    Senha = None
    ConfirmacaoSenha = None
    Biografia = None
    NumeroCasa = None
    FotoPerfil = None

    def __init__(self):
        self.Erros = E()

    def setCadastro(self, app):
        self.CPF = app.get_screen("CadastroProfissional1").ids.CPFCadastroTextField.text.replace('.', '').replace('-', '')
        self.Nome = app.get_screen("CadastroProfissional1").ids.NomeCompletoCadastroTextFild.text
        self.Usuario = app.get_screen("CadastroProfissional1").ids.UsuarioCadastroTextField.text
        self.Profissao = app.get_screen("CadastroProfissional1").ids.ProsissaoCadastroTextField.text
        self.DataNascimento = None
        self.UF = app.get_screen("CadastroProfissional2").ids.UFCadastroProfissionaisTextField.text
        self.Cidade = app.get_screen("CadastroProfissional2").ids.CidadeCadastroProfissionalTextField.text
        self.Escola = app.get_screen("CadastroProfissional2").ids.EscolaCadastroProfissionalTextField.text
        self.Senha = app.get_screen("CadastroProfissional2").ids.SenhaCadastroProfissionaisTextField.text
        self.ConfirmacaoSenha = app.get_screen("CadastroProfissional2").ids.ConfirmarSenhaCadastroProfissionaisTextFild.text
        self.Biografia = 'Fale um pouco sobre você'
        self.NumeroCasa = ''
        self.FotoPerfil = ''

    def getUsuario(self):
        return [
            self.CPF,
            self.Nome,
            self.Usuario,
            self.Profissao,
            self.DataNascimento,
            self.UF,
            self.Cidade,
            self.Escola,
            self.Senha,
            self.Biografia,
            self.FotoPerfil
        ]

    def setUsuario(self, condicao):
        self.Profissional = Profissional()
        usuario = self.Profissional.getUsuario(condicao)

        if not usuario:
            print("⚠️ Nenhum usuário encontrado.")
            return False

        (
            self.CPF,
            self.Nome,
            self.Usuario,
            self.Profissao,
            self.DataNascimento,
            self.UF,
            self.Cidade,
            self.Escola,
            self.Senha,
            self.Biografia,
            self.FotoPerfil
        ) = usuario
        return True

    def Cadastar(self):
        try:
            self.Profissional = Profissional()
            self.Profissional.setProfissional(self.getUsuario())
            resultado = self.Profissional.Salvar()
            if resultado:
                return True
            return False
        except Exception as e:
            return e














