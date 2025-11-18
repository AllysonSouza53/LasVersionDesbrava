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
    Pos_x_CadastroLabel = NumericProperty(0.0)
    Pos_y_CPFCadastroLabel = NumericProperty(0.0)
    Pos_x_List_Botao = NumericProperty(0.0)
    Pos_y_NomeCompletoLabel = NumericProperty(0.0)
    Pos_y_NomeCompletoCadastroLabel = NumericProperty(0.0)
    Pos_y_UsuarioCadastroLabel = NumericProperty(0.0)
    Pos_y_ProsissaoCadastroLabel = NumericProperty(0.0)
    Size_x_FundoCadastroProfissional = NumericProperty(0.0)
    Pos_x_FundoCadastroProfissional = NumericProperty(0.0)
    Pos_y_EscolaCadastroProfissionalLabel = NumericProperty(0.0)
    Pos_y_CidadeCadastroProfissionaisLabel = NumericProperty(0.0)
    Pos_y_UFCadastroProfissionaisLabel = NumericProperty(0.0)
    Pos_y_SenhaCadastroProfissionaisLabel = NumericProperty(0.0)
    Pos_y_ConfirmarSenhaCadastroProfissionaisLabel = NumericProperty(0.0)
    Size_x_Logo_inter = NumericProperty(0.0)
    Size_y_Logo_inter = NumericProperty(0.0)
    Size_x_Image_Perfil = NumericProperty(0.0)
    Size_y_Image_Perfil = NumericProperty(0.0)
    Pos_y_Image_Perfil = NumericProperty(0.0)
    FontSize_PerfilText = NumericProperty(0.0)
    Pos_x_Logo_inter = NumericProperty(0.0)
    Pos_y_Logo_inter = NumericProperty(0.0)
    Pos_y_Menu = NumericProperty(0.0)

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
            self.Pos_x_CadastroLabel = 0.7
            self.Pos_x_List_Botao = 0.75
            self.Size_x_FundoCadastroProfissional = 0.7
            self.Pos_x_FundoCadastroProfissional = 0.35
            self.Size_x_Logo_inter = 95
            self.Size_y_Logo_inter = 95
            self.Size_x_Image_Perfil = dp(90)
            self.Size_y_Image_Perfil = dp(90)
            self.FontSize_PerfilText = dp(12)
            self.Pos_y_Logo_inter = 0.5
            self.Pos_y_Logo_inter = 0.5
            self.Pos_y_Menu = 0.5

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
            self.Pos_x_CadastroLabel = 0.83
            self.Pos_x_List_Botao = 0.65
            self.Size_x_FundoCadastroProfissional = 0.4
            self.Pos_x_FundoCadastroProfissional = 0.20
            self.Size_x_Logo_inter = 80
            self.Size_y_Logo_inter = 80
            self.Size_x_Image_Perfil = dp(110)
            self.Size_y_Image_Perfil = dp(110)
            self.FontSize_PerfilText = dp(20)
            self.Pos_y_Logo_inter = 1
            self.Pos_y_Menu = -0.2

        else:
        # desktop
            self.FontSize = sp(20)
            self.Pos_x_btn1 = 0.44
            self.Pos_x_btn2 = 0.55
            self.Pos_y_btn1 = 0.5
            self.Pos_y_btn2 = 0.5
            self.Transp_Back = 0.5
            self.Size_x_Logo = 150
            self.Size_y_Logo = 150
            self.FontSize_Title = sp(19)
            self.Text_Title = "Bem Vindo(a) Profissional!"
            self.Pos_Title = 0.8
            self.Text_SubLabel = 'Sem cadastro! Se conecte!'
            self.Size_x_TextInput = 0.25
            self.Pos_x_Label_1 = 0.88
            self.Pos_x_Label_2 = 0.88
            self.Size_x_Fundo_1 = 0.30
            self.Pos_x_Fundo_1 = 0.15
            self.Pos_x_CadastroLabel = 0.88
            self.Pos_x_List_Botao = 0.61
            self.Size_x_FundoCadastroProfissional = 0.3
            self.Pos_x_FundoCadastroProfissional = 0.15
            self.Size_x_Logo_inter = 110
            self.Size_x_Image_Perfil = dp(140)
            self.Size_y_Image_Perfil = dp(140)
            self.FontSize_PerfilText = dp(20)
            self.Pos_y_Logo_inter = 1.3
            self.Pos_y_Menu = 1.5


        if height < 500:
            self.Pos_y_Label_1 = 0.7
            self.Pos_y_Label_2 = 0.6
            self.Pos_y_CPFCadastroLabel = 0.8
            self.Pos_y_NomeCompletoCadastroLabel = 0.7
            self.Pos_y_UsuarioCadastroLabel = 0.6
            self.Pos_y_ProsissaoCadastroLabel = 0.5
            self.Pos_y_EscolaCadastroProfissionalLabel = 0.6
            self.Pos_y_CidadeCadastroProfissionaisLabel = 0.7
            self.Pos_y_UFCadastroProfissionaisLabel = 0.8
            self.Pos_y_SenhaCadastroProfissionaisLabel = 0.4
            self.Pos_y_ConfirmarSenhaCadastroProfissionaisLabel = 0.3
            self.Pos_y_Image_Perfil = 0.5
            self.Size_y_Logo_inter = 200
        elif height <900:
            self.Pos_y_Label_1 = 0.635
            self.Pos_y_Label_2 = 0.535
            self.Pos_y_CPFCadastroLabel = 0.7
            self.Pos_y_NomeCompletoCadastroLabel = 0.6
            self.Pos_y_UsuarioCadastroLabel = 0.5
            self.Pos_y_ProsissaoCadastroLabel = 0.4
            self.Pos_y_EscolaCadastroProfissionalLabel = 0.5
            self.Pos_y_CidadeCadastroProfissionaisLabel = 0.6
            self.Pos_y_UFCadastroProfissionaisLabel = 0.7
            self.Pos_y_SenhaCadastroProfissionaisLabel = 0.4
            self.Pos_y_ConfirmarSenhaCadastroProfissionaisLabel = 0.3
            self.Pos_y_Image_Perfil = 0.8
            self.Size_y_Logo_inter = 200
        else:
            self.Pos_y_Label_1 = 0.635
            self.Pos_y_Label_2 = 0.535
            self.Pos_y_CPFCadastroLabel = 0.7
            self.Pos_y_NomeCompletoCadastroLabel = 0.6
            self.Pos_y_UsuarioCadastroLabel = 0.5
            self.Pos_y_ProsissaoCadastroLabel = 0.4
            self.Pos_y_EscolaCadastroProfissionalLabel = 0.5
            self.Pos_y_CidadeCadastroProfissionaisLabel = 0.6
            self.Pos_y_UFCadastroProfissionaisLabel = 0.7
            self.Pos_y_SenhaCadastroProfissionaisLabel = 0.4
            self.Pos_y_ConfirmarSenhaCadastroProfissionaisLabel = 0.3
            self.Pos_y_Image_Perfil = 0.8
            self.Size_y_Logo_inter = 1.3
