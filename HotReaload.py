from kivy.lang import Builder
from kivymd.tools.hotreload.app import MDApp

class MainApp(MDApp):
    KV_FILES = ["Views/Front.kv"]
    DEBUG = True
    def build_app(self):
        return Builder.load_file(self.KV_FILES[0])

    def on_start(self):
        if self.root:
            print("ScreenManager inicializado com sucesso!")

    def irLoginAluno(self):
        if self.root:
            self.root.current = "LoginAluno"

    def irEscolha(self):
        if self.root:
            self.root.current = "Escolha"

    def irLoginProfissional(self):
        if self.root:
            self.root.current = "LoginProfissional"

MainApp().run()