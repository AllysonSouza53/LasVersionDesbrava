from kivy.app import App
from kivy.lang import Builder
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from Controllers.ProfissionaisController import ProfissionaisControler
from Controllers.ProfissionaisLoginController import LoginController
from Helpers.Requerimentos import Escolas,Perfis,Posts,Cidades
from Banco import Banco
from kivy.core.window import Window

#-------------------------------------------------------------------
class TelaEscolha(MDScreen):
    def EscolhaProfissionalButton_Click(self):
        if self.manager:
            self.manager.current = "LoginProfissional"

    def irLoginAluno(self):
        if self.manager:
            self.manager.current = "LoginAluno"

#--------------------------------------------------------------------
class TelaLoginProfissionais(MDScreen):
    def VoltarEscolhaButton_Click(self):
        if self.manager:
            self.manager.current = "Escolha"

    def ParaCadastroProfissionaisButton_Click(self):
        if self.manager:
            self.manager.current = "CadastroProfissional1"

    def EntrarButton_Click(self):
        Sessao = LoginController()
        Sessao.setLogin(self.manager)
        if self.manager:
            if Sessao.Sessao():
                self.manager.current = "PerfilProfissional"

#--------------------------------------------------------------------
class TelaCadastroProfissional1(MDScreen):
    def VoltarEscolhaButton_Click(self):
        if self.manager:
            self.manager.current = "Escolha"

    def CPFCadastroTextField_Active(self, instancia):
        puro = "".join(ch for ch in instancia.text if ch.isdigit())
        puro = puro[:11]

        novo = ""
        for i, d in enumerate(puro):
            novo += d
            if i == 2 or i == 5:
                if len(puro) > i + 1:
                    novo += '.'
            if i == 8:
                if len(puro) > i + 1:
                    novo += '-'
        if instancia.text != novo:
            instancia.text = novo
            Clock.schedule_once(lambda dt: instancia.do_cursor_movement('cursor_end'))


    def ProsissaoCadastroTextField_Focus(self,instancia,focus):
        if focus:
            menu_items = self.ProsissaoCadastroTextField_AddItens(Banco.consultar('NOME', 'PROFISSOES', '1'))
            MDDropdownMenu(caller=instancia, items=menu_items).open()
        else:
            pass

    def ProsissaoCadastroButton_Click(self,instancia):
        try:
            menu_items = self.ProsissaoCadastroTextField_AddItens(Banco.consultar('NOME', 'PROFISSOES', '1'))
            MDDropdownMenu(caller=instancia, items=menu_items).open()
        except:
            pass

    def ProsissaoCadastroTextField_AddItens(self, itens):
        menu_items = [
            {
                "text": f"{item[0].translate(str.maketrans("", "", "(),'"))}",
                "on_release": lambda
                    x=f"{item[0].translate(str.maketrans("", "", "(),'"))}": self.ProsissaoCadastroTextField_ItensClick(x),
            } for item in itens
        ]
        return menu_items

    def ProsissaoCadastroTextField_ItensClick(self, text_item):
        self.ids.ProsissaoCadastroTextField.text = text_item

    def ParaLoginProfissionalButton_Click(self):
        if self.manager:
            self.manager.current = "LoginProfissional"

    def ParaCadastroProfissionais2Button_Click(self):
        if self.manager:
            self.manager.current = "CadastroProfissional2"

#-------------------------------------------------------------------------------------------------
class TelaCadastroProfissional2(MDScreen):
    def VoltarEscolhaButton_Click(self):
        if self.manager:
            self.manager.current = "CadastroProfissional1"

    def UFCadastroProfissionaisTextField_Focus(self,instancia,focus):
            if focus:
                self.itens = [
                    'AC',
                    'AL',
                    'AP',
                    'AM',
                    'BA',
                    'CE',
                    'DF',
                    'ES',
                    'GO',
                    'MA',
                    'MS',
                    'MT',
                    'MG',
                    'PA',
                    'PB',
                    'PR',
                    'PE',
                    'PI',
                    'RJ',
                    'RN',
                    'RS',
                    'RO',
                    'RR',
                    'SC',
                    'SP',
                    'SE',
                    'TO',
                ]
                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.UFCadastroProfissionais_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def UFCadastroProfissionaisBotao_Click(self, instancia):
        try:
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.UFCadastroProfissionais_ItensClick(x)
                } for index in self.itens
            ]

            MDDropdownMenu(caller=instancia, items=menu_items).open()
        except Exception as e:
            print(e)

    def UFCadastroProfissionais_ItensClick(self, text_item):
        self.ids.UFCadastroProfissionaisTextField.text = text_item

    def CidadeCadastroProfissionaisTextFild_Focus(self, instancia, focus):
        if focus:
            Cidade = Cidades()
            itens = Cidade.get_cidades_por_uf(self.ids.UFCadastroProfissionaisTextField.text)
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.CidadeCadastroProfissional_ItensClick(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=instancia, items=menu_items).open()
        else:
            print('erro')

    def CidadeCadastroProfissionalBotao_Click(self, instancia):
        try:
            Cidade = Cidades()
            itens = Cidade.get_cidades_por_uf(self.ids.UFCadastroProfissionaisTextField.text)
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.CidadeCadastroProfissional_ItensClick(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=instancia, items=menu_items).open()
        except Exception as e:
            print(e)

    def CidadeCadastroProfissional_ItensClick(self, text_item):
        self.ids.CidadeCadastroProfissionalTextField.text = text_item

    def EscolaCadastroProfissionalTextField_Focus(self, instancia, focus):
        if focus:
            Escola = Escolas()
            dados = Escola.Get(self.ids.UFCadastroProfissionaisTextField.text, self.ids.CidadeCadastroProfissionalTextField.text)
            itens = [item["escola"] for item in dados if "escola" in item]
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.EscolaCadastroProfissional_ItensClick(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=instancia, items=menu_items).open()
        else:
            print('erro')

    def EscolaCadastroProfissionalButton_Click(self, instancia):
        try:
            Escola = Escolas()
            dados = Escola.Get(self.ids.UFCadastroProfissionaisTextField.text, self.ids.CidadeCadastroProfissionalTextField.text)
            itens = [item["escola"] for item in dados if "escola" in item]
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.EscolaCadastroProfissional_ItensClick(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=instancia, items=menu_items).open()
        except Exception as e:
            print(e)

    def EscolaCadastroProfissional_ItensClick(self, text_item):
        self.ids.EscolaCadastroProfissionalTextField.text = text_item

    def ParaLoginProfissionalButton_Click(self):
        if self.manager:
            self.manager.current = "LoginProfissional"

    def CadastrarProfissionalButton_Click(self):
        if self.manager:
            controle = ProfissionaisControler()
            controle.setCadastro(self.manager)
            if controle.Cadastar():
                self.manager.current = "LoginProfissional"
        else:
            print("root ainda não existe")

#-------------------------------------------------------------------------------------------------------
class TelaPerfilProfissional(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_resize=self.Atualizar)

    def on_enter(self, *args):
        self.Gerar()

    def Gerar(self):
        self.Sessao = LoginController()
        self.Sessao.setLogin(self.manager)
        self.Profissional = ProfissionaisControler()
        self.Profissional.setUsuario(f'USUARIO = "{self.Sessao.usuario}"')
        Orientacao = "horizontal" if Window.width > 700 else "vertical"
        Padding = 70 if Window.width > 700 else 10
        Altura = 'self.minimum_height' if Window.width < 700 else 0
        Tamanho_y = None if Window.width < 700 else 1
        TelaPerfil = (f'''
MDFloatLayout:
    canvas.before:
        # Desenha o fundo
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            source: 'Imagens/Fundo.png'
            size: self.size
            pos: self.pos
    BoxLayout:
        orientation: "vertical"
        cols:2
        BoxLayout:
            size_hint: 1, None
            orientation: "horizontal"
            BoxLayout:
                canvas:
                    # Desenha o logo
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        source: 'Imagens/Logo.png'
                        size: app.resp.Size_x_Image_Perfil, app.resp.Size_y_Image_Perfil
                        pos: self.center_x - self.width * 0.48, self.center_y - self.height * app.resp.Pos_y_Image_Perfil
            BoxLayout:
                orientation: "horizontal"
                MDTextButton:
                    text: "Perfil"
                    theme_text_color: "Custom"
                    text_color: 1, 1, 1, 1
                    on_release: app.label_clicado()
                    font_size: "18sp"
                    bold: True
                    pos_hint: {{"center_x": 0.5, "center_y": 0.5}}
                
        MDBoxLayout:
            orientation: "{Orientacao}"
            MDBoxLayout:
                spacing: 0
                padding: {Padding}
                orientation:"vertical"
                size_hint_y: {Tamanho_y}          
                height: {Altura}             
                
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0.5  # cor do fundo (RGBA)
                    RoundedRectangle:
                        pos: self.x + self.padding[0] - 10, self.y + self.padding[1] - 10
                        size: self.width + 20 - (self.padding[0] + self.padding[2]), self.height + 20- (self.padding[1] + self.padding[3])
                
                MDBoxLayout:
                    orientation: "vertical"
                    Image:
                        id:PerfilImagem
                        source: 'Imagens/FotoPerfil.png'
                        size_hint: None, None
                        size: app.resp.Size_x_Image_Perfil, app.resp.Size_y_Image_Perfil
                        pos_hint: {{"center_x": 0.5}}
                      
                    MDLabel:
                        text: "@{self.Profissional.Usuario}"
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1      # permite definir altura manualmente
                        height: self.texture_size[1]   # ajusta altura conforme o texto
                        text_size: self.width, None    # define limite de quebra de linha
                        font_size: app.resp.FontSize_Title
                    
                    MDLabel:
                        text: "Nome:{self.Profissional.Nome}"
                        halign: "left"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1        # permite definir altura manualmente
                        height: self.texture_size[1]   # ajusta altura conforme o texto
                        text_size: self.width, None    # define limite de quebra de linha
                        font_size: app.resp.FontSize_Title
                    
                    MDLabel:
                        text: "CPF:{self.Profissional.CPF}"
                        halign: "left"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1        # permite definir altura manualmente
                        height: self.texture_size[1]   # ajusta altura conforme o texto
                        text_size: self.width, None    # define limite de quebra de linha
                        font_size: app.resp.FontSize_Title
                    
                    MDLabel:
                        text: "Profissão:{self.Profissional.Profissao}"
                        halign: "left"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1          # permite definir altura manualmente
                        height: self.texture_size[1]   # ajusta altura conforme o texto
                        text_size: self.width, None    # define limite de quebra de linha
                        font_size: app.resp.FontSize_Title
                        
                    MDLabel:
                        text: "Escola:{self.Profissional.Escola}"
                        halign: "left"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1            # permite definir altura manualmente
                        height: self.texture_size[1]   # ajusta altura conforme o texto
                        text_size: self.width, None    # define limite de quebra de linha
                        font_size: app.resp.FontSize_Title
                        
                    MDLabel:
                        text: "Biografia:{self.Profissional.Biografia}"
                        halign: "left"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1           # permite definir altura manualmente
                        height: self.texture_size[1]   # ajusta altura conforme o texto
                        text_size: self.width, None    # define limite de quebra de linha
                        font_size: app.resp.FontSize_Title
                
                BoxLayout:
                    MDRaisedButton:
                        text: 'Alterar Perfil'
                        pos_hint: {{'center_x': 0.5}}
                        md_bg_color: 0.0, 0.4, 0.0, 1
                        font_size: "18sp"
                        bold: True
                        line_color: 1, 1, 1, 1
                        on_release: app.CadatrarProfissionais_Click()
    
            BoxLayout:
                MDLabel:
                    text: "foi?"
                    halign: "center"
                    valign: "center"
                    text_size: self.size
''')

        layout = Builder.load_string(TelaPerfil)
        self.add_widget(layout)

    def Atualizar(self, *args):
        self.Gerar()