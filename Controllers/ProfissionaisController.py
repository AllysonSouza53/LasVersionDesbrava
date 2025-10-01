from Models.Profissionais import Profissionais
from Helpers.TratamentoErros import Erros as E

class ProfissionaisControler:
    def __init__(self, app):
        self.Profissionais = None
        self.CPF = app.get_screen("CadastroProfissional1").ids.lbl_CPFCadastroProfissional.text.replace('.', '').replace('-', '')
        self.Nome= app.get_screen("CadastroProfissional1").ids.lbl_NomeCadastroProfissional.text
        self.Usuario = app.get_screen("CadastroProfissional1").ids.lbl_UsuarioCadastroProfissional.text
        self.Profissao = app.get_screen("CadastroProfissional1").ids.List_ProfissoesText.text
        self.DataNascimento = None
        self.UF = app.get_screen("CadastroProfissional2").ids.List_UFText.text
        self.Cidade = app.get_screen("CadastroProfissional2").ids.List_CidadesText.text
        self.Escola = app.get_screen("CadastroProfissional2").ids.List_EscolasText.text
        self.Senha = app.get_screen("CadastroProfissional2").ids.lbl_SenhaProfissional.text
        self.ConfirmacaoSenha = app.get_screen("CadastroProfissional2").ids.lbl_ConfirmarSenhaProfissional.text
        self.Biografia = ''
        self.NumeroCasa  = ''
        self.Rua = ''
        self.Bairro = ''
        self.FotoPerfil = ''
        self.Erros = E()

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
            self.Rua,
            self.Bairro,
            self.FotoPerfil
        ]
    def CarregarUsuario(self, condicao):
        self.Profissionais = Profissionais(self.getUsuario())
        return self.Profissionais.Pesquisar("*",condicao)

    def Cadastar(self):
        try:
            self.Profissionais = Profissionais(self.getUsuario())
            resultado = self.Profissionais.Salvar()
            if resultado:
                return True
        except Exception as e:
            return e














