from Models.Login import Login

class LoginController:
    def __init__(self,app):
        self.usuario = app.get_screen("LoginProfissional").ids.lbl_ProfissionalUsuario.text
        self.senha = app.get_screen("LoginProfissional").ids.lbl_ProfissionalSenha.text

    def getLogin(self):
        return [self.usuario,
                self.senha]

    def Sessao(self):
        try:
            Usuario = Login(self.getLogin())
            return Usuario.Logar()
        except Exception as e:
            print(e)

    def Desconectar(self):
        return 'Escolh'
