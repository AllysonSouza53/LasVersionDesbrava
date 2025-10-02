from kivymd.uix.screen import MDScreen

class TelaEscolha(MDScreen):
    def irLoginProfissional(self):
        if self.manager:
            self.manager.current = "LoginProfissional"

    def irLoginAluno(self):
        if self.manager:
            self.manager.current = "LoginAluno"

class TelaLoginProfissionais(MDScreen):
    pass

class TelaLoginAluno(MDScreen):
    pass