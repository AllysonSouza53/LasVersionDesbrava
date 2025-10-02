from kivy.core.window import Window
from kivy.properties import NumericProperty, StringProperty
from kivy.metrics import sp, dp
from kivy.event import EventDispatcher

class Responsividade(EventDispatcher):
    FontSize = NumericProperty(sp(18))
    Pos_x_btn1 = NumericProperty(0.0)
    Pos_x_btn2 = NumericProperty(0.0)
    Pos_y_btn1 = NumericProperty(0.0)
    Pos_y_btn2 = NumericProperty(0.0)
    Transp_Back = NumericProperty(0.0)
    Size_x_Logo = NumericProperty(0.0)
    Size_y_Logo = NumericProperty(0.0)
    Text_Title = StringProperty("")
    FontSize_Title = NumericProperty(0.0)
    FontSize_Subtitle = NumericProperty(0.0)
    Pos_Title = NumericProperty(0.0)
    Pos_Label = NumericProperty(0.0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Window.bind(on_resize=self.Atualizar)
        self.Atualizar(Window, Window.width, Window.height)

    def Atualizar(self,window, width, height):
        if width < 700:
        # celular
            self.FontSize = sp(12)
            self.Pos_x_btn1 = 0.5
            self.Pos_x_btn2 = 0.5
            self.Pos_y_btn1 = 0.45
            self.Pos_y_btn2 = 0.55
            self.Transp_Back = 0.0
            self.Size_x_Logo = 100
            self.Size_y_Logo = 100
            self.FontSize_Title = sp(16)
            self.Text_Title = "Bem Vindo(a)!"
            self.Pos_Title = 0.83

        elif width < 1200:
        # tablet
            self.FontSize = sp(12)
            self.Pos_x_btn1 = 0.44
            self.Pos_x_btn2 = 0.55
            self.Pos_y_btn1 = 0.5
            self.Pos_y_btn2 = 0.5
            self.Transp_Back = 0.5
            self.Size_x_Logo = 120
            self.Size_y_Logo = 120
            self.FontSize_Title = sp(18)
            self.Text_Title = "Bem Vindo(a)!"
            self.Pos_Title = 0.93

        else:
        # desktop
            self.FontSize = sp(16)
            self.Pos_x_btn1 = 0.44
            self.Pos_x_btn2 = 0.55
            self.Pos_y_btn1 = 0.5
            self.Pos_y_btn2 = 0.5
            self.Transp_Back = 0.5
            self.Size_x_Logo = 150
            self.Size_y_Logo = 150
            self.FontSize_Title = sp(20)
            self.Text_Title = "Bem Vindo(a) Profissional!"
            self.Pos_Title = 0.8

        if height < 700:
            self.Pos_Label = 0.64
        elif height < 1200:
            self.Pos_Label = 0.62
        else:
            self.Pos_Label = 0.5