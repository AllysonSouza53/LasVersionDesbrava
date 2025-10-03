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
    Pos_y_Label_1 = NumericProperty(0.0)
    Pos_y_Label_2 = NumericProperty(0.0)
    Pos_x_Label_1 = NumericProperty(0.0)
    Pos_x_Label_2 = NumericProperty(0.0)
    Text_SubLabel = StringProperty("")
    Size_x_TextInput = NumericProperty(0.0)
    Size_x_Fundo_1 = NumericProperty(0.0)
    Pos_x_Fundo_1 = NumericProperty(0.0)
    Pos_x_CPFCadastroLabel = NumericProperty(0.0)
    Pos_y_CPFCadastroLabel = NumericProperty(0.0)
    Pos_x_List_ProfissoesBotao = NumericProperty(0.0)

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
            self.Text_SubLabel = 'se Conecte!'
            self.Size_x_TextInput = 0.6
            self.Pos_x_Label_1 = 0.7
            self.Pos_x_Label_2 = 0.7
            self.Size_x_Fundo_1 = 0.7
            self.Pos_x_Fundo_1 = 0.35
            self.Pos_x_CPFCadastroLabel = 0.7
            self.Pos_x_List_ProfissoesBotao = 0.75

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
            self.Text_SubLabel = 'se Conecte!'
            self.Size_x_TextInput = 0.35
            self.Pos_x_Label_1 = 0.83
            self.Pos_x_Label_2 = 0.83
            self.Size_x_Fundo_1 = 0.40
            self.Pos_x_Fundo_1 = 0.20
            self.Pos_x_CPFCadastroLabel = 0.83
            self.Pos_x_List_ProfissoesBotao = 0.65

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
            self.Text_SubLabel = 'Sem cadastro! Se conecte!'
            self.Size_x_TextInput = 0.25
            self.Pos_x_Label_1 = 0.88
            self.Pos_x_Label_2 = 0.88
            self.Size_x_Fundo_1 = 0.30
            self.Pos_x_Fundo_1 = 0.15
            self.Pos_x_CPFCadastroLabel = 0.88
            self.Pos_x_List_ProfissoesBotao = 0.61


        if height < 700:
            self.Pos_y_Label_1 = 0.64
            self.Pos_y_Label_2 = 0.54
            self.Pos_y_CPFCadastroLabel = 0.71
        else:
            self.Pos_y_Label_1 = 0.635
            self.Pos_y_Label_2 = 0.535
            self.Pos_y_CPFCadastroLabel = 0.7
