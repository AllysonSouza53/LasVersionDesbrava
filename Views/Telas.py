from kivymd.uix.screen import MDScreen

class TelaEscolha(MDScreen):
    def EscolhaProfissionalButton_Click(self):
        if self.manager:
            self.manager.current = "LoginProfissional"

    def irLoginAluno(self):
        if self.manager:
            self.manager.current = "LoginAluno"

class TelaLoginProfissionais(MDScreen):
    def VoltarEscolhaButton_Click(self):
        if self.manager:
            self.manager.current = "Escolha"

    def ParaCadastroProfissionaisButton_Click(self):
        if self.manager:
            self.manager.current = "CadastroProfissional"

    def EntrarButton_Click(self):
        pass

class TelaCadastroProfissional(MDScreen):
    def VoltarEscolhaButton_Click(self):
        if self.manager:
            self.manager.current = "Escolha"
