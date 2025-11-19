from Models.ProfissionalLogin import Login

class LoginController:
    usuario = None
    senha = None
    erros = None

    def setNewLogin(self,app):
        self.usuario = app.get_screen("LoginProfissional").ids.lbl_ProfissionalUsuario.text
        self.senha = app.get_screen("LoginProfissional").ids.lbl_ProfissionalSenha.text

    def getLogin(self):
        return [self.usuario,
                self.senha]
    
    def setLogin(self, dados):
        self.usuario = dados[0]
        self.senha = dados[1]

    def Sessao(self):
        try:
            Usuario = Login(self.getLogin())
            if Usuario.Logar():
                return True
            self.erros = Usuario.Erros.GetErros()
            return False
        except Exception as e:
            return e

    def Desconectar(self):
        return
