from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from Controllers.ProfissionaisLoginController import LoginController
from Controllers.ProfissionaisController import ProfissionaisControler
from kivymd.uix.menu import MDDropdownMenu
from Banco import Banco
from Helpers.Requerimentos import Escolas,Perfis,Posts
from Helpers import Requerimentos
from kivy.clock import Clock
from Controllers.ProfissionaisController import ProfissionaisControler
import base64


class MyApp(MDApp):
    def build(self):
        return Builder.load_file("Views/Front.kv")
    #quando iniciar
    def on_start(self):
        if self.root:
            print("ScreenManager inicializado com sucesso!")
    #tela escolha
    def irLoginAluno(self):
        if self.root:
            self.root.current = "LoginAluno"

    def irEscolha(self):
        if self.root:
            self.root.current = "Escolha"

    def irLoginProfissional(self):
        if self.root:
            self.root.current = "LoginProfissional"

    #tela LoginProfissional
    def irCadastroProfissional1(self):
        if self.root:
            self.root.current = "CadastroProfissional1"

    def LoginProfissionais_Click(self):
        PC = ProfissionaisControler(self.root)
        Sessao = LoginController(self.root)
        if self.root:
            self.controle = LoginController(self.root)
            if self.controle.Sessao():
                PostView = self.root.get_screen("PerfilProfissional").ids.datagrid
                DadosPerfil = self.root.get_screen("PerfilProfissional").ids
                '''
                    Posts = Posts.GetPorUsuario()
                imagens = [
                    {
                        'imagem': Post[Post][3]
                    }for Post in Posts
                ]
                '''
                FotoPerfil = ClassePerfis.GetPorUsuario(Sessao.usuario)
                print(FotoPerfil)
                self.Profissional = PC.CarregarUsuario(f"USUARIO ='{Sessao.usuario}'")
                if FotoPerfil == None:
                    img_bytes = base64.b64decode(ClassePerfis.GetPorUsuario('padrao')['imagem'])
                    print(img_bytes)
                else:
                    img_bytes = base64.b64decode(FotoPerfil['imagem'])

                with open("Imagens/FotoPerfil.png", "wb") as f:
                    f.write(img_bytes)
                DadosPerfil['lbl_UsuarioPerfil'].text = '@'+self.Profissional[0][2]
                DadosPerfil['lbl_CPFPerfil'].text = f"CPF:{self.Profissional[0][0]}"
                DadosPerfil['lbl_NomePerfil'].text = f"Nome:{self.Profissional[0][1]}"
                DadosPerfil['lbl_ProfissaoPerfil'].text = f"Profissão:{self.Profissional[0][3]}"
                if not DadosPerfil['lbl_BiografiaPerfil'].text:
                    DadosPerfil['lbl_BiografiaPerfil'].text = f"Biografia:Conte mais sobre você"
                else:
                    DadosPerfil['lbl_BiografiaPerfil'].text = f"Biografia:{self.Profissional[0][9]}"
                '''
                for imagem, legenda in dados:
                    # 1ª linha: imagem
                    PostView.add_widget(
                        FitImage(
                            source=imagem,
                            size_hint_y=None,
                            height=100
                        )
                    )

                    # 2ª linha: legenda
                    PostView.add_widget(
                        MDLabel(
                            text=legenda,
                            halign="center",
                            size_hint_y=None,
                            height=40
                        )
                    )
                '''
                self.root.current = "PerfilProfissional"
        else:
            print("root ainda não existe")

    #tela CadastroProfissional1
    def ListaProfissõesText_Click(self, item, ativa):
        if ativa:
            menu_items = self.AddItensProfissoes(Banco.consultar('NOME','PROFISSOES','1'))
            MDDropdownMenu(caller=item, items=menu_items).open()
        else:
            print('erro')


    def ListaProfissõesBotao_Click(self, item):
        try:
            menu_items = self.AddItensProfissoes(Banco.consultar('NOME','PROFISSOES','1'))
            MDDropdownMenu(caller=item, items=menu_items).open()
        except Exception as e:
            print(e)

    def ListaProfissoesItens_Click(self, text_item):
        self.root.get_screen("CadastroProfissional1").ids.List_ProfissoesText.text = text_item

    def AddItensProfissoes(self, itens):
        menu_items = [
            {
                "text": f"{item[0].translate(str.maketrans("", "", "(),'"))}",
                "on_release": lambda x=f"{item[0].translate(str.maketrans("", "", "(),'"))}": self.ListaProfissoesItens_Click(x),
            } for item in itens
        ]
        return menu_items

    def irCadastroProfissional2(self):
        if self.root:
            self.root.current = "CadastroProfissional2"

    #tela CadastroProfissionais2
    def ListaUFText_Click(self,item, ativa):
        if ativa:
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
                "text":f'{index}',
                "on_release": lambda x=f'{index}': self.ListaUFItens_Click(x)
                }for index in self.itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        else:
            print('err')

    def ListaUFBotao_Click(self, item):
        try:
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.ListaUFItens_Click(x)
                } for index in self.itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        except Exception as e:
            print(e)

    def ListaUFItens_Click(self, text_item):
        self.root.get_screen("CadastroProfissional2").ids.List_UFText.text = text_item

    def ListaCidadesText_Click(self,item, ativa):
        if ativa:
            itens = Requerimentos.get_cidades_por_uf(self.root.get_screen("CadastroProfissional2").ids.List_UFText.text)
            menu_items = [
                {
                "text":f'{index}',
                "on_release": lambda x=f'{index}': self.ListaCidadesItens_Click(x)
                }for index in itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        else:
            print('erro')

    def ListaCidadesBotao_Click(self, item):
        try:
            itens = Requerimentos.get_cidades_por_uf(self.root.get_screen("CadastroProfissional2").ids.List_UFText.text)
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.ListaCidadesItens_Click(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        except Exception as e:
            print(e)

    def ListaCidadesItens_Click(self, text_item):
        self.root.get_screen("CadastroProfissional2").ids.List_CidadesText.text = text_item

    def ListaEscolasBotao_Click(self, item):
        try:
            itens = Requerimentos.get_escolas(self.root.get_screen("CadastroProfissional2").ids.List_UFText.text,self.root.get_screen("CadastroProfissional2").ids.List_CidadesText.text,'BaseInterna//microdados_ed_basica_2024.csv')
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.ListaEscolasBotao_Click(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        except Exception as e:
            print(e)


    def ListaEscolasText_Click(self,item, ativa):
        if ativa:
            itens = Requerimentos.get_escolas(self.root.get_screen("CadastroProfissional2").ids.List_UFText.text,self.root.get_screen("CadastroProfissional2").ids.List_CidadesText.text,'BaseInterna//microdados_ed_basica_2024.csv')
            menu_items = [
                {
                "text":f'{index}',
                "on_release": lambda x=f'{index}': self.ListaEscolasBotao_Click(x)
                }for index in itens
            ]

            MDDropdownMenu(caller=item, items=menu_items).open()
        else:
            print('erro')

    def ListaEscolasBotao_Click(self, text_item):
        self.root.get_screen("CadastroProfissional2").ids.List_EscolasText.text = text_item

    def formatar_cpf(self, instance):
        puro = "".join(ch for ch in instance.text if ch.isdigit())
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
        if instance.text != novo:
            instance.text = novo
            Clock.schedule_once(lambda dt: self.mover_cursor(instance))

    def mover_cursor(self, instance):
        instance.do_cursor_movement('cursor_end')

    def CadatrarProfissionais_Click(self):
        if self.root:
            self.controle = ProfissionaisControler(self.root)
            if self.controle.Cadastar():
                self.root.current = "LoginProfissional"
        else:
            print("root ainda não existe")

ClassePerfis = Perfis()
MyApp().run()