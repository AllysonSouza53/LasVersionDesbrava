class ProfissionaisControler:
    def __init__(self, app):
        CPF = app.get_screen("CadastroProfissional1").ids.lbl_CPFCadastroProfissional.text
        Nome= app.get_screen("CadastroProfissional1").ids.lbl_NomeCadastroProfissional.text
        Usuario = app.get_screen("CadastroProfissional1").ids.lbl_UsuarioCadastroProfissional.text
        Profissao = app.get_screen("CadastroProfissional1").ids.List_ProfissoesText.text
        UF = app.get_screen("CadastroProfissional2").ids.List_EscolasText.text
        Cidade = app.get_screen("CadastroProfissional2").ids.List_CidadesText.text
        Escola = app.get_screen("CadastroProfissional2").ids.List_UFText.text
        Senha = app.get_screen("CadastroProfissional2").ids.lbl_SenhaProfissional.text
        ConfirmacaoSenha = app.get_screen("CadastroProfissional2").ids.lbl_ConfirmarSenhaProfissional.text
        print('(:')