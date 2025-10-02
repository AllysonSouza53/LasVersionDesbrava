from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from Views.Telas import TelaEscolha,TelaLoginProfissionais
from Helpers.Responsividade import Responsividade


class Gerenciador(ScreenManager):
    pass

class MainApp(MDApp):
    def build(self):
        self.resp = Responsividade()
        self.load_kv("Views/DesbravaFront.kv")
        return Gerenciador()

MainApp().run()
