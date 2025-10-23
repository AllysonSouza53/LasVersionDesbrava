from Models.AlunoLogin import Login

class LoginAlunoController:
    usuario = None
    RA = None

    def setLogin(self,app):
        self.usuario = app.ids.UsuarioTextField.text
        self.RA = app.ids.RATextField.text
        print(f'Usuario: {self.usuario} | RA: {self.RA}')

    def getLogin(self):
        return [self.usuario,
                self.RA]

    def Sessao(self):
        try:
            Usuario = Login(self.getLogin())
            return Usuario.Logar()
        except Exception as e:
            return e

    def Desconectar(self):
        return