from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from Helpers.Responsividade import Responsividade
from Views.Telas import *


class Gerenciador(ScreenManager):
    pass

class MainApp(MDApp):
    resp = None
    def build(self):
        self.resp = Responsividade()
        self.load_kv("Views/DesbravaFront.kv")
        return Gerenciador()

MainApp().run()
