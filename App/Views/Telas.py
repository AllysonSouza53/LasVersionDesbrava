import os
import io
import json
import time
import base64
import random
from functools import partial

from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from kivy.graphics import Color, Line
from kivy.properties import (
    StringProperty, NumericProperty, BooleanProperty, ListProperty
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.button import (
    MDFillRoundFlatIconButton, MDFlatButton, MDRoundFlatButton,
    MDIconButton, MDFloatingActionButton
)
from kivymd.uix.dialog import MDDialog
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.filemanager import MDFileManager

from Controllers.AlunosController import AlunoController
from Controllers.AlunoControllerLogin import LoginAlunoController
from Controllers.ComentarioController import ComentarioController
from Controllers.DadosJogosController import DadosJogosController
from Controllers.FavoritosController import FavoritosController
from Controllers.PostController import PostController
from Controllers.ProfissionalController import ProfissionalControler
from Controllers.ProfissionaisLoginController import LoginController
from Controllers.AlbumController import AlbumController

from Helpers.Requerimentos import Escolas, Perfis, Posts, Cidades
from Banco import Banco

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
            self.manager.current = "CadastroProfissional1"

    def EntrarButton_Click(self):
        Sessao = LoginController()
        Sessao.setLogin(self.manager)
        if self.manager:
            if Sessao.Sessao():
                self.manager.current = "CarregamentoInicial"

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
            controle = ProfissionalControler()
            controle.setCadastro(self.manager)
            if controle.Cadastar():
                self.manager.current = "LoginProfissional"
        else:
            print("root ainda não existe")

class TelaCarregamentoInicial(MDScreen):
    Profissional = None
    def on_enter(self, *args):
        self.Sessao = LoginController()
        self.Sessao.setLogin(self.manager)
        self.Profissional = ProfissionalControler()
        self.Profissional.setUsuario(f'USUARIO = "{self.Sessao.usuario}"')
        if self.manager:
            self.manager.current = "PerfilProfissional"

class TelaPerfilProfissional(MDScreen):
    Profissional = None
    Post = None
    FeedPerfil = None
    resposta = None
    imagens = None
    Favoritos = None
    Post = None
    resposta = None
    ControlePerfil = None
    Comentario = None
    dialog = None
    instanciacomentario = None

    def on_pre_enter(self, *args):
        self.Post = PostController()
        self.Favoritos = FavoritosController()
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        self.ControlePerfil = tela_carregamento.Profissional or None
        self.FeedPerfil = self.ids.feed_grid
        usuario = self.ControlePerfil.Usuario if self.ControlePerfil else None
        if not usuario:
            return
        self.Comentario = ComentarioController()
        self.resposta = self.Post.PesquisarPorUsuario(usuario)
        self.resposta = self.CarregarImagensPosts(self.resposta)
        self.textura = self.GetFotoPerfil(usuario)
        self.MostrarDados()
        self.ListarPosts()

    def GetFotoPerfil(self, usuario):
        Perfil = Perfis()
        UsuarioPerfil = Perfil.GetPorUsuario(usuario)
        if UsuarioPerfil is None:
            UsuarioPerfilImagem = Perfil.GetPorUsuario('ADMIN')['imagem']
            imagem_bytes = base64.b64decode(UsuarioPerfilImagem)
        else:
            UsuarioPerfilImagem = UsuarioPerfil['imagem']
            imagem_bytes = base64.b64decode(UsuarioPerfilImagem)
        
        imagem_bytes_io = io.BytesIO(imagem_bytes)
        return CoreImage(imagem_bytes_io, ext='png').texture

    def MostrarDados(self):
        if not self.ControlePerfil:
            return
        
        imagem_widget = Image(
            texture=self.textura
        )

        self.ids.imagemperfil.clear_widgets()
        self.ids.imagemperfil.add_widget(imagem_widget)

        self.ids.UsuarioPerfilLabel.text = f'@{self.ControlePerfil.Usuario}'
        self.ids.NomePerfilLabel.text = f'Nome: {self.ControlePerfil.Nome}'
        self.ids.CPFPerfilLabel.text = f'CPF: {self.ControlePerfil.CPF}'
        self.ids.ProfissaoPerfilLabel.text = f'Profissão: {self.ControlePerfil.Profissao}'
        self.ids.EscolaPerfilLabel.text = f'Escola: {self.ControlePerfil.Escola}'
        self.ids.BiografiaPerfilLabel.text = f'Biografia: {self.ControlePerfil.Biografia}'

    def ListarPosts(self):
        self.FeedPerfil.clear_widgets()

        for post in self.resposta:
            box_post = MDBoxLayout(
                orientation="vertical",
                size_hint_y=None,
                padding=dp(5),
            )

            card = MDCard(
                size_hint_y=None,
                padding=dp(10),
                orientation="vertical",
                spacing=dp(10)
            )

            # Cabeçalho
            box_cabecalho = MDBoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(30),
                spacing=dp(10)
            )

            usuario = MDLabel(
                text=f"@{post.get('usuario', '')}",
                font_size="16sp",
                halign="left",
                theme_text_color="Primary",
                size_hint_x=0.7
            )
            usuario.bind(texture_size=usuario.setter('size'))

            btn_menu = MDIconButton(
                icon="dots-vertical",
                size_hint=(None, None),
                size=(dp(24), dp(24)),
                pos=(dp(0), dp(5))
            )

            # Cria menu
            menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
            menu.items = [
                {
                    "text": "Excluir",
                    "icon": "delete",
                    "on_release": lambda x=post: (menu.dismiss(), self.excluir_post(x))
                }
            ]

            btn_menu.on_release = menu.open

            box_cabecalho.add_widget(usuario)
            box_cabecalho.add_widget(btn_menu)
            card.add_widget(box_cabecalho)

            # Imagem do post
            imagem_obj = post.get('imagem_obj', None)
            if imagem_obj:
                imagem_widget = Image(
                    texture=imagem_obj,
                    size_hint_y=None,
                    height=dp(400),
                    allow_stretch=True,
                    keep_ratio=True
                )
                card.add_widget(imagem_widget)

            # Legenda
            legenda = MDLabel(
                text=post.get('legenda', ''),
                halign="left",
                theme_text_color="Secondary",
                size_hint_y=None
            )
            legenda.bind(texture_size=legenda.setter('size'))
            card.add_widget(legenda)

            # Rodapé
            box_rodape = MDBoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(30),
                spacing=dp(10)
            )

            Comentarios_button = MDIconButton(
                icon="comment-outline",
                size_hint=(None, None),
                size=(dp(24), dp(24))
            )
            Comentarios_button.post_id = post.get("id")
            Comentarios_button.bind(on_release=self.abrir_comentarios)

            box_rodape.add_widget(Comentarios_button)
            card.add_widget(box_rodape)

            card.bind(minimum_height=card.setter('height'))
            box_post.add_widget(card)
            box_post.bind(minimum_height=box_post.setter('height'))
            self.FeedPerfil.add_widget(box_post)

    def excluir_post(self, post):
        print(f"🗑️ Excluindo post de {post.get('usuario')}")

    def abrir_comentarios(self, instance):
        self.instanciacomentario = instance
        self.post_id = getattr(instance, "post_id", None)
        resultado = self.Comentario.setListaComentarios(f'IDPOST = {self.post_id}')
        # BoxLayout que vai conter tudo
        BoxComentarios = MDBoxLayout(
            orientation="vertical",
            padding = dp(10),
            spacing = dp(10),
            size_hint_y = None,
            height = dp(500),  # define altura do box
            md_bg_color = (1, 1, 1, 1)
        )
        if resultado:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(20),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))

            for comentario in resultado:
                Card = MDCard(
                    size_hint_y=None,
                    padding=dp(10),
                    orientation="vertical",
                    spacing=dp(5),
                    md_bg_color=(0.8, 0.8, 0.8, 1)
                )

                BoxCabecalho = MDBoxLayout(
                    orientation="horizontal",
                    padding=dp(0),
                    spacing=dp(20),
                    size_hint_y=None,
                    md_bg_color=(1, 1, 1, 1)
                )

                btn_menu = MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    pos=(dp(0), dp(0))
                )

                btn_menu.theme_icon_color = "Custom"
                btn_menu.text_color  = (0, 0, 0, 0)

                BoxCabecalho.md_bg_color = (0.8, 0.8, 0.8, 1)
                BoxCabecalho.bind(minimum_height=BoxCabecalho.setter('height'))
                BoxCabecalho.add_widget(MDLabel(text=f"@{comentario['Usuario']}"))
                if comentario['Usuario'] == self.ControlePerfil.Usuario:
                    btn_menu.text_color  = (0, 0, 0, 1)
                    menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
                    menu.items = [
                        {
                            "text": "Excluir",
                            "icon": "delete",
                            "on_release": lambda x=comentario: (menu.dismiss(), self.ExcluirComentario(x))
                        }
                    ]
                    btn_menu.on_release = menu.open

                BoxCabecalho.add_widget(btn_menu)
                Card.add_widget(BoxCabecalho)
                TextoComentario = MDLabel(
                    text=comentario['Texto'],
                    size_hint_y = None
                )
                Card.add_widget(TextoComentario)

                Card.bind(minimum_height=Card.setter('height'))
                BoxComentario.add_widget(Card)
        else:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(10),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))
            BoxComentario.add_widget(
                MDLabel(
                    text='Sem Comentários. Seja o Primeiro!',
                    halign="center",
                    valign="center",
                )
            )

        BoxPostarComentario = MDBoxLayout(
            orientation="horizontal",
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(80),  # define altura do box
            md_bg_color=(1, 1, 1, 1),
        )

        self.tf = TextInput(
            size_hint_x=0.8,
            cursor_color=(0, 0, 0, 1),
            foreground_color=(0, 0, 0, 1),
            multiline=True,
        )

        # limite de caracteres
        self.tf.max_chars = 500

        # evento que monitora a digitação
        self.tf.bind(text=self.limitar_texto)

        # Botão circular com seta
        btn_cima = MDFloatingActionButton(
            icon="arrow-up",
            md_bg_color=(1, 1, 1, 1),
            text_color=(0, 0, 0, 1),
        )

        btn_cima.bind(on_release=lambda _: self.on_release_Comentarios_button())
        BoxPostarComentario.add_widget(self.tf)
        BoxPostarComentario.add_widget(btn_cima)

        # ScrollView para permitir rolagem se necessário
        scroll = ScrollView(
            do_scroll_x=False, do_scroll_y=True,
            size_hint=(1, None),
            height=dp(400)
        )

        scroll.add_widget(BoxComentario)
        BoxComentarios.add_widget(scroll)
        BoxComentarios.add_widget(BoxPostarComentario)

        # Cria o Dialog
        self.dialog = MDDialog(
            title="Comentários",
            type="custom",
            content_cls=BoxComentarios,
            size_hint=(0.5, None),
            height=dp(180),  # altura do diálogo
        )

        # Abre o Dialog
        self.dialog.open()

    def limitar_texto(self, instance, value):
        if len(value) > instance.max_chars:
            instance.text = value[:instance.max_chars]

    def AtualizarComentarios(self, instance):
        if self.dialog:
            self.dialog.dismiss()
        self.abrir_comentarios(instance)

    def on_release_Comentarios_button(self):
        try:
            self.Comentario.setNewComentario(self)
            self.Comentario.Comentar()
            self.AtualizarComentarios(self.instanciacomentario)
        except Exception as e:
            print(e)

    # Carrega imagens decodificando Base64 e associando pelo id do post
    def CarregarImagensPosts(self, posts):
        try:
            ListaPostsHelper = Posts()
            posts_no_banco = ListaPostsHelper.GetPorUsuario(self.ControlePerfil.Usuario)  # pega todos os posts do banco

            # Cria um dicionário de imagens pelo id do post
            print(posts_no_banco)
            imagens_dict = {}
            for post_banco in posts_no_banco:
                imagem_b64 = post_banco.get('imagem', None)
                textura = None
                if imagem_b64 and imagem_b64 not in ("NULL", "null", ""):
                    try:
                        data = io.BytesIO(base64.b64decode(imagem_b64))
                        textura = CoreImage(data, ext='png').texture  # ou tente detectar o formato
                    except Exception:
                        try:
                            data = io.BytesIO(base64.b64decode(imagem_b64))
                            textura = CoreImage(data, ext='jpg').texture
                        except Exception as e:
                            print(f"Erro ao carregar imagem: {e}")
                            textura = None

                imagens_dict[post_banco['id']] = textura

            # Atualiza os posts originais com a textura correta
            for post in posts:
                post['imagem_obj'] = imagens_dict.get(post.get('id'), None)
                print(f"Imagem no post {post.get('id', 'SEM ID')}: {bool(post.get('imagem_obj'))}")

            return posts

        except Exception as e:
            print(f"Erro ao carregar imagens dos posts: {e}")
            return posts

    def ExcluirComentario(self, post):
        pass

    # Navegação entre telas
    def AlterarPerfilButton_Click(self):
        if self.manager:
            self.manager.current = "AlterarPerfilProfissional"

    def FavoritosPerfilButton_Click(self):
        if self.manager:
            self.manager.current = "FavoritosPerfilProfissional"

    def PerfilMDTextButton_Click(self):
        pass

    def AlunosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"

    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InformacoesJogosProfissionais"

    def ComunidadeMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "ComunidadeProfissionais"

class TelaAlterarPerfilProfissional(MDScreen):
    ControlePerfil = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Cria o gerenciador de arquivos
        self.abrir_file_manager()

    def abrir_file_manager(self):
        from kivymd.uix.filemanager import MDFileManager
        from kivymd.toast import toast

        self.file_manager = MDFileManager(
            exit_manager=self.fechar_file_manager,
            select_path=self.selecionar_imagem
        )
        # Inicia no diretório padrão (por exemplo, a pasta Imagens)
        import os
        start_dir = os.path.expanduser("~/Pictures")  # ou "~/" para pasta do usuário

    def fechar_file_manager(self, *args):
        try:
            self.file_manager.close()
        except Exception as e:
            print(f"Erro ao fechar o FileManager: {e}")

    def GetFotoPerfil(self, usuario):
        Perfil = Perfis()
        UsuarioPerfil = Perfil.GetPorUsuario(usuario)
        if UsuarioPerfil is None:
            UsuarioPerfilImagem = Perfil.GetPorUsuario('ADMIN')['imagem']
            imagem_bytes = base64.b64decode(UsuarioPerfilImagem)
        else:
            UsuarioPerfilImagem = UsuarioPerfil['imagem']
            imagem_bytes = base64.b64decode(UsuarioPerfilImagem)

        self.imagem_base64 = base64.b64encode(imagem_bytes).decode("utf-8")
        imagem_bytes_io = io.BytesIO(imagem_bytes)
        return CoreImage(imagem_bytes_io, ext='png').texture
    
    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ControlePerfil = tela_carregamento.Profissional
        else:
            self.ControlePerfil = None

        if self.ControlePerfil.DataNascimento is None:
            self.ControlePerfil.DataNascimento = ''

        if self.ControlePerfil.Biografia == 'Fale um pouco sobre você':
            self.ControlePerfil.Biografia = ''

        self.ids.UsuarioAlterarTextField.text = f'@{self.ControlePerfil.Usuario}'
        self.ids.NomeAlterarTextField.text = f'{self.ControlePerfil.Nome}'
        self.ids.ProfissaoAlterarTextField.text = f'{self.ControlePerfil.Profissao}'
        self.ids.DataNascimentoAlterarTextField.text = f'{self.ControlePerfil.DataNascimento}'
        self.ids.EstadoAlterarTextField.text = f'{self.ControlePerfil.UF}'
        self.ids.CidadeAlterarTextField.text = f'{self.ControlePerfil.Cidade}'
        self.ids.EscolaAlterarTextField.text = f'{self.ControlePerfil.Escola}'
        self.ids.BiografiaAlterarTextField.text = f'{self.ControlePerfil.Biografia}'
        self.ids.SenhaAlterarTextField.text = f'{self.ControlePerfil.Senha}'
        self.textura = self.GetFotoPerfil(self.ControlePerfil.Usuario)
        imagem_widget = Image(
            texture=self.textura
        )
        self.ids.imagemperfil.clear_widgets()
        self.ids.imagemperfil.add_widget(imagem_widget)

    def on_enter(self, *args):
        pass

    def VoltarEscolhaButton_Click(self):
        if self.manager:
            self.manager.current = "PerfilProfissional"

    def UFAlterarProfissionaisTextField_Focus(self,instancia,focus):
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
                        "on_release": lambda x=f'{index}': self.UFAlterarProfissionais_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def UFAlterarProfissionais_ItensClick(self, text_item):
        self.ids.UFCadastroProfissionaisTextField.text = text_item

    def CidadeAlterarProfissionaisTextFild_Focus(self, instancia, focus):
        if focus:
            Cidade = Cidades()
            itens = Cidade.get_cidades_por_uf(self.ids.EstadoAlterarTextField.text)
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.CidadeAlterarProfissional_ItensClick(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=instancia, items=menu_items).open()
        else:
            print('erro')


    def CidadeAlterarProfissional_ItensClick(self, text_item):
        self.ids.CidadeAlterarTextField.text = text_item

    def EscolaAlterarProfissionalTextField_Focus(self, instancia, focus):
        if focus:
            Escola = Escolas()
            dados = Escola.Get(self.ids.EstadoAlterarTextField.text, self.ids.CidadeAlterarTextField.text)
            itens = [item["escola"] for item in dados if "escola" in item]
            menu_items = [
                {
                    "text": f'{index}',
                    "on_release": lambda x=f'{index}': self.EscolaAlterarProfissional_ItensClick(x)
                } for index in itens
            ]

            MDDropdownMenu(caller=instancia, items=menu_items).open()
        else:
            print('erro')

    def EscolaAlterarProfissional_ItensClick(self, text_item):
        self.ids.EscolaCadastroProfissionalTextField.text = text_item

    def ProfissaoAlterarTextField_Focus(self,instancia,focus):
        if focus:
            menu_items = self.ProfissaoAlterarTextField_AddItens(Banco.consultar('NOME', 'PROFISSOES', '1'))
            MDDropdownMenu(caller=instancia, items=menu_items).open()
        else:
            pass

    def ProfissaoAlterarTextField_AddItens(self, itens):
        menu_items = [
            {
                "text": f"{item[0].translate(str.maketrans("", "", "(),'"))}",
                "on_release": lambda
                    x=f"{item[0].translate(str.maketrans("", "", "(),'"))}": self.ProsissaoAlterarTextField_ItensClick(x),
            } for item in itens
        ]
        return menu_items

    def ProsissaoAlterarTextField_ItensClick(self, text_item):
        self.ids.ProfissaoAlterarTextField.text = text_item

    def TrocarImagem(self):
        initial_path = "/" if Window.system_size[0] > 0 else "."
        self.file_manager.show(initial_path)

    def selecionar_imagem(self, path):
        self.fechar_file_manager()
        with open(path, "rb") as f:
            imagem_bytes = f.read()
        self.imagem_base64 = base64.b64encode(imagem_bytes).decode("utf-8")
        from kivy.core.image import Image as CoreImage
        data = io.BytesIO(base64.b64decode(self.imagem_base64))
        textura = CoreImage(data, ext='png').texture

        self.textura= textura

        imagem_widget = Image(
            texture=self.textura
        )
        self.ids.imagemperfil.clear_widgets()
        self.ids.imagemperfil.add_widget(imagem_widget)

        MDDialog(title="Imagem selecionada", text=f"Caminho: {path}").open()
        from kivy.cache import Cache

        Cache.remove('kv.image', 'Imagens/FotoPerfil.png')

    def AlterarPerfilButton_Click(self):
        self.ControlePerfil.FotoPerfil = ''
        Perfil = Perfis()
        if not Perfil.GetPorUsuario(self.ControlePerfil.Usuario):
            Perfil.Post(self.ControlePerfil.CPF, self.ControlePerfil.Usuario, self.imagem_base64)
        else:
            Perfil.Update(self.ControlePerfil.CPF, self.ControlePerfil.Usuario, self.imagem_base64)

        MDDialog(
            title="Sucesso",
            text="O perfil foi atualizado!"
        ).open()

        self.ControlePerfil.AlterarProfissional([self.ControlePerfil.CPF,
                                                 self.ids.NomeAlterarTextField.text,
                                                 self.ids.UsuarioAlterarTextField.text.replace('@', ''),
                                                 self.ids.ProfissaoAlterarTextField.text,
                                                 self.ids.DataNascimentoAlterarTextField.text if self.ids.DataNascimentoAlterarTextField.text != '' else None,
                                                 self.ids.EstadoAlterarTextField.text,
                                                 self.ids.CidadeAlterarTextField.text,
                                                 self.ids.EscolaAlterarTextField.text,
                                                 self.ids.SenhaAlterarTextField.text,
                                                 self.ids.BiografiaAlterarTextField.text,
                                                 ''])
        if self.manager:
            self.manager.current = "CarregamentoInicial"


class TelaFavoritosPerfilProfissional(MDScreen):
    
    ControlePerfil = None
    ControleFavoritos = None
    FeedFavoritos = None
    ControlePost = None
    ControleAlbuns = None
    Favoritos = None
    GridAlbuns = None
    IDs = None
    Resultado = None
    Nome = None

        # Navegação entre telas
    def AlterarPerfilButton_Click(self):
        if self.manager:
            self.manager.current = "AlterarPerfilProfissional"

    def FavoritosPerfilButton_Click(self):
        if self.manager:
            self.manager.current = "FavoritosPerfilProfissional"

    def PerfilMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "PerfilProfissional"

    def AlunosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"

    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InformacoesJogosProfissionais"

    def ComunidadeMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "ComunidadeProfissionais"

    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ControlePerfil = tela_carregamento.Profissional
        else:
            self.ControlePerfil = None
        self.FeedFavoritos = self.ids.FeedFavoritos
        self.GridAlbuns = self.ids.GridAlbuns

        self.ControleFavoritos = FavoritosController()
        self.ControlePost = PostController()
        self.ControleAlbuns = AlbumController()
        self.Favoritos = self.ControleFavoritos.setListaFavoritos(f"USUARIO = '{self.ControlePerfil.Usuario}'")
        try:
            self.IDs = [item['PostID'] for item in self.Favoritos]
        except Exception as e:
            print(e)
            self.IDs = []
        self.Resultado = self.ControlePost.ListarPostPorID(self.IDs)
        self.Resultado = self.CarregarImagensPosts(self.Resultado)
        print("Favoritos:", self.Favoritos)
        print("IDs:", self.IDs)
        print(self.Resultado)
        self.ListarAlbuns()
        self.ListarFavoritos()

    def ListarAlbuns(self):
        self.GridAlbuns.clear_widgets()
        try:
            self.Albuns = self.ControleAlbuns.ListarAlbumPorUsuario(self.ControlePerfil.Usuario)

            if not self.Albuns:
                Label = MDLabel(
                    text="Nenhum álbum encontrado.",
                    halign="center",
                    valign="top",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1)
                )
                self.GridAlbuns.add_widget(Label)
                return

            for album in self.Albuns:
                # 🔹 Card maior e espaçado
                card = MDCard(
                    size_hint=(1, None),
                    height=dp(100),        # altura do card (aumente aqui)
                    padding=dp(15),
                    orientation="horizontal",
                    spacing=dp(25),
                    radius=[15, 15, 15, 15],
                    md_bg_color=(0.152, 0.251, 0.152, 1),
                    elevation=3,
                    on_release=lambda x, nome=album.get('nome', ''): self.AbrirAlbum(nome)
                )

                # 🔹 Ícone grande
                Icone = MDIcon(
                    icon="book",
                    size_hint=(None, None),
                    size=(dp(150), dp(150)),  # controla o tamanho real do ícone
                    font_size=dp(150),
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),  # amarelo
                    pos_hint={"center_y": 0.5}
                )

                # 🔹 Título do álbum
                titulo = MDLabel(
                    text=album.get('nome', ''),
                    halign="left",
                    valign="middle",
                    font_style="H5",
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1),
                    size_hint_x=1
                )
 

                # Espaçador à esquerda
                btn_menu = MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    pos=(dp(0), dp(0)),
                    radius=[20, 20, 20, 20]  # <- evita ValueError
                )

                menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
                menu.items = [
                    {
                        "text": "Excluir",
                        "icon": "delete",
                        "on_release": lambda x=album: (menu.dismiss(), self.excluir_album(x))
                    }
                ]

                btn_menu.on_release = menu.open

                # adiciona ao card
                card.add_widget(Icone)
                card.add_widget(titulo)
                card.add_widget(btn_menu)

                # adiciona ao grid
                self.GridAlbuns.add_widget(card)

        except Exception as e:
            print(e)

    
    def excluir_album(self, album):
        try:
            print(f"🗑️ Excluindo álbum: {album.get('nome')}")
            if self.ControleAlbuns.setAlbum(f"USUARIO = '{self.ControlePerfil.Usuario}' AND NOME = '{album.get('nome')}'"):
                self.ControleAlbuns.ExcluirAlbum()
                self.ListarAlbuns()
        except Exception as e:
            print(e)

    # Carrega imagens decodificando Base64 e associando pelo id do post
    def ListarFavoritos(self):
        self.FeedFavoritos.clear_widgets()
        try:
            if not self.Resultado:
                Label = MDLabel(
                    text="Nenhum favorito encontrado.",
                    halign="center",
                    valign="top",
                )

                self.FeedFavoritos.add_widget(Label)
                return
            
            for post in self.Resultado:
                box_post = MDBoxLayout(
                    orientation="vertical",
                    size_hint_y=None,
                    padding=dp(5),
                )

                card = MDCard(
                    size_hint_y=None,
                    padding=dp(10),
                    orientation="vertical",
                    spacing=dp(10)
                )

                # Cabeçalho
                box_cabecalho = MDBoxLayout(
                    orientation="horizontal",
                    size_hint_y=None,
                    height=dp(30),
                    spacing=dp(10)
                )

                usuario = MDLabel(
                    text=f"@{post.get('usuario', '')}",
                    font_size="16sp",
                    halign="left",
                    theme_text_color="Primary",
                    size_hint_x=0.7
                )
                usuario.bind(texture_size=usuario.setter('size'))

                btn_menu = MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    pos=(dp(0), dp(5))
                )

                # Cria menu
                menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
                menu.items = [
                    {
                        "text": "Excluir",
                        "icon": "delete",
                        "on_release": lambda x=post: (menu.dismiss(), self.excluir_post(x))
                    }
                ]

                btn_menu.on_release = menu.open

                box_cabecalho.add_widget(usuario)
                box_cabecalho.add_widget(btn_menu)
                card.add_widget(box_cabecalho)

                # Imagem do post
                imagem_obj = post.get('imagem_obj', None)
                if imagem_obj:
                    imagem_widget = Image(
                        texture=imagem_obj,
                        size_hint_y=None,
                        height=dp(600),
                        allow_stretch=True,
                        keep_ratio=True
                    )
                    card.add_widget(imagem_widget)

                # Legenda
                legenda = MDLabel(
                    text=post.get('legenda', ''),
                    halign="left",
                    theme_text_color="Secondary",
                    size_hint_y=None
                )
                legenda.bind(texture_size=legenda.setter('size'))
                card.add_widget(legenda)

                # Rodapé
                box_rodape = MDBoxLayout(
                    orientation="horizontal",
                    size_hint_y=None,
                    height=dp(30),
                    spacing=dp(10)
                )

                Favoritar_button = MDIconButton(
                    icon="star",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    radius=[20, 20, 20, 20],  # <- evita ValueError
                    icon_color=(1, 0.843, 0, 1)
                )
                Favoritar_button.post_id = post.get("id")

                Favoritar_button.favoritado = False
                Favoritar_button.bind(on_release=self.on_release_buttonfavoritos)

                Comentarios_button = MDIconButton(
                    icon="comment-outline",
                    size_hint=(None, None),
                    size=(dp(24), dp(24))
                )

                Comentarios_button.post_id = post.get("id")
                Comentarios_button.bind(on_release=self.abrir_comentarios)

                box_rodape.add_widget(Favoritar_button)
                box_rodape.add_widget(Comentarios_button)
                card.add_widget(box_rodape)

                card.bind(minimum_height=card.setter('height'))
                box_post.add_widget(card)
                box_post.bind(minimum_height=box_post.setter('height'))
                self.FeedFavoritos.add_widget(box_post)
        except IndexError:
            pass
    
    def on_release_buttonfavoritos(self, instance):
        self.post_id = getattr(instance, "post_id", None)
        print(f"ID do post favoritado: {self.post_id}")
        self.ControleFavoritos.setNewFavorito(self)
        if not instance.favoritado:
            instance.icon = "star-outline"
            instance.icon_color = (0.5, 0.5, 0.5, 1)
            instance.favoritado = False
            self.ControleFavoritos.Desfavoritar()
            self.Favoritos = self.ControleFavoritos.setListaFavoritos(f"USUARIO = '{self.ControlePerfil.Usuario}'")
            try:
                self.IDs = [item['PostID'] for item in self.Favoritos]
            except Exception as e:
                print(e)
                self.IDs = []
            self.Resultado = self.ControlePost.ListarPostPorID(self.IDs)
            self.Resultado = self.CarregarImagensPosts(self.Resultado)
            self.ListarFavoritos()
        else:
            instance.icon = "star"
            instance.icon_color = (1, 0.843, 0, 1)
            instance.favoritado = True
            self.ControleFavoritos.Favoritar()

    def excluir_post(self, post):
        print(f"🗑️ Excluindo post de {post.get('usuario')}")

    def abrir_comentarios(self, instance):
        self.instanciacomentario = instance
        self.post_id = getattr(instance, "post_id", None)
        resultado = self.Comentario.setListaComentarios(f'IDPOST = {self.post_id}')
        # BoxLayout que vai conter tudo
        BoxComentarios = MDBoxLayout(
            orientation="vertical",
            padding = dp(10),
            spacing = dp(10),
            size_hint_y = None,
            height = dp(500),  # define altura do box
            md_bg_color = (1, 1, 1, 1)
        )
        if resultado:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(20),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))

            for comentario in resultado:
                Card = MDCard(
                    size_hint_y=None,
                    padding=dp(10),
                    orientation="vertical",
                    spacing=dp(5),
                    md_bg_color=(0.8, 0.8, 0.8, 1)
                )

                BoxCabecalho = MDBoxLayout(
                    orientation="horizontal",
                    padding=dp(0),
                    spacing=dp(20),
                    size_hint_y=None,
                    md_bg_color=(1, 1, 1, 1)
                )

                btn_menu = MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    pos=(dp(0), dp(0))
                )

                btn_menu.theme_icon_color = "Custom"
                btn_menu.text_color  = (0, 0, 0, 0)

                BoxCabecalho.md_bg_color = (0.8, 0.8, 0.8, 1)
                BoxCabecalho.bind(minimum_height=BoxCabecalho.setter('height'))
                BoxCabecalho.add_widget(MDLabel(text=f"@{comentario['Usuario']}"))
                if comentario['Usuario'] == self.ControlePerfil.Usuario:
                    btn_menu.text_color  = (0, 0, 0, 1)
                    menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
                    menu.items = [
                        {
                            "text": "Excluir",
                            "icon": "delete",
                            "on_release": lambda x=comentario: (menu.dismiss(), self.ExcluirComentario(x))
                        }
                    ]
                    btn_menu.on_release = menu.open

                BoxCabecalho.add_widget(btn_menu)
                Card.add_widget(BoxCabecalho)
                TextoComentario = MDLabel(
                    text=comentario['Texto'],
                    size_hint_y = None
                )
                Card.add_widget(TextoComentario)

                Card.bind(minimum_height=Card.setter('height'))
                BoxComentario.add_widget(Card)
        else:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(10),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))
            BoxComentario.add_widget(
                MDLabel(
                    text='Sem Comentários. Seja o Primeiro!',
                    halign="center",
                    valign="center",
                )
            )

        BoxPostarComentario = MDBoxLayout(
            orientation="horizontal",
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(80),  # define altura do box
            md_bg_color=(1, 1, 1, 1),
        )

        self.tf = TextInput(
            size_hint_x=0.8,
            cursor_color=(0, 0, 0, 1),
            foreground_color=(0, 0, 0, 1),
            multiline=True,
        )

        # limite de caracteres
        self.tf.max_chars = 500

        # evento que monitora a digitação
        self.tf.bind(text=self.limitar_texto)

        # Botão circular com seta
        btn_cima = MDFloatingActionButton(
            icon="arrow-up",
            md_bg_color=(1, 1, 1, 1),
            text_color=(0, 0, 0, 1),
        )

        btn_cima.bind(on_release=lambda _: self.on_release_Comentarios_button())
        BoxPostarComentario.add_widget(self.tf)
        BoxPostarComentario.add_widget(btn_cima)

        # ScrollView para permitir rolagem se necessário
        scroll = ScrollView(
            do_scroll_x=False, do_scroll_y=True,
            size_hint=(1, None),
            height=dp(400)
        )

        scroll.add_widget(BoxComentario)
        BoxComentarios.add_widget(scroll)
        BoxComentarios.add_widget(BoxPostarComentario)

        # Cria o Dialog
        self.dialog = MDDialog(
            title="Comentários",
            type="custom",
            content_cls=BoxComentarios,
            size_hint=(0.5, None),
            height=dp(180),  # altura do diálogo
        )

        # Abre o Dialog
        self.dialog.open()

    def limitar_texto(self, instance, value):
        if len(value) > instance.max_chars:
            instance.text = value[:instance.max_chars]

    def AtualizarComentarios(self, instance):
        if self.dialog:
            self.dialog.dismiss()
        self.abrir_comentarios(instance)

    def on_release_Comentarios_button(self):
        try:
            self.Comentario.setNewComentario(self)
            self.Comentario.Comentar()
            self.AtualizarComentarios(self.instanciacomentario)
        except Exception as e:
            print(e)

    def GetFavoritos(self):
        ListaPostsHelper = Posts()
        lista = []
        try:
            for id in self.IDs:
                Resultado = ListaPostsHelper.GetPorId(id)
                if Resultado:
                    for post in Resultado:
                        lista.append({
                            'id': post['id'],
                            'usuario': post['usuario'],
                            'imagem': post['imagem']
                        })
            return lista
        except Exception as e:
            print(f"Erro ao obter favoritos: {e}")
            return []
    # Carrega imagens decodificando Base64 e associando pelo id do post
    def CarregarImagensPosts(self, posts):
        try:
            posts_no_banco = self.GetFavoritos()  # pega todos os posts do banco

            # Cria um dicionário de imagens pelo id do post
            print(posts_no_banco)
            imagens_dict = {}
            for post_banco in posts_no_banco:
                imagem_b64 = post_banco.get('imagem', None)
                textura = None
                if imagem_b64 and imagem_b64 not in ("NULL", "null", ""):
                    try:
                        data = io.BytesIO(base64.b64decode(imagem_b64))
                        textura = CoreImage(data, ext='png').texture  # ou tente detectar o formato
                    except Exception:
                        try:
                            data = io.BytesIO(base64.b64decode(imagem_b64))
                            textura = CoreImage(data, ext='jpg').texture
                        except Exception as e:
                            print(f"Erro ao carregar imagem: {e}")
                            textura = None

                imagens_dict[post_banco['id']] = textura

            # Atualiza os posts originais com a textura correta
            for post in posts:
                post['imagem_obj'] = imagens_dict.get(post.get('id'), None)
                print(f"Imagem no post {post.get('id', 'SEM ID')}: {bool(post.get('imagem_obj'))}")

            return posts

        except Exception as e:
            print(f"Erro ao carregar imagens dos posts: {e}")
            return posts

    def ExcluirComentario(self, post):
        pass

    def AdicionarAlbum(self):
        from kivymd.uix.boxlayout import MDBoxLayout
        from kivymd.uix.textfield import MDTextField
        from kivymd.uix.button import MDFloatingActionButton
        from kivymd.uix.label import MDLabel
        from kivymd.uix.dialog import MDDialog
        from kivy.metrics import dp
        from kivy.uix.widget import Widget

        # Layout principal do diálogo
        BoxAlbum = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(25),
            size_hint_y=None,
            height=dp(300),
            md_bg_color=(1, 1, 1, 1)
        )

        # Título interno
        Titulo = MDLabel(
            text="Adicionar Álbum",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.2, 0.2, 0.2, 1),
            font_style="H6",
            bold=True
        )

        # Campo de texto
        NomeText = MDTextField(
            id = 'NomeAlbumTextField',
            hint_text="Digite op nome do album",
            mode="rectangle",
            size_hint_x=1,
            line_color_normal=(0.7, 0.7, 0.7, 1),
            line_color_focus=(0.2, 0.6, 0.3, 1),
            text_color_normal=(0, 0, 0, 1),
            text_color_focus=(0, 0, 0, 1),
            cursor_color=(0.2, 0.6, 0.3, 1),
            icon_right="account",
            radius=[10, 10, 10, 10],
        )

        # Espaço entre campo e botão
        Spacer = Widget(size_hint_y=None, height=dp(10))

        # Botão flutuante para confirmar
        from kivymd.uix.button import MDRectangleFlatIconButton

        Botao = MDRectangleFlatIconButton(
            text="Adicionar",
            icon="plus",
            line_color=(0.2, 0.6, 0.3, 1),
            text_color=(0.2, 0.6, 0.3, 1),
            pos_hint={"center_x": 0.5},
            on_release=lambda x: self.ConfirmarAlbum(NomeText.text)
        )

        # Adiciona elementos ao layout
        BoxAlbum.add_widget(Titulo)
        BoxAlbum.add_widget(NomeText)
        BoxAlbum.add_widget(Spacer)
        BoxAlbum.add_widget(Botao)

        # Diálogo principal
        self.dialog = MDDialog(
            title="",
            type="custom",
            content_cls=BoxAlbum,
            radius=[20, 20, 20, 20],
            md_bg_color=(0.97, 0.97, 0.97, 1),
            size_hint=(0.6, None),
            height=dp(400),
        )

        self.dialog.open()

    def ConfirmarAlbum(self, nome_album):
        self.Nome = nome_album
        album = AlbumController()
        if not nome_album.strip():
            toast("Por favor, digite o registro do album.")
            return

        album.setNewAlbum(self, nome_album)
        album.Salvar()
        self.ListarAlbuns()
        self.dialog.dismiss()
        toast(f"Álbum '{nome_album}' adicionado com sucesso!")

    def AbrirAlbum(self, nome):
        self.Nome = nome
        if self.manager:
            self.manager.current = 'AlbumEspecifico'

class TelaAlunosProfissional(MDScreen):
    Sessao = LoginController()
    ProfissionalControle = ProfissionalControler()
    AlunoControle = AlunoController()
    aluno_usuario = None

    def on_enter(self, *args):
        self.Sessao.setLogin(self.manager)
        self.ProfissionalControle.setUsuario(f'USUARIO = "{self.Sessao.usuario}"')
        self.ListarAlunos()

    def ListarAlunos(self):
        # Pega os alunos do profissional
        ListaAlunos = self.AlunoControle.ListarAlunosPorProfissional(
            self.ProfissionalControle.CPF
        )
        DataGrid = self.ids.AlunosDataGridBox
        DataGrid.clear_widgets()  # Limpa widgets antigos

        if not ListaAlunos:
            # Caso não haja alunos
            Card = MDCard(
                size_hint_y=0.8,
                padding=dp(10),
                orientation="vertical",
                spacing=dp(10),
                pos_hint={"x": 0.5, "y": 0.2}
            )
            SemAluno = MDLabel(
                text='Sem alunos. Adicione seus alunos ao App!',
                font_style="H6",
                halign="center",
                valign="top",
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1)
            )
            Card.add_widget(SemAluno)
            DataGrid.add_widget(
                Widget(
                    size_hint_x=0.4,
                )
            )
            DataGrid.add_widget(Card)
            DataGrid.add_widget(
                Widget(
                    size_hint_x=0.4,
                )
            )
        else:
            # Monta dados da tabela
            Dados = [
                (
                    aluno["RE"],
                    aluno["Nome"],
                    aluno["Usuario"],
                    aluno["Escola"],
                    aluno["Genero"],
                    aluno["Turma"],
                    aluno["Diagnostico"],
                    aluno['DataNascimento']
                ) for aluno in ListaAlunos
            ]

            # Cria o MDDataTable
            tabela = MDDataTable(
                size_hint=(4, 1),
                use_pagination=False,
                rows_num=5,  # substitui rows_per_page
                column_data=[
                    ("RE", dp(30)),
                    ("Nome", dp(30)),
                    ("Usuario", dp(30)),
                    ("Escola", dp(40)),
                    ("Genero", dp(30)),
                    ("Turma", dp(30)),
                    ("Diagnostico", dp(30)),
                    ('DataNascimento', dp(20))
                ],
                row_data=Dados
            )
            tabela.bind(on_row_press=self.on_row_press)


            DataGrid.add_widget(Widget())
            DataGrid.add_widget(tabela)
            DataGrid.add_widget(Widget())

    def on_row_press(self, instance_table, instance_row):
        colunas = len(instance_table.column_data)
        indice_celula = instance_row.index
        linha = indice_celula // colunas
        coluna = indice_celula % colunas
        self.aluno_RA = instance_row.table.row_data[linha][0]
        print(self.aluno_RA)
        if self.manager:
            self.manager.current = "AlunoEspecifico"


    def PerfilMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "PerfilProfissional"

    def AlunosMDTextButton_Click(self):
        pass

    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InformacoesJogosProfissionais"

    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InformacoesJogosProfissionais"

    def ComunidadeMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "ComunidadeProfissionais"

    def AdicionarAlunoButton_Click(self):
        if self.manager:
            self.manager.current = "AdicionarAluno"

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"

class TelaInformacoesJogosProfissionais(MDScreen):
    Titulo = StringProperty("")
    Objetivo = StringProperty("")
    Competencias = StringProperty("")
    BaseTeorica = StringProperty("")
    Instrucoes = StringProperty("")
    Classificar = StringProperty("")
    Explicacoes = StringProperty("")

    def on_enter(self, *args):
        pass

    def JogosCard_Click(self, jogo):
        if jogo == 1:
            self.Titulo = 'Jogo dos 7 Erros'
            self.Objetivo = 'Desenvolver a Percepção Visual e o Pensamento Crítico através da identificação e análise de semelhanças e diferenças entre duas imagens.'
            self.Competencias = 'Atenção Sustentada, Concentração Visual, Análise e Síntese, Habilidade de Comparação e Raciocínio Lógico-Visual.'
            self.BaseTeorica = 'Fundamentado na Teoria da Gestalt (que estuda a percepção de formas e padrões) e nas Funções Executivas (especificamente o controle de atenção e inibição).'
            self.Instrucoes = 'Oriente a criança a escanear a imagem de forma sistemática (de cima para baixo, da esquerda para a direita) para evitar a busca aleatória. Peça que verbalize o que mudou (tamanho, cor, posição) após encontrar o erro.'
            self.Classificar = 'Raciocínio'
            self.Explicacoes = 'Consiste em duas imagens que parecem idênticas, mas que contêm um número específico de diferenças intencionais (geralmente 7). O jogador deve usar a comparação ativa para localizar os pontos de divergência. A atividade treina o cérebro a filtrar informações redundantes e focar apenas nas alterações.'
        elif jogo == 2:
            self.Titulo = 'WaterSort'
            self.Objetivo = 'Treinar o Planejamento Multiestágio e o Raciocínio Lógico Dedutivo, ensinando a criança a antecipar e otimizar movimentos sob regras de restrição.'
            self.Competencias = 'Raciocínio Lógico, Pensamento Estratégico, Antecipação, Resolução de Problemas (fase de "tentativa e erro" e análise de consequências) e Concentração.'
            self.BaseTeorica = 'Baseado na Teoria da Resolução de Problemas (Heurística) e no desenvolvimento de Funções Executivas, como o planejamento e a memória de trabalho (para reter o estado atual dos tubos).'
            self.Instrucoes = 'Incentive a criança a pensar sobre o movimento atual e suas consequências a longo prazo ("O que este movimento me permite fazer no futuro?"). Em caso de travamento, peça que reinicie, revisando mentalmente a estratégia inicial.'
            self.Classificar = 'Raciocínio'
            self.Explicacoes = 'O jogador deve classificar líquidos coloridos em tubos de ensaio, de modo que cada tubo contenha apenas uma cor. As regras de restrição (só pode despejar em um tubo se a cor for a mesma do topo e houver espaço) exigem a criação de uma sequência lógica de movimentos para liberar os tubos e permitir a classificação completa.'
        elif jogo == 3:
            self.Titulo = 'SílabasMix'
            self.Objetivo = 'Desenvolver a Consciência Silábica e Fonológica, permitindo a análise (separação) e a síntese (junção) de sílabas para a construção de palavras.'
            self.Competencias = 'Consciência Fonológica, Análise e Síntese, Rastreamento Visual da Palavra, Reconhecimento de Padrões Ortográficos e Vocabulário.'
            self.BaseTeorica = 'Fundamentado no Modelo Construtivista da aquisição da escrita e em pesquisas sobre a importância do conhecimento das unidades menores (sílabas) para o avanço no processo de alfabetização.'
            self.Instrucoes = 'Peça que a criança pronuncie a palavra em voz alta, batendo palmas a cada sílaba, antes de manipular as peças. Proponha desafios como: "Se tirarmos a primeira sílaba de "sapato", o que sobra?".'
            self.Classificar = 'Palavras'
            self.Explicacoes = 'O jogo apresenta diferentes atividades com sílabas (digitação, arrasto, clique) que requerem a identificação e a manipulação de sílabas simples e complexas para completar ou formar palavras ilustradas. Estimula o reconhecimento de que a palavra escrita é formada pela união de unidades silábicas.'
        elif jogo == 4:
            self.Titulo = 'Som e Sílaba'
            self.Objetivo = 'Estabelecer a conexão sólida entre os sons da fala (fonemas/sílabas orais) e suas representações escritas (grafemas), fundamentando o princípio alfabético.'
            self.Competencias = 'Discriminação Auditiva, Memória Sonora, Associação Fonema-Grafema, Reconhecimento de Letras e Sílabas Iniciais e Leitura Fonética.'
            self.BaseTeorica = 'Apoiado nos estudos da Consciência Fonológica e do Processamento Fonológico, essenciais para a decodificação de palavras e o diagnóstico/intervenção em dificuldades de leitura (dislexia).'
            self.Instrucoes = 'Use o método multisensorial, pedindo à criança para tocar na letra ou sílaba enquanto emite o som. Concentre-se nos sons, não apenas nos nomes das letras. O feedback imediato sobre acerto/erro é crucial.'
            self.Classificar = 'Palavras'
            self.Explicacoes = 'Apresenta desafios onde a criança deve ouvir um som (de letra ou sílaba) e selecionar a representação gráfica correspondente, ou vice-versa. Utiliza recursos visuais e auditivos para reforçar a ideia de que a escrita representa a fala, tornando o aprendizado da leitura mais consistente e significativo.'
        elif jogo == 5:
            self.Titulo = 'Jogo da Memória'
            self.Objetivo = 'Fortalecer a Memória de Trabalho e a Associação Semântica, ligando o conceito visual (imagem) à sua forma escrita (palavra) para acelerar o reconhecimento de leitura.'
            self.Competencias = 'Memória Visual e Espacial, Concentração, Raciocínio Lógico (estratégia de localização), Reconhecimento de Palavras (vocabulário) e Leitura Global.'
            self.BaseTeorica = 'Utiliza princípios da Teoria Cognitiva da Aprendizagem (processamento de informação e memória de curto prazo) e da Abordagem Lexical, que prioriza o reconhecimento da palavra completa.'
            self.Instrucoes = 'Comece com poucos pares e aumente gradualmente a dificuldade. Antes de virar as cartas, peça à criança para tentar ler as palavras viradas ou nomear as figuras para reforçar a associação.'
            self.Classificar = 'Memória'
            self.Explicacoes = 'As cartas são dispostas viradas para baixo; uma carta contém a imagem de um objeto e a outra contém o nome escrito desse objeto. O jogador deve virar duas cartas por vez para encontrar o par correspondente (imagem e palavra), exercitando a lembrança da localização e a leitura.'
        elif jogo == 6:
            self.Titulo = 'Memória das Cores'
            self.Objetivo = 'Desenvolver a Memória Visual, a Sequenciação e o Reconhecimento de Padrões, habilidades que servem como pré-requisitos para a organização do pensamento em tarefas complexas.'
            self.Competencias = 'Memória Visual de Curto Prazo, Discriminação Visual, Rastreamento e Reprodução de Padrões, Concentração e Organização da Informação.'
            self.BaseTeorica = 'Enraizado na Psicologia Cognitiva (estudo da memória de curto prazo e da capacidade de codificação e recuperação de estímulos visuais) e na importância do reconhecimento de padrões para o raciocínio.'
            self.Instrucoes = 'Para jogos de sequência (como o Genius), peça que a criança verbalize a sequência de cores antes de reproduzi-la (codificação verbal). Para jogos de pares, estimule a criação de estratégias de localização espacial.'
            self.Classificar = 'Memória'
            self.Explicacoes = 'Em sua forma clássica, é um jogo de memória simples de encontrar pares de cores idênticas. Em sua forma avançada (sequência), o jogo exibe um padrão de luzes e sons coloridos que o jogador deve memorizar e reproduzir. A dificuldade aumenta progressivamente, exigindo um esforço crescente da memória para reter sequências longas.'

        if self.manager:
            self.manager.current = "InformacaoJogoEspecifico"


    def JogosMDDropDownItem_Click(self, instancia):
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": "Raciocínio",
                "height": dp(40),
                "width": dp(100),
                "on_release": lambda x="Raciocínio": self.opcao_selecionada(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Palavras",
                "height": dp(40),
                "width": dp(100),
                "on_release": lambda x="Palavras": self.opcao_selecionada(x),
            },
            {
                "viewclass": "OneLineListItem",
                "text": "Memória",
                "height": dp(40),
                "width": dp(100),
                "on_release": lambda x="Memória": self.opcao_selecionada(x),
            },
        ]

        # Cria o menu dropdown centralizado e logo abaixo do botão
        self.menu = MDDropdownMenu(
            caller=instancia,
            items=menu_items,
            width_mult=0,
            background_color=(0.15, 0.15, 0.15, 1),
            ver_growth="down",  # garante que o menu cresça para baixo
            position="bottom",  # centraliza em relação ao botão
        )

        # Ajuste fino: empurra um pouco o menu para baixo
        self.menu.open()

    def opcao_selecionada(self, texto):
        print(f"Opção selecionada: {texto}")
        self.menu.dismiss()

    def on_pre_enter(self):
        self.ids.carrossel.bind(index=self.verificar_loop)

    def verificar_loop(self, instance, value):
        total = len(instance.slides)
        # Se estiver no último e tentar avançar → volta ao primeiro
        if value == total - 1 and instance.direction == "right":
            instance.index = 0
        # Se estiver no primeiro e tentar voltar → vai para o último
        elif value == 0 and instance.direction == "left":
            instance.index = total - 1
        # Adicionando loop para o lado esquerdo quando arrasta do primeiro para trás
        elif value < 0:
            instance.index = total - 1

    def PerfilMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "PerfilProfissional"

    def AlunosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"

    def ComunidadeMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "ComunidadeProfissionais"

class TelaComunidadeProfissionais(MDScreen):

    Favoritos = None
    Post = None
    FeedComunidade = None
    resposta = None
    ControlePerfil = None
    Comentario = None
    dialog = None
    instanciacomentario = None

    def on_pre_enter(self, *args):
        self.Post = PostController()
        self.FeedComunidade = self.ids.FeedComunidade
        self.Favoritos = FavoritosController()
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ControlePerfil = tela_carregamento.Profissional
        else:
            self.ControlePerfil = None

        self.Comentario = ComentarioController()
        # Carrega todos os posts
        self.resposta = self.Post.ListarPosts()

        # Atualiza posts com imagens
        self.resposta = self.CarregarImagensPosts(self.resposta)

        # Lista os posts no feed
        self.ListarPosts()

    # Navegação entre telas
    def PerfilMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "PerfilProfissional"

    def AlunosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"

    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InformacoesJogosProfissionais"

    def ComunidadeMDTextButton_Click(self):
        pass

    def PostarNoFeed(self):
        if self.manager:
            self.manager.current = "PostarNoFeed"

    # Atualiza o feed
    def AtualizarFeed(self):
        self.resposta = self.Post.ListarPosts()
        self.resposta = self.CarregarImagensPosts(self.resposta)
        self.ListarPosts()


    def ListarPosts(self):
        self.FeedComunidade.clear_widgets()

        for post in self.resposta:
            box_post = MDBoxLayout(
                orientation="vertical",
                size_hint_y=None,
                padding=dp(5),
            )

            card = MDCard(
                size_hint_y=None,
                padding=dp(10),
                orientation="vertical",
                spacing=dp(10)
            )

            # Cabeçalho
            box_cabecalho = MDBoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(30),
                spacing=dp(10)
            )

            usuario = MDLabel(
                text=f"@{post.get('usuario', '')}",
                font_size="16sp",
                halign="left",
                theme_text_color="Primary",
                size_hint_x=0.7
            )
            usuario.bind(texture_size=usuario.setter('size'))

            btn_menu = MDIconButton(
                icon="dots-vertical",
                size_hint=(None, None),
                size=(dp(24), dp(24)),
                pos=(dp(0), dp(5)),
                radius=[20, 20, 20, 20]  # <- evita ValueError
            )

            # Cria menu
            menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
            menu.items = [
                {
                    "text": "Excluir",
                    "icon": "delete",
                    "on_release": lambda x=post: (menu.dismiss(), self.excluir_post(x))
                }
            ]

            btn_menu.on_release = menu.open

            box_cabecalho.add_widget(usuario)
            box_cabecalho.add_widget(btn_menu)
            card.add_widget(box_cabecalho)

            # Imagem do post
            imagem_obj = post.get('imagem_obj', None)
            if imagem_obj:
                imagem_widget = Image(
                    texture=imagem_obj,
                    size_hint_y=None,
                    height=dp(400),
                    allow_stretch=True,
                    keep_ratio=True
                )
                card.add_widget(imagem_widget)

            # Legenda
            legenda = MDLabel(
                text=post.get('legenda', ''),
                halign="left",
                theme_text_color="Secondary",
                size_hint_y=None
            )
            legenda.bind(texture_size=legenda.setter('size'))
            card.add_widget(legenda)

            # Rodapé
            box_rodape = MDBoxLayout(
                orientation="horizontal",
                size_hint_y=None,
                height=dp(30),
                spacing=dp(10)
            )

            Favoritar_button = MDIconButton(
                icon="star-outline",
                size_hint=(None, None),
                size=(dp(24), dp(24)),
                radius=[20, 20, 20, 20]  # <- evita ValueError
            )
            Favoritar_button.post_id = post.get("id")

            Favoritar_button.favoritado = False
            Favoritar_button.bind(on_release=self.on_release_buttonfavoritos)

            Comentarios_button = MDIconButton(
                icon="comment-outline",
                size_hint=(None, None),
                size=(dp(24), dp(24)),
                radius=[20, 20, 20, 20]  # <- evita ValueError
            )
            Comentarios_button.post_id = post.get("id")
            Comentarios_button.bind(on_release=self.abrir_comentarios)

            box_rodape.add_widget(Favoritar_button)
            box_rodape.add_widget(Comentarios_button)
            card.add_widget(box_rodape)

            card.bind(minimum_height=card.setter('height'))
            box_post.add_widget(card)
            box_post.bind(minimum_height=box_post.setter('height'))
            self.FeedComunidade.add_widget(box_post)

    def excluir_post(self, post):
        print(f"🗑️ Excluindo post de {post.get('usuario')}")

    def abrir_comentarios(self, instance):
        self.instanciacomentario = instance
        self.post_id = getattr(instance, "post_id", None)
        resultado = self.Comentario.setListaComentarios(f'IDPOST = {self.post_id}')
        # BoxLayout que vai conter tudo
        BoxComentarios = MDBoxLayout(
            orientation="vertical",
            padding = dp(10),
            spacing = dp(10),
            size_hint_y = None,
            height = dp(500),  # define altura do box
            md_bg_color = (1, 1, 1, 1)
        )
        if resultado:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(20),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))

            for comentario in resultado:
                Card = MDCard(
                    size_hint_y=None,
                    padding=dp(10),
                    orientation="vertical",
                    spacing=dp(5),
                    md_bg_color=(0.8, 0.8, 0.8, 1)
                )

                BoxCabecalho = MDBoxLayout(
                    orientation="horizontal",
                    padding=dp(0),
                    spacing=dp(20),
                    size_hint_y=None,
                    md_bg_color=(1, 1, 1, 1)
                )

                btn_menu = MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    pos=(dp(0), dp(0)),
                    radius=[20, 20, 20, 20]  # <- evita ValueError
                )

                btn_menu.theme_icon_color = "Custom"
                btn_menu.text_color  = (0, 0, 0, 0)

                BoxCabecalho.md_bg_color = (0.8, 0.8, 0.8, 1)
                BoxCabecalho.bind(minimum_height=BoxCabecalho.setter('height'))
                BoxCabecalho.add_widget(MDLabel(text=f"@{comentario['Usuario']}"))
                if comentario['Usuario'] == self.ControlePerfil.Usuario:
                    btn_menu.text_color  = (0, 0, 0, 1)
                    menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
                    menu.items = [
                        {
                            "text": "Excluir",
                            "icon": "delete",
                            "on_release": lambda x=comentario: (menu.dismiss(), self.ExcluirComentario(x))
                        }
                    ]
                    btn_menu.on_release = menu.open

                BoxCabecalho.add_widget(btn_menu)
                Card.add_widget(BoxCabecalho)
                TextoComentario = MDLabel(
                    text=comentario['Texto'],
                    size_hint_y = None
                )
                Card.add_widget(TextoComentario)

                Card.bind(minimum_height=Card.setter('height'))
                BoxComentario.add_widget(Card)
        else:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(10),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))
            BoxComentario.add_widget(
                MDLabel(
                    text='Sem Comentários. Seja o Primeiro!',
                    halign="center",
                    valign="center",
                )
            )

        BoxPostarComentario = MDBoxLayout(
            orientation="horizontal",
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(80),  # define altura do box
            md_bg_color=(1, 1, 1, 1),
        )

        self.tf = TextInput(
            size_hint_x=0.8,
            cursor_color=(0, 0, 0, 1),
            foreground_color=(0, 0, 0, 1),
            multiline=True,
        )

        # limite de caracteres
        self.tf.max_chars = 500

        # evento que monitora a digitação
        self.tf.bind(text=self.limitar_texto)

        # Botão circular com seta
        btn_cima = MDFloatingActionButton(
            icon="arrow-up",
            md_bg_color=(1, 1, 1, 1),
            text_color=(0, 0, 0, 1),
        )

        btn_cima.bind(on_release=lambda _: self.on_release_Comentarios_button())
        BoxPostarComentario.add_widget(self.tf)
        BoxPostarComentario.add_widget(btn_cima)

        # ScrollView para permitir rolagem se necessário
        scroll = ScrollView(
            do_scroll_x=False, do_scroll_y=True,
            size_hint=(1, None),
            height=dp(400)
        )

        scroll.add_widget(BoxComentario)
        BoxComentarios.add_widget(scroll)
        BoxComentarios.add_widget(BoxPostarComentario)

        # Cria o Dialog
        self.dialog = MDDialog(
            title="Comentários",
            type="custom",
            content_cls=BoxComentarios,
            size_hint=(0.5, None),
            height=dp(180),  # altura do diálogo
        )

        # Abre o Dialog
        self.dialog.open()

    def limitar_texto(self, instance, value):
        if len(value) > instance.max_chars:
            instance.text = value[:instance.max_chars]

    def AtualizarComentarios(self, instance):
        if self.dialog:
            self.dialog.dismiss()
        self.abrir_comentarios(instance)

    def on_release_buttonfavoritos(self, instance):
        self.post_id = getattr(instance, "post_id", None)
        print(f"ID do post favoritado: {self.post_id}")
        self.Favoritos.setNewFavorito(self)
        if instance.favoritado:
            instance.icon = "star-outline"
            instance.icon_color = (0.5, 0.5, 0.5, 1)
            instance.favoritado = False
            self.Favoritos.Desfavoritar()
        else:
            instance.icon = "star"
            instance.icon_color = (1, 0.843, 0, 1)
            instance.favoritado = True
            self.Favoritos.Favoritar()

    def on_release_Comentarios_button(self):
        try:
            self.Comentario.setNewComentario(self)
            self.Comentario.Comentar()
            self.AtualizarComentarios(self.instanciacomentario)
        except Exception as e:
            print(e)

    # Carrega imagens decodificando Base64 e associando pelo id do post
    def CarregarImagensPosts(self, posts):
        try:
            ListaPostsHelper = Posts()
            posts_no_banco = ListaPostsHelper.Get()  # pega todos os posts do banco

            # Cria um dicionário de imagens pelo id do post
            imagens_dict = {}
            for post_banco in posts_no_banco:
                imagem_b64 = post_banco.get('imagem', None)
                textura = None
                if imagem_b64 and imagem_b64 not in ("NULL", "null", ""):
                    try:
                        data = io.BytesIO(base64.b64decode(imagem_b64))
                        textura = CoreImage(data, ext='png').texture
                    except Exception as e:
                        print(f"Erro ao decodificar imagem do post {post_banco.get('id', '')}: {e}")
                imagens_dict[post_banco['id']] = textura

            # Atualiza os posts originais com a textura correta
            for post in posts:
                post['imagem_obj'] = imagens_dict.get(post.get('id'), None)

            return posts

        except Exception as e:
            print(f"Erro ao carregar imagens dos posts: {e}")
            return posts

    def ExcluirComentario(self, post):
        pass

class TelaPostarNoFeed(MDScreen):
    file_manager = None
    imagem_base64 = None
    Vizualizacao = None
    textura = None
    MidiaPostarTextField = None
    LegendaPostarTextField = None
    PostControle = None
    ProfissionalControle = None

    def on_enter(self, *args):
        self.file_manager = MDFileManager(
            exit_manager=self.fechar_file_manager,
            select_path=self.selecionar_imagem
        )
        self.Vizualizacao = self.ids.vizualizacao
        self.MidiaPostarTextField = self.ids.MidiaPostarTextField
        self.LegendaPostarTextField = self.ids.LegendaPostarTextField
        self.PostControle = PostController()
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ProfissionalControle = tela_carregamento.Profissional
        else:
            self.ProfissionalControle = None

    def fechar_file_manager(self, *args):
        self.file_manager.close()

    def selecionar_imagem(self, path):
        """Chamado quando o usuário escolhe uma imagem no file manager"""
        self.fechar_file_manager()

        try:
            with open(path, "rb") as f:
                imagem_bytes = f.read()

            # Converte para base64
            self.imagem_base64 = base64.b64encode(imagem_bytes).decode("utf-8")

            # Descobre extensão real do arquivo
            _, ext = os.path.splitext(path)
            ext = ext.replace(".", "").lower()
            if ext not in ["png", "jpg", "jpeg"]:
                ext = "png"  # fallback

            # Decodifica textura
            data = io.BytesIO(base64.b64decode(self.imagem_base64))
            self.textura = CoreImage(data, ext=ext).texture

            # Limpa e ajusta área de visualização
            self.Vizualizacao.clear_widgets()
            self.Vizualizacao.size_hint_y = None
            self.Vizualizacao.height = dp(500)  # altura fixa para área da imagem

            # Cria card envolvente
            card = MDCard(
                size_hint=(0.85, None),
                height=dp(480),
                pos_hint={"center_x": 0.5},
                orientation="vertical",
                elevation=8,
                shadow_softness=4,
                radius=[25, 25, 25, 25],
                md_bg_color=(0, 0, 0, 0.5),
            )

            BotaoRetirar = MDIconButton(
                icon = 'close-circle',
                theme_icon_color = "Custom",
                icon_color = (1, 1, 1, 1),
                on_release=lambda x: self.remover_imagem()
            )

            card.add_widget(BotaoRetirar)

            imagem_widget = Image(
                texture=self.textura,
                allow_stretch=True,
                keep_ratio=True,
                size_hint=(0.80, 0.80),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )

            card.add_widget(imagem_widget)


            self.Vizualizacao.add_widget(card)
            self.MidiaPostarTextField.text = str(path)
            MDDialog(title="Imagem selecionada", text=f"Caminho: {path}").open()

        except Exception as e:
            print(f"Erro ao processar imagem selecionada: {e}")
            MDDialog(title="Erro", text=f"Não foi possível carregar a imagem.\n{e}").open()

    def MidiaPostarTextField_Focus(self, *args):
        self.SelecionarImagem()

    def SelecionarImagem(self):
        initial_path = "/" if Window.system_size[0] > 0 else "."
        self.file_manager.show(initial_path)

    def remover_imagem(self):
        self.Vizualizacao.clear_widgets()
        self.imagem_base64 = None
        self.textura = None
        self.Vizualizacao.size_hint_y = 0.01
        self.MidiaPostarTextField.text = ''

    def VoltarComunidade_Click(self):
        if self.manager:
            self.manager.current = "ComunidadeProfissionais"

    def CancelarPostarButton_Click(self):
        self.MidiaPostarTextField.text = ''
        self.Vizualizacao.clear_widgets()
        self.imagem_base64 = None
        self.textura = None
        self.Vizualizacao.size_hint_y = 0.01
        self.LegendaPostarTextField.text = ''
        if self.manager:
            self.manager.current = "ComunidadeProfissionais"

    def PostarButton_Click(self):
        try:
            self.PostControle.setNewPost(self)
            self.PostControle.Postar()
            if self.manager:
                self.manager.current = "ComunidadeProfissionais"
        except Exception as e:
            print(e)

class TelaInformacaoJogoEspecifico(MDScreen):
    Titulo = StringProperty("")
    Objetivo = StringProperty("")
    Competencias = StringProperty("")
    BaseTeorica = StringProperty("")
    Instrucoes = StringProperty("")
    Classificar = StringProperty("")
    Explicacoes = StringProperty("")

    def on_pre_enter(self, *args):
        JogoEspecifico = self.manager.get_screen("InformacoesJogosProfissionais")
        self.Titulo = JogoEspecifico.Titulo
        self.Objetivo = JogoEspecifico.Objetivo
        self.Competencias = JogoEspecifico.Competencias
        self.BaseTeorica = JogoEspecifico.BaseTeorica
        self.Instrucoes = JogoEspecifico.Instrucoes
        self.Classificar = JogoEspecifico.Classificar
        self.Explicacoes = JogoEspecifico.Explicacoes

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "InformacoesJogosProfissionais"

class TelaAdicionarAluno(MDScreen):
    ControleProfissional = None
    AlunoControle = None

    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ControleProfissional = tela_carregamento.Profissional
        else:
            self.ControleProfissional = None
        self.AlunoControle = AlunoController()

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"


    def UFAlunosProfissionaisTextField_Focus(self,instancia,focus):
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
                        "on_release": lambda x=f'{index}': self.UFAlunosProfissionais_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def UFAlunosProfissionais_ItensClick(self, text_item):
        self.ids.UFAlunosTextField.text = text_item

    def CidadeAlunosProfissionaisTextField_Focus(self, instancia, focus):
        if focus:
            Cidade = Cidades()
            try:
                itens = Cidade.get_cidades_por_uf(self.ids.UFAlunosTextField.text)

                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.CidadeAlunosProfissional_ItensClick(x)
                    } for index in itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            except Exception as e:
                print(e)
        else:
            print('erro')


    def CidadeAlunosProfissional_ItensClick(self, text_item):
        self.ids.CidadeAlunosTextField.text = text_item

    def EscolaAlunosProfissionalTextField_Focus(self, instancia, focus):
        if focus:
            Escola = Escolas()
            try:
                dados = Escola.Get(self.ids.UFAlunosTextField.text, self.ids.CidadeAlunosTextField.text)
                itens = [item["escola"] for item in dados if "escola" in item]
                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.EscolaAlunosProfissional_ItensClick(x)
                    } for index in itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            except:
                pass
        else:
            print('erro')

    def EscolaAlunosProfissional_ItensClick(self, text_item):
        self.ids.EscolaAlunosTextField.text = text_item

    def NivelLeituraAlunosProfissionalTextField_Focus(self,instancia,focus):
            if focus:
                self.itens = [
                    '1',
                    '2',
                    '3',
                ]
                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.NivelLeituraAlunosProfissionalTextField_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def NivelLeituraAlunosProfissionalTextField_ItensClick(self, text_item):
        self.ids.NivelLeituraAlunosTextField.text = text_item

    def NivelEscritaAlunosProfissionalTextField_Focus(self,instancia,focus):
            if focus:
                self.itens = [
                    '1',
                    '2',
                    '3',
                ]
                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.NivelEscritaAlunosTextField_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def NivelEscritaAlunosTextField_ItensClick(self, text_item):
        self.ids.NivelEscritaAlunosTextField.text = text_item

    from kivy.clock import Clock

    def DataNascimentoAlunosTextField_Active(self, instancia):
        # Remove tudo que não for número
        puro = "".join(ch for ch in instancia.text if ch.isdigit())
        puro = puro[:8]  # Limita a 8 dígitos (DDMMAAAA)

        novo = ""
        for i, d in enumerate(puro):
            novo += d
            # Adiciona "/" após o dia e mês
            if i == 1 or i == 3:
                if len(puro) > i + 1:
                    novo += '/'

        # Atualiza o texto formatado
        if instancia.text != novo:
            instancia.text = novo
            Clock.schedule_once(lambda dt: instancia.do_cursor_movement('cursor_end'))

    def AdicionarAlunos_Click(self):
        try:
            print("IDs disponíveis:", self.ids.keys())
            print(self.ControleProfissional.CPF)
            self.AlunoControle.setCadastro(self)
            print("Aluno:", self.AlunoControle.getAluno())
            self.AlunoControle.Salvar()
            if self.manager:
                self.manager.current = "AlunosProfissional"
        except Exception as e:
            print("Erro ao adicionar aluno:", e)

class TelaAlunoEspecifico(MDScreen):
    RA = StringProperty("")
    NOME = StringProperty("")
    USUARIO = StringProperty("")
    ESCOLA = StringProperty("")
    DATANASCIMENTO = StringProperty("")
    GENERO = StringProperty("")
    TURMA = StringProperty("")
    PROFISSIONALRESPONSAVEL = StringProperty("")
    UF = StringProperty("")
    CIDADE = StringProperty("")
    DIAGNOSTICO = StringProperty("")
    OBSERVACOES = StringProperty("")
    NIVELDELEITURA = StringProperty("")
    NIVELDEESCRITA = StringProperty("")
    AlunoRA = None
    dialog = None  # variável para controlar o diálogo
    titulo = StringProperty("")
    nivel = StringProperty("")
    Aluno = None

    def on_pre_enter(self):
        # Pegar referência do aluno da tela anterior
        tela_carregamento = self.manager.get_screen("AlunosProfissional")
        self.AlunoRA = tela_carregamento.aluno_RA

        # Inicializar o controller e carregar os dados do aluno
        self.Aluno = AlunoController()
        self.Aluno.setAluno(self.AlunoRA)

        # Preencher os campos da tela com os dados do aluno
        self.RA = str(self.Aluno.RE) if self.Aluno.RE is not None else ""
        self.NOME = str(self.Aluno.Nome) if self.Aluno.Nome is not None else ""
        self.USUARIO = str(self.Aluno.Usuario) if self.Aluno.Usuario is not None else ""
        self.ESCOLA = str(self.Aluno.Escola) if self.Aluno.Escola is not None else ""
        if self.Aluno.DataNascimento:
            self.DATANASCIMENTO = self.Aluno.DataNascimento.strftime("%d/%m/%Y")
        else:
            self.DATANASCIMENTO = ""
        self.GENERO = str(self.Aluno.Genero) if self.Aluno.Genero is not None else ""
        self.TURMA = str(self.Aluno.Turma) if self.Aluno.Turma is not None else ""
        self.PROFISSIONALRESPONSAVEL = str(self.Aluno.ProfissionalResponsavel) if self.Aluno.ProfissionalResponsavel is not None else ""
        self.UF = str(self.Aluno.UF) if self.Aluno.UF is not None else ""
        self.CIDADE = str(self.Aluno.Cidade) if self.Aluno.Cidade is not None else ""
        self.DIAGNOSTICO = str(self.Aluno.Diagnostico) if self.Aluno.Diagnostico is not None else ""
        self.OBSERVACOES = str(self.Aluno.Observacao) if self.Aluno.Observacao is not None else ""
        self.NIVELDELEITURA = str(self.Aluno.NivelLeitura) if self.Aluno.NivelLeitura is not None else ""
        self.NIVELDEESCRITA = str(self.Aluno.NivelEscrita) if self.Aluno.NivelEscrita is not None else ""

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"

    def AbrirTelaJogoEspecifico(self, titulo):
        self.titulo = titulo
        # Fecha o diálogo anterior, se já estiver aberto
        if self.dialog:
            self.dialog.dismiss()

        # Layout vertical com espaçamento entre os níveis
        box_botoes = MDBoxLayout(
            orientation="vertical",
            spacing=dp(10),
            padding=dp(10),
            adaptive_height=True
        )

        # Cria 3 níveis (você pode aumentar esse número depois)
        for i in range(1, 4):
            card = MDCard(
                size_hint_y=None,
                height=dp(60),
                md_bg_color=(0.9, 0.9, 0.9, 1),  # cor do card
                radius=[15],
                padding=dp(10),
                ripple_behavior=True,  # animação ao clicar
            )

            # Texto centralizado
            label = MDLabel(
                text=f"[b]Nível {i}[/b]",
                halign="center",
                valign="center",
                markup=True,
            )

            card.add_widget(label)
            card.bind(on_release=partial(self.AbrirNivel, i))  # passa o número do nível
            box_botoes.add_widget(card)

        # Cria o diálogo com o título do jogo e os cards dentro
        self.dialog = MDDialog(
            title=self.titulo,
            type="custom",
            content_cls=box_botoes,
            size_hint=(0.8,None),
            auto_dismiss=True,
        )

        # Exibe o diálogo
        self.dialog.open()

    def AbrirNivel(self, nivel, *args):
        self.nivel = str(nivel)
        print(f"Abrindo informações do Nível {self.nivel}...")
        self.dialog.dismiss()
        if self.manager:
            self.manager.current = "EstatisticasJogos"

    def ExcluirAluno_Click(self):
        if self.dialog:
            self.dialog.dismiss()

        # Layout vertical com espaçamento entre os níveis
        box_botoes = MDBoxLayout(
            orientation="horizontal",
            spacing=dp(10),
            padding=dp(10),
            adaptive_height=True
        )

        Btn1 = MDRoundFlatButton(
            text="Cancelar",
            on_release=lambda x: self.dialog.dismiss(),
            md_bg_color=(0.8, 0.1, 0.1, 1),
            text_color=(1, 1, 1, 1),

        )

        Btn2 = MDRoundFlatButton(
            text="Excluir",
            on_release=lambda x: self.Excluir(),
            md_bg_color=(0.1, 0.6, 0.1, 1),
            text_color=(1, 1, 1, 1),
        )

        box_botoes.add_widget(Btn1)
        box_botoes.add_widget(Btn2)

        # Cria o diálogo com o título do jogo e os cards dentro
        self.dialog = MDDialog(
            title='Tem certeza que deseja excluir este aluno de sua lista?',
            type="custom",
            content_cls=box_botoes,
            size_hint=(0.8,None),
            auto_dismiss=True,
        )

        # Exibe o diálogo
        self.dialog.open()
    
    def Excluir(self):
        try:
            self.Aluno.ExcluirAluno(self.AlunoUsuario)
            if self.manager:
                self.dialog.dismiss()
                self.manager.current = "AlunosProfissional"
        except Exception as e:
            print(e)
    
    def AlterarAluno_Click(self):
        if self.manager:
            self.manager.current = "AlterarAlunoProfissional"

class TelaEstatisticasJogos(MDScreen):
    AlunoRA = None
    Jogo = StringProperty("")
    Nivel = StringProperty("")
    Profissional = None
    UsuarioProfissional = StringProperty("")
    ControleDados = None
    PONTUACAO = StringProperty("")
    PORCENTAGEM_COMPLETADA = StringProperty("")
    TEMPO_GASTO = StringProperty("")
    ACERTOS = StringProperty("")
    ERROS = StringProperty("")
    TENTATIVAS = StringProperty("")
    DATA_REGISTRO = StringProperty("")

    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("AlunoEspecifico")
        self.AlunoRA = tela_carregamento.AlunoRA
        self.Jogo = tela_carregamento.titulo
        self.Nivel = str(tela_carregamento.nivel)
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        self.Profissional = tela_carregamento.Profissional
        self.UsuarioProfissional = self.Profissional.Usuario
        self.ControleDados = DadosJogosController()
        self.PegarDados()


    def PegarDados(self):
        try:
            if self.ControleDados.setDadoJogo(f"ID_ALUNO = '{self.AlunoRA}' AND NOME_JOGO = '{self.Jogo}' AND ID_NIVEL = {self.Nivel} AND USUARIO_PROFISSIONAL = '{self.UsuarioProfissional}'"):
                self.PONTUACAO = str(self.ControleDados.PONTUACAO)
                self.PORCENTAGEM_COMPLETADA = str(self.ControleDados.PORCENTAGEM_COMPLETADA)
                self.TEMPO_GASTO = str(self.ControleDados.TEMPO_GASTO)
                self.ACERTOS = str(self.ControleDados.ACERTOS)
                self.ERROS = str(self.ControleDados.ERROS)
                self.TENTATIVAS = str(self.ControleDados.TENTATIVAS)
                self.DATA_REGISTRO = str(self.ControleDados.DATA_REGISTRO)
            else:
                self.PONTUACAO = 'Sem dados'
                self.PORCENTAGEM_COMPLETADA = 'Sem dados'
                self.TEMPO_GASTO = 'Sem dados'
                self.ACERTOS = 'Sem dados'
                self.ERROS = 'Sem dados'
                self.TENTATIVAS = 'Sem dados'
                self.DATA_REGISTRO = 'Sem dados'
        except Exception as e:
            print(e)

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "AlunoEspecifico"

class TelaAlterarAlunoProfissional(MDScreen):
    ControleProfissional = None
    AlunoControle = None
    Tela_especifico = None
    RA = StringProperty("")
    NOME = StringProperty("")
    USUARIO = StringProperty("")
    ESCOLA = StringProperty("")
    DATANASCIMENTO = StringProperty("")
    GENERO = StringProperty("")
    TURMA = StringProperty("")
    PROFISSIONALRESPONSAVEL = StringProperty("")
    UF = StringProperty("")
    CIDADE = StringProperty("")
    DIAGNOSTICO = StringProperty("")
    OBSERVACOES = StringProperty("")
    NIVELDELEITURA = StringProperty("")
    NIVELDEESCRITA = StringProperty("")


    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ControleProfissional = tela_carregamento.Profissional
        else:
            self.ControleProfissional = None
        self.Tela_especifico = self.manager.get_screen("AlunoEspecifico")
        self.AlunoControle = AlunoController()

        # Carregar dados do aluno específico
        self.RA = str(self.Tela_especifico.RA) if self.Tela_especifico.RA is not None else ""
        self.NOME = str(self.Tela_especifico.NOME) if self.Tela_especifico.NOME is not None else ""
        self.USUARIO = str(self.Tela_especifico.USUARIO) if self.Tela_especifico.USUARIO is not None else ""
        self.ESCOLA = str(self.Tela_especifico.ESCOLA) if self.Tela_especifico.ESCOLA is not None else ""
        self.DATANASCIMENTO = str(self.Tela_especifico.DATANASCIMENTO) if self.Tela_especifico.DATANASCIMENTO is not None else ""
        self.GENERO = str(self.Tela_especifico.GENERO) if self.Tela_especifico.GENERO is not None else ""
        self.TURMA = str(self.Tela_especifico.TURMA) if self.Tela_especifico.TURMA is not None else ""
        self.PROFISSIONALRESPONSAVEL = str(self.Tela_especifico.PROFISSIONALRESPONSAVEL) if self.Tela_especifico.PROFISSIONALRESPONSAVEL is not None else ""
        self.UF = str(self.Tela_especifico.UF) if self.Tela_especifico.UF is not None else ""
        self.CIDADE = str(self.Tela_especifico.CIDADE) if self.Tela_especifico.CIDADE is not None else ""
        self.DIAGNOSTICO = str(self.Tela_especifico.DIAGNOSTICO) if self.Tela_especifico.DIAGNOSTICO is not None else ""
        self.OBSERVACOES = str(self.Tela_especifico.OBSERVACOES) if self.Tela_especifico.OBSERVACOES is not None else ""
        self.NIVELDELEITURA = str(self.Tela_especifico.NIVELDELEITURA) if self.Tela_especifico.NIVELDELEITURA is not None else ""
        self.NIVELDEESCRITA = str(self.Tela_especifico.NIVELDEESCRITA) if self.Tela_especifico.NIVELDEESCRITA is not None else ""

        #Insere as informações nos TextFields
        self.ids.NomeAlunosTextField.text = self.NOME
        self.ids.UsuarioAlunosTextField.text = self.USUARIO
        self.ids.EscolaAlunosTextField.text = self.ESCOLA
        self.ids.DataNascimentoAlunosTextField.text = self.DATANASCIMENTO
        self.ids.GeneroAlunosTextField.text = self.GENERO
        self.ids.TurmaAlunosTextField.text = self.TURMA
        self.ids.UFAlunosTextField.text = self.UF
        self.ids.CidadeAlunosTextField.text = self.CIDADE
        self.ids.DiagnosticoAlunosTextField.text = self.DIAGNOSTICO
        self.ids.ObservacaoAlunosTextField.text = self.OBSERVACOES
        self.ids.NivelLeituraAlunosTextField.text = self.NIVELDELEITURA
        self.ids.NivelEscritaAlunosTextField.text = self.NIVELDEESCRITA


    def DataNascimentoAlunosTextField_Active(self, instancia):
            # Remove tudo que não for número
            puro = "".join(ch for ch in instancia.text if ch.isdigit())
            puro = puro[:8]  # Limita a 8 dígitos (DDMMAAAA)

            novo = ""
            for i, d in enumerate(puro):
                novo += d
                # Adiciona "/" após o dia e mês
                if i == 1 or i == 3:
                    if len(puro) > i + 1:
                        novo += '/'

            # Atualiza o texto formatado
            if instancia.text != novo:
                instancia.text = novo
                Clock.schedule_once(lambda dt: instancia.do_cursor_movement('cursor_end'))
    
    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"


    def UFAlunosProfissionaisTextField_Focus(self,instancia,focus):
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
                        "on_release": lambda x=f'{index}': self.UFAlunosProfissionais_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def UFAlunosProfissionais_ItensClick(self, text_item):
        self.ids.UFAlunosTextField.text = text_item

    def CidadeAlunosProfissionaisTextField_Focus(self, instancia, focus):
        if focus:
            Cidade = Cidades()
            try:
                itens = Cidade.get_cidades_por_uf(self.ids.UFAlunosTextField.text)

                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.CidadeAlunosProfissional_ItensClick(x)
                    } for index in itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            except Exception as e:
                print(e)
        else:
            print('erro')


    def CidadeAlunosProfissional_ItensClick(self, text_item):
        self.ids.CidadeAlunosTextField.text = text_item

    def EscolaAlunosProfissionalTextField_Focus(self, instancia, focus):
        if focus:
            Escola = Escolas()
            try:
                dados = Escola.Get(self.ids.UFAlunosTextField.text, self.ids.CidadeAlunosTextField.text)
                itens = [item["escola"] for item in dados if "escola" in item]
                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.EscolaAlunosProfissional_ItensClick(x)
                    } for index in itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            except:
                pass
        else:
            print('erro')

    def EscolaAlunosProfissional_ItensClick(self, text_item):
        self.ids.EscolaAlunosTextField.text = text_item

    def NivelLeituraAlunosProfissionalTextField_Focus(self,instancia,focus):
            if focus:
                self.itens = [
                    '1',
                    '2',
                    '3',
                ]
                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.NivelLeituraAlunosProfissionalTextField_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def NivelLeituraAlunosProfissionalTextField_ItensClick(self, text_item):
        self.ids.NivelLeituraAlunosTextField.text = text_item

    def NivelEscritaAlunosProfissionalTextField_Focus(self,instancia,focus):
            if focus:
                self.itens = [
                    '1',
                    '2',
                    '3',
                ]
                menu_items = [
                    {
                        "text": f'{index}',
                        "on_release": lambda x=f'{index}': self.NivelEscritaAlunosTextField_ItensClick(x)
                    } for index in self.itens
                ]

                MDDropdownMenu(caller=instancia, items=menu_items).open()
            else:
                print('erro')

    def NivelEscritaAlunosTextField_ItensClick(self, text_item):
        self.ids.NivelEscritaAlunosTextField.text = text_item

    def AlterarAlunos_Click(self):
        try:
            self.AlunoControle.setCadastro(self)
            self.AlunoControle.Salvar()
            if self.manager:
                self.manager.current = "AlunosProfissional"
        except Exception as e:
            print("Erro ao alterar aluno:", e)
    
class TelaAlbumEspecifico(MDScreen):
    ControlePerfil = None
    ControleFavoritos = None
    FeedAlbumEspecifico = None
    ControlePost = None
    ControleAlbuns = None
    Favoritos = None
    GridAlbuns = None
    IDs = None
    Resultado = None
    Nome = None
    Comentario = None

    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ControlePerfil = tela_carregamento.Profissional
        else:
            self.ControlePerfil = None
        self.FeedAlbumEspecifico = self.ids.FeedAlbumEspecifico

        self.Nome = self.manager.get_screen("FavoritosPerfilProfissional").Nome
        print("Nome do álbum:", self.Nome)

        self.ControleFavoritos = FavoritosController()
        self.ControlePost = PostController()
        self.ControleAlbuns = AlbumController()
        self.Favoritos = self.ControleFavoritos.setListaFavoritos(f"USUARIO = '{self.ControlePerfil.Usuario}' AND NOME_ALBUM = '{self.Nome}'")
        try:
            self.IDs = [item['PostID'] for item in self.Favoritos]
        except Exception as e:
            print(e)
            self.IDs = []
        self.Resultado = self.ControlePost.ListarPostPorID(self.IDs)
        self.Resultado = self.CarregarImagensPosts(self.Resultado)
        print("Favoritos:", self.Favoritos)
        print("IDs:", self.IDs)
        print(self.Resultado)
        self.Comentario = ComentarioController()
        self.ListarAlbuns()

            # Carrega imagens decodificando Base64 e associando pelo id do post
    def CarregarImagensPosts(self, posts):
        try:
            ListaPostsHelper = Posts()
            posts_no_banco = ListaPostsHelper.Get()  # pega todos os posts do banco

            # Cria um dicionário de imagens pelo id do post
            imagens_dict = {}
            for post_banco in posts_no_banco:
                imagem_b64 = post_banco.get('imagem', None)
                textura = None
                if imagem_b64 and imagem_b64 not in ("NULL", "null", ""):
                    try:
                        data = io.BytesIO(base64.b64decode(imagem_b64))
                        textura = CoreImage(data, ext='png').texture
                    except Exception as e:
                        print(f"Erro ao decodificar imagem do post {post_banco.get('id', '')}: {e}")
                imagens_dict[post_banco['id']] = textura

            # Atualiza os posts originais com a textura correta
            for post in posts:
                post['imagem_obj'] = imagens_dict.get(post.get('id'), None)

            return posts

        except Exception as e:
            print(f"Erro ao carregar imagens dos posts: {e}")
            return posts
        
        # Carrega imagens decodificando Base64 e associando pelo id do post
    def ListarAlbuns(self):
        self.FeedAlbumEspecifico.clear_widgets()
        try:
            if not self.Resultado:
                Label = MDLabel(
                    text="Nenhum favorito encontrado.",
                    halign="center",
                    valign="top",
                )

                self.FeedAlbumEspecifico.add_widget(Label)
                return
            for post in self.Resultado:
                box_post = MDBoxLayout(
                    orientation="vertical",
                    size_hint_y=None,
                    padding=dp(5),
                )

                card = MDCard(
                    size_hint_y=None,
                    padding=dp(10),
                    orientation="vertical",
                    spacing=dp(10)
                )

                # Cabeçalho
                box_cabecalho = MDBoxLayout(
                    orientation="horizontal",
                    size_hint_y=None,
                    height=dp(30),
                    spacing=dp(10)
                )

                usuario = MDLabel(
                    text=f"@{post.get('usuario', '')}",
                    font_size="16sp",
                    halign="left",
                    theme_text_color="Primary",
                    size_hint_x=0.7
                )
                usuario.bind(texture_size=usuario.setter('size'))

                btn_menu = MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    pos=(dp(0), dp(5)),
                    radius=[20, 20, 20, 20]  # <- evita ValueError
                )

                # Cria menu
                menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
                menu.items = [
                    {
                        "text": "Excluir",
                        "icon": "delete",
                        "on_release": lambda x=post: (menu.dismiss(), self.excluir_post(x))
                    }
                ]

                btn_menu.on_release = menu.open

                box_cabecalho.add_widget(usuario)
                box_cabecalho.add_widget(btn_menu)
                card.add_widget(box_cabecalho)

                # Imagem do post
                imagem_obj = post.get('imagem_obj', None)
                if imagem_obj:
                    imagem_widget = Image(
                        texture=imagem_obj,
                        size_hint_y=None,
                        height=dp(400),
                        allow_stretch=True,
                        keep_ratio=True
                    )
                    card.add_widget(imagem_widget)

                # Legenda
                legenda = MDLabel(
                    text=post.get('legenda', ''),
                    halign="left",
                    theme_text_color="Secondary",
                    size_hint_y=None
                )
                legenda.bind(texture_size=legenda.setter('size'))
                card.add_widget(legenda)

                # Rodapé
                box_rodape = MDBoxLayout(
                    orientation="horizontal",
                    size_hint_y=None,
                    height=dp(30),
                    spacing=dp(10)
                )

                Favoritar_button = MDIconButton(
                    icon="star",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    radius=[20, 20, 20, 20],  # <- evita ValueError
                    icon_color=(1, 0.843, 0, 1)
                )
                Favoritar_button.post_id = post.get("id")

                Favoritar_button.favoritado = False
                Favoritar_button.bind(on_release=self.on_release_buttonfavoritos)

                Comentarios_button = MDIconButton(
                    icon="comment-outline",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    radius=[20, 20, 20, 20]  # <- evita ValueError
                )
                Comentarios_button.post_id = post.get("id")
                Comentarios_button.bind(on_release=self.abrir_comentarios)

                box_rodape.add_widget(Favoritar_button)
                box_rodape.add_widget(Comentarios_button)
                card.add_widget(box_rodape)

                card.bind(minimum_height=card.setter('height'))
                box_post.add_widget(card)
                box_post.bind(minimum_height=box_post.setter('height'))
                self.FeedAlbumEspecifico.add_widget(box_post)
        except Exception as e:
            print(e)
            return

    def excluir_post(self, post):
        print(f"🗑️ Excluindo post de {post.get('usuario')}")

    def abrir_comentarios(self, instance):
        self.instanciacomentario = instance
        self.post_id = getattr(instance, "post_id", None)
        resultado = self.Comentario.setListaComentarios(f'IDPOST = {self.post_id}')
        # BoxLayout que vai conter tudo
        BoxComentarios = MDBoxLayout(
            orientation="vertical",
            padding = dp(10),
            spacing = dp(10),
            size_hint_y = None,
            height = dp(500),  # define altura do box
            md_bg_color = (1, 1, 1, 1)
        )
        if resultado:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(20),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))

            for comentario in resultado:
                Card = MDCard(
                    size_hint_y=None,
                    padding=dp(10),
                    orientation="vertical",
                    spacing=dp(5),
                    md_bg_color=(0.8, 0.8, 0.8, 1)
                )

                BoxCabecalho = MDBoxLayout(
                    orientation="horizontal",
                    padding=dp(0),
                    spacing=dp(20),
                    size_hint_y=None,
                    md_bg_color=(1, 1, 1, 1)
                )

                btn_menu = MDIconButton(
                    icon="dots-vertical",
                    size_hint=(None, None),
                    size=(dp(24), dp(24)),
                    pos=(dp(0), dp(0)),
                    radius=[20, 20, 20, 20]  # <- evita ValueError
                )

                btn_menu.theme_icon_color = "Custom"
                btn_menu.text_color  = (0, 0, 0, 0)

                BoxCabecalho.md_bg_color = (0.8, 0.8, 0.8, 1)
                BoxCabecalho.bind(minimum_height=BoxCabecalho.setter('height'))
                BoxCabecalho.add_widget(MDLabel(text=f"@{comentario['Usuario']}"))
                if comentario['Usuario'] == self.ProfissionalControle.Usuario:
                    btn_menu.text_color  = (0, 0, 0, 1)
                    menu = MDDropdownMenu(caller=btn_menu, width_mult=4)
                    menu.items = [
                        {
                            "text": "Excluir",
                            "icon": "delete",
                            "on_release": lambda x=comentario: (menu.dismiss(), self.ExcluirComentario(x))
                        }
                    ]
                    btn_menu.on_release = menu.open

                BoxCabecalho.add_widget(btn_menu)
                Card.add_widget(BoxCabecalho)
                TextoComentario = MDLabel(
                    text=comentario['Texto'],
                    size_hint_y = None
                )
                Card.add_widget(TextoComentario)

                Card.bind(minimum_height=Card.setter('height'))
                BoxComentario.add_widget(Card)
        else:
            BoxComentario = MDBoxLayout(
                orientation="vertical",
                padding=dp(10),
                spacing=dp(10),
                size_hint_y=None,
                md_bg_color=(1, 1, 1, 1)
            )
            BoxComentario.bind(minimum_height=BoxComentario.setter('height'))
            BoxComentario.add_widget(
                MDLabel(
                    text='Sem Comentários. Seja o Primeiro!',
                    halign="center",
                    valign="center",
                )
            )

        BoxPostarComentario = MDBoxLayout(
            orientation="horizontal",
            padding=dp(10),
            spacing=dp(10),
            size_hint_y=None,
            height=dp(80),  # define altura do box
            md_bg_color=(1, 1, 1, 1),
        )

        self.tf = TextInput(
            size_hint_x=0.8,
            cursor_color=(0, 0, 0, 1),
            foreground_color=(0, 0, 0, 1),
            multiline=True,
        )

        # limite de caracteres
        self.tf.max_chars = 500

        # evento que monitora a digitação
        self.tf.bind(text=self.limitar_texto)

        # Botão circular com seta
        btn_cima = MDFloatingActionButton(
            icon="arrow-up",
            md_bg_color=(1, 1, 1, 1),
            text_color=(0, 0, 0, 1),
        )

        btn_cima.bind(on_release=lambda _: self.on_release_Comentarios_button())
        BoxPostarComentario.add_widget(self.tf)
        BoxPostarComentario.add_widget(btn_cima)

        # ScrollView para permitir rolagem se necessário
        scroll = ScrollView(
            do_scroll_x=False, do_scroll_y=True,
            size_hint=(1, None),
            height=dp(400)
        )

        scroll.add_widget(BoxComentario)
        BoxComentarios.add_widget(scroll)
        BoxComentarios.add_widget(BoxPostarComentario)

        # Cria o Dialog
        self.dialog = MDDialog(
            title="Comentários",
            type="custom",
            content_cls=BoxComentarios,
            size_hint=(0.5, None),
            height=dp(180),  # altura do diálogo
        )

        # Abre o Dialog
        self.dialog.open()

    def limitar_texto(self, instance, value):
        if len(value) > instance.max_chars:
            instance.text = value[:instance.max_chars]

    def AtualizarComentarios(self, instance):
        if self.dialog:
            self.dialog.dismiss()
        self.abrir_comentarios(instance)

    def on_release_buttonfavoritos(self, instance):
        self.post_id = getattr(instance, "post_id", None)
        print(f"ID do post favoritado: {self.post_id}")
        self.ControleFavoritos.setNewFavorito(self)
        if not instance.favoritado:
            instance.icon = "star-outline"
            instance.icon_color = (0.5, 0.5, 0.5, 1)
            instance.favoritado = False
            self.ControleFavoritos.Desfavoritar()
            self.Favoritos = self.ControleFavoritos.setListaFavoritos(f"USUARIO = '{self.ControlePerfil.Usuario}' AND NOME_ALBUM = '{self.Nome}'")
            try:
                self.IDs = [item['PostID'] for item in self.Favoritos]
            except Exception as e:
                print(e)
                self.IDs = []
            self.Resultado = self.ControlePost.ListarPostPorID(self.IDs)
            self.Resultado = self.CarregarImagensPosts(self.Resultado)
            self.ListarAlbuns()
        else:
            instance.icon = "star"
            instance.icon_color = (1, 0.843, 0, 1)
            instance.favoritado = True
            self.ControleFavoritos.Favoritar()

    def on_release_Comentarios_button(self):
        try:
            self.Comentario.setNewComentario(self)
            self.Comentario.Comentar()
            self.AtualizarComentarios(self.instanciacomentario)
        except Exception as e:
            print(e)

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "FavoritosPerfilProfissional"

#----------------------------------Alunos----------------------------------#

class TelaLoginAluno(MDScreen):
    ControleLoginAluno = None
    Usuario = StringProperty("")
    RA = StringProperty("")

    def on_pre_enter(self, *args):
        self.ControleLoginAluno = LoginAlunoController()

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "Escolha"
    
    def Entrar(self):
        self.Usuario = self.ids.UsuarioTextField.text
        self.RA = self.ids.RATextField.text
        try:
            self.ControleLoginAluno.setLogin(self)
            if self.ControleLoginAluno.Sessao():
                if self.manager:
                    self.manager.current = "CarregamentoInicialAluno"
            else:
                print("Usuário ou RA incorretos.")
        except Exception as e:
            print("Erro ao realizar login:", e)

class TelaCarregamentoInicialAluno(MDScreen):
    InformacoesAluno = None
    ControleAluno = None

    def on_enter(self, *args):
        Tela_Login = self.manager.get_screen("LoginAluno")
        self.InformacoesAluno = [Tela_Login.Usuario, Tela_Login.RA]
        self.ControleAluno = AlunoController()
        print("Carregando dados do aluno:", self.InformacoesAluno)
        self.ControleAluno.setAluno(self.InformacoesAluno[1])
        if self.manager:
            self.manager.current = "InicialAluno"

class TelaInicialAluno(MDScreen):
    
    def JogosMDTextButton_Click(self):
        pass
    
    def PerfilMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"

import json
from pathlib import Path
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.app import App

class TelaPerfilAluno(MDScreen):
    def PerfilMDTextButton_Click(self):
        pass

    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InicialAluno"

    def ConquistasMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "Conquistas"

    def JogosCard_Click(self, jogo):
        if jogo == 1:
            self.manager.current = "JogoDosSeteErros"
        elif jogo == 2:
            self.manager.current = "OrganizeAsCores"
        elif jogo == 3:
            self.manager.current = "SilabaMix"
        elif jogo == 4:
            self.manager.current = "JogoDaMemoria"
        elif jogo == 5:
            self.manager.current = "JogoMemoriaDosCores"
        elif jogo == 6:
            self.manager.current = "JogoSomSilaba"

    # ---------------------------
    # 🔹 Função principal da trilha
    # ---------------------------
    from kivymd.uix.dialog import MDDialog
    from kivymd.uix.button import MDFillRoundFlatIconButton
    from pathlib import Path
    import json

    def JogoDaTrilha(self):
        """
        Controla a sequência de jogos do aluno e redireciona para o ponto certo.
        """
        try:
            # === Pega dados do aluno ===
            tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
            if not tela_carregamento or not tela_carregamento.ControleAluno:
                print("⚠️ Nenhum aluno logado.")
                return

            self.ControleAluno = tela_carregamento.ControleAluno
            re_aluno = str(self.ControleAluno.RE)

            # === Caminho de progresso individual ===
            caminho_dados = Path(f"dados_jogo_{re_aluno}.json")

            # === Se não existir, cria começando do início ===
            if not caminho_dados.exists():
                progresso = {
                    "re": re_aluno,
                    "jogo_atual": "sete_erros",
                    "nivel_atual": 1,
                    "fase_atual": 1
                }
                caminho_dados.write_text(json.dumps(progresso, indent=4))
            else:
                progresso = json.loads(caminho_dados.read_text())

            jogo = progresso["jogo_atual"]
            nivel = progresso["nivel_atual"]
            fase = progresso["fase_atual"]

            trilha = {
                "sete_erros": {"fases": 1, "niveis": 1, "proximo": "organize_cores", "tela": "JogoDosSeteErros"},
                "organize_cores": {"fases": 6, "niveis": 3, "proximo": "silaba_mix", "tela": "OrganizeAsCores"},
                "silaba_mix": {"fases": 24, "niveis": 3, "proximo": "memoria", "tela": "SilabaMix"},
                "memoria": {"fases": 6, "niveis": 3, "proximo": "memoria_cores", "tela": "JogoDaMemoria"},
                "memoria_cores": {"fases": 3, "niveis": 3, "proximo": "som_silaba", "tela": "JogoMemoriaDosCores"},
                "som_silaba": {"fases": 15, "niveis": 3, "proximo": None, "tela": "JogoSomSilaba"}
            }

            info = trilha.get(jogo)
            if not info:
                print("⚠️ Erro: jogo atual inválido.")
                return

            print(f"➡ Entrando no jogo: {jogo} | Nível {nivel} | Fase {fase}")

            # === Redireciona para o jogo correspondente ===
            if self.manager:
                tela_destino = info["tela"]
                self.manager.current = tela_destino

                # Define os IDs dentro da tela de jogo (caso existam)
                tela_jogo = self.manager.get_screen(tela_destino)
                if hasattr(tela_jogo, "id_fase"):
                    tela_jogo.id_fase = fase
                if hasattr(tela_jogo, "id_nivel"):
                    tela_jogo.id_nivel = nivel

        except Exception as e:
            print(f"⚠️ Erro em JogoDaTrilha: {e}")


    # ---------------------------
    # 🔹 Função de atualização de progresso
    # ---------------------------
    def atualizar_progresso(self):
        """
        Atualiza o progresso do jogador ao concluir uma fase.
        Mostra MDDialog se o jogador concluiu um nível ou jogo.
        """
        try:
            tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
            if not tela_carregamento or not tela_carregamento.ControleAluno:
                print("⚠️ Nenhum aluno logado para atualizar progresso.")
                return

            self.ControleAluno = tela_carregamento.ControleAluno
            re_aluno = str(self.ControleAluno.RE)
            caminho_dados = Path(f"dados_jogo_{re_aluno}.json")

            if not caminho_dados.exists():
                print("⚠️ Nenhum progresso encontrado, criando novo arquivo.")
                self.JogoDaTrilha()
                return

            progresso = json.loads(caminho_dados.read_text())

            trilha = {
                "sete_erros": {"fases": 1, "niveis": 1, "proximo": "organize_cores"},
                "organize_cores": {"fases": 6, "niveis": 3, "proximo": "silaba_mix"},
                "silaba_mix": {"fases": 24, "niveis": 3, "proximo": "memoria"},
                "memoria": {"fases": 6, "niveis": 3, "proximo": "memoria_cores"},
                "memoria_cores": {"fases": 3, "niveis": 3, "proximo": "som_silaba"},
                "som_silaba": {"fases": 15, "niveis": 3, "proximo": None}
            }

            jogo = progresso["jogo_atual"]
            nivel = progresso["nivel_atual"]
            fase = progresso["fase_atual"]
            info = trilha.get(jogo)

            if not info:
                print("⚠️ Erro ao atualizar progresso: jogo inválido.")
                return

            nivel_concluido = False
            jogo_concluido = False

            # Incrementa fase
            fase += 1
            if fase > info["fases"]:
                fase = 1
                nivel += 1
                nivel_concluido = True

                # Se terminou o último nível
                if nivel > info["niveis"]:
                    nivel = 1
                    jogo = info["proximo"]
                    jogo_concluido = True

            # Se acabou tudo
            if not jogo:
                self._mostrar_dialogo_final("🎉 Parabéns! Você concluiu todos os jogos!")
                caminho_dados.unlink(missing_ok=True)
                return

            progresso["jogo_atual"] = jogo
            progresso["nivel_atual"] = nivel
            progresso["fase_atual"] = fase
            caminho_dados.write_text(json.dumps(progresso, indent=4))

            print(f"✅ Progresso atualizado: {jogo} | Nível {nivel} | Fase {fase}")

            # Mostra diálogos conforme situação
            if jogo_concluido:
                self._mostrar_dialogo_final("🎮 Você concluiu este jogo! Continue para o próximo!")
            elif nivel_concluido:
                self._mostrar_dialogo_final(f"🏁 Parabéns! Você concluiu o nível {nivel - 1}!")

        except Exception as e:
            print(f"⚠️ Erro em atualizar_progresso: {e}")


    # ---------------------------
    # 🔹 Função auxiliar para exibir o diálogo final
    # ---------------------------
    def _mostrar_dialogo_final(self, texto):
        try:
            self.dialog_final = MDDialog(
                title="✨ Conquista!",
                text=texto,
                md_bg_color=(1, 1, 1, 0.8),
                radius=[20, 20, 20, 20],
                auto_dismiss=False,
                buttons=[
                    MDFillRoundFlatIconButton(
                        text="OK",
                        icon="check",
                        text_color="white",
                        md_bg_color=(0, 0.6, 0.1, 1),
                        on_release=self._fechar_dialogo_final
                    )
                ]
            )
            self.dialog_final.title_align = "center"
            self.dialog_final.open()
        except Exception as e:
            print(f"⚠️ Erro ao mostrar diálogo final: {e}")


    def _fechar_dialogo_final(self, *args):
        try:
            if hasattr(self, "dialog_final"):
                self.dialog_final.dismiss()
            if self.manager:
                self.manager.current = "PerfilAluno"
        except Exception:
            pass

class TelaConquistas(MDScreen):
    porcentagem = 0

    def on_pre_enter(self, *args):
        self.controledadosjogos = DadosJogosController()

        pass

    def PerfilMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"
    
    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InicialAluno"

    def ConquistasMDTextButton_Click(self):
        pass

    def carousel_prev(self):
        try:
            self.ids.carousel.load_previous()
        except Exception as e:
            print("Erro ao ir para slide anterior:", e)

    def carousel_next(self):
        try:
            self.ids.carousel.load_next()
        except Exception as e:
            print("Erro ao ir para próximo slide:", e)

from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivy.properties import NumericProperty
import time

class TelaJogoDosSeteErros(MDScreen):
    # === Propriedades do jogo ===
    erros_encontrados = NumericProperty(0)
    total_erros = 7

    # === Dados de desempenho ===
    id_fase = NumericProperty(1)
    id_nivel = NumericProperty(1)
    pontuacao = NumericProperty(0)
    porcentagem_completada = NumericProperty(0)
    tempo_inicial = NumericProperty(0)
    tempo_gasto = NumericProperty(0)
    acertos = NumericProperty(0)
    erros = NumericProperty(0)
    tentativas = NumericProperty(0)

    # === Ao entrar na tela ===
    def on_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
        if tela_carregamento.ControleAluno:
            self.ControleAluno = tela_carregamento.ControleAluno
        else:
            self.ControleAluno = None

        self.VoltarAoInicio()

        # Diálogo inicial
        self.dialog_inicial = MDDialog(
            md_bg_color=(1, 1, 1, 0.7),
            title="🕵️‍♂️ Jogo dos 7 Erros",
            text="Encontre os 7 erros entre as imagens! Deseja começar o jogo?",
            type="custom",
            radius=[20, 20, 20, 20],
            auto_dismiss=False,
            buttons=[
                MDFillRoundFlatIconButton(
                    icon="close",
                    text="Sair",
                    text_color="white",
                    md_bg_color=(0.7, 0, 0, 1),
                    on_release=self.SairDoJogo
                ),
                MDFillRoundFlatIconButton(
                    icon="play",
                    text="Começar",
                    text_color="white",
                    md_bg_color=(0, 0.6, 0.1, 1),
                    on_release=self.StartJogo
                ),
            ],
        )
        self.dialog_inicial.title_align = "center"
        self.dialog_inicial.open()

    # === Reinicia os botões ===
    def VoltarAoInicio(self):
        for i in range(1, 8):
            btn = self.ids.get(f"btn{i}")
            if btn:
                btn.text_color = (0.6, 1, 0.6, 0)
                btn.disabled = False

    # === Inicia o jogo ===
    def StartJogo(self, *args):
        try:
            self.dialog_inicial.dismiss()
        except Exception:
            pass

        self.erros_encontrados = 0
        self.acertos = 0
        self.erros = 0
        self.tentativas += 1
        self.pontuacao = 0
        self.tempo_inicial = time.time()

        print("🎮 Jogo iniciado! Boa sorte!")

    # === Sai do jogo e volta para o perfil ===
    def SairDoJogo(self, *args):
        try:
            self.dialog_inicial.dismiss()
            if self.manager:
                self.manager.current = "PerfilAluno"
        except Exception:
            pass

    # === Clique em botão de erro ===
    def botao_clicado(self, valor, botao):
        if not botao.disabled:
            botao.disabled = True
            self.erros_encontrados += 1
            self.acertos += 1
            self.pontuacao += 1
            self.porcentagem_completada = (self.acertos / self.total_erros) * 100

            print(f"✅ Botão {valor} clicado - ({self.erros_encontrados}/{self.total_erros})")

            if self.erros_encontrados >= self.total_erros:
                self.tempo_gasto = round(time.time() - self.tempo_inicial, 2)
                self.AbrirDialogoVitoria()
        else:
            print(f"⚠️ Botão {valor} já clicado anteriormente.")

    # === Diálogo de vitória ===
    def AbrirDialogoVitoria(self):
        self.dialog_vitoria = MDDialog(
            md_bg_color=(1, 1, 1, 0.7),
            title="🎉 Parabéns!",
            text="Você encontrou todos os 7 erros! Deseja jogar novamente?",
            type="custom",
            radius=[20, 20, 20, 20],
            auto_dismiss=False,
            buttons=[
                MDFillRoundFlatIconButton(
                    icon="close",
                    text="Sair",
                    text_color="white",
                    md_bg_color=(0.7, 0, 0, 1),
                    on_release=self._sair_dialog_vitoria
                ),
                MDFillRoundFlatIconButton(
                    icon="replay",
                    text="Reiniciar",
                    text_color="white",
                    md_bg_color=(0, 0.6, 0.1, 1),
                    on_release=self._reiniciar_dialog_vitoria
                ),
            ],
        )
        self.dialog_vitoria.title_align = "center"

        # === Coleta e exibe os dados ===
        dados_jogo = {
            "ID_FASE": self.id_fase,
            "ID_NIVEL": self.id_nivel,
            "PONTUACAO": self.pontuacao,
            "PORCENTAGEM_COMPLETADA": self.porcentagem_completada,
            "TEMPO_GASTO": self.tempo_gasto,
            "ACERTOS": self.acertos,
            "ERROS": self.total_erros - self.acertos,
            "TENTATIVAS": self.tentativas
        }

        print("\n📊 DADOS COLETADOS:")
        for k, v in dados_jogo.items():
            print(f"{k}: {v}")

        # === Salva e atualiza progresso ===
        self.salvar_dados(dados_jogo)
        self.dialog_vitoria.open()

    # === Fecha e volta ao perfil ===
    def _sair_dialog_vitoria(self, *args):
        try:
            self.atualizar_progresso_aluno()
            self.dialog_vitoria.dismiss()
            if self.manager:
                self.manager.current = "PerfilAluno"
        except Exception:
            pass

    # === Reinicia o jogo ===
    def _reiniciar_dialog_vitoria(self, *args):
        try:
            self.VoltarAoInicio()
            self.dialog_vitoria.dismiss()
        except Exception:
            pass

        self.erros_encontrados = 0
        self.pontuacao = 0
        self.acertos = 0
        self.erros = 0
        self.porcentagem_completada = 0
        print("🔄 Jogo reiniciado!")

    # === Botão de voltar ===
    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"

    # === Salvar dados em arquivo JSON ===
    def salvar_dados(self, dados):
        try:
            DadosJogosControle = DadosJogosController()
            Dados = []

            # Garantir que o controle do aluno está presente
            if not hasattr(self, "ControleAluno") or not self.ControleAluno:
                tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
                self.ControleAluno = tela_carregamento.ControleAluno

            Dados.append(self.ControleAluno.RE)
            Dados.append(self.ControleAluno.ProfissionalResponsavel)
            Dados.append("sete erros")

            for k, v in dados.items():
                Dados.append(v)

            DadosJogosControle.setNewDadoJogo(Dados)
            DadosJogosControle.SalvarDado()
            print("💾 Dados salvos com sucesso!")

        except Exception as e:
            print(f"⚠️ Erro ao salvar dados: {e}")

    # === Atualiza progresso no perfil ===
    def atualizar_progresso_aluno(self):
        try:
            tela_perfil = self.manager.get_screen("PerfilAluno")
            if hasattr(tela_perfil, "atualizar_progresso"):
                tela_perfil.atualizar_progresso()
                print("📈 Progresso atualizado com sucesso!")
            else:
                print("⚠️ TelaPerfilAluno não possui método atualizar_progresso().")
        except Exception as e:
            print(f"⚠️ Erro ao atualizar progresso: {e}")

COLOR_MAP = {
    "vermelho": (1, 0, 0, 1),
    "azul": (0, 0.5, 1, 1),
    "verde": (0, 1, 0, 1),
    "amarelo": (1, 1, 0, 1),
    "roxo": (0.6, 0, 0.8, 1),
    "laranja": (1, 0.5, 0, 1),
    "rosa": (1, 0.3, 0.6, 1),
    "ciano": (0, 1, 1, 1),
    "marrom": (0.6, 0.3, 0.1, 1),
}

class TelaOrganizeAsCores(MDScreen):

    
    card_selecionado = None
    fase_atual = NumericProperty(1)

    # === Dados de desempenho ===
    id_fase = NumericProperty(1)
    id_nivel = NumericProperty(1)
    pontuacao = NumericProperty(0)
    porcentagem_completada = NumericProperty(0)
    tempo_inicial = NumericProperty(0)
    tempo_gasto = NumericProperty(0)
    acertos = NumericProperty(0)
    erros = NumericProperty(0)
    tentativas = NumericProperty(0)

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"

    def on_enter(self, *args):

        tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
        if tela_carregamento.ControleAluno:
            self.ControleAluno = tela_carregamento.ControleAluno
        else:
            self.ControleAluno = None

        # === Diálogo inicial ===
        self.dialog_inicial = MDDialog(
            md_bg_color=(1, 1, 1, 0.7),
            title="🎨 Organize as Cores",
            text="Deseja iniciar o jogo?",
            type="custom",
            radius=[20, 20, 20, 20],
            auto_dismiss=False,
            buttons=[
                MDFillRoundFlatIconButton(
                    icon="close",
                    text="Sair",
                    text_color="white",
                    md_bg_color=(0.7, 0, 0, 1),
                    on_release=self.SairDoJogo
                ),
                MDFillRoundFlatIconButton(
                    icon="play",
                    text="Jogar",
                    text_color="white",
                    md_bg_color=(0, 0.6, 0.1, 1),
                    on_release=self.StartJogo
                ),
            ],
        )
        self.dialog_inicial.title_align = "center"
        self.dialog_inicial.open()

    # === Início do jogo ===
    def StartJogo(self, *args):
        try:
            self.dialog_inicial.dismiss()
        except Exception:
            pass

        # Reinicia dados da fase
        self.acertos = 0
        self.erros = 0
        self.pontuacao = 0
        self.porcentagem_completada = 0
        self.tentativas += 1
        self.tempo_inicial = time.time()

        self.Desenhar()

    def SairDoJogo(self, *args):
        try:
            self.dialog_inicial.dismiss()
        except Exception:
            pass
        App.get_running_app().stop()

    # === Desenha a fase ===
    def Desenhar(self):
        self.ids.JogoOrganizarCores.clear_widgets()

        # Configurações por fase
        if self.fase_atual <= 2:
            num_colunas = 3
            slots_por_coluna = 2
        elif self.fase_atual <= 4:
            num_colunas = 4
            slots_por_coluna = 3
        else:
            num_colunas = 5
            slots_por_coluna = 4

        CardFundo = MDCard(
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            radius=[20, 20, 20, 20],
            md_bg_color=(0.95, 0.95, 0.95, 0.3),
            padding=dp(10),
        )

        cores_disponiveis = list(COLOR_MAP.values())
        random.shuffle(cores_disponiveis)
        indice_branco = random.randint(0, num_colunas - 1)

        CorLista = []
        SubCardsPorColuna = []

        for i in range(num_colunas):
            if i == indice_branco:
                cor_rgba = (1, 1, 1, 1)
            else:
                cor_rgba = cores_disponiveis.pop()

            CorLista.append(cor_rgba)

            if i == 0:
                radius = [15, 0, 0, 15]
            elif i == num_colunas - 1:
                radius = [0, 15, 15, 0]
            else:
                radius = [0, 0, 0, 0]

            BoxCor = MDBoxLayout(
                orientation='vertical',
                size_hint=(1 / num_colunas, 1),
                spacing=dp(8),
            )

            FundoCor = MDCard(
                radius=radius,
                md_bg_color=cor_rgba,
                size_hint=(1, 1),
                elevation=0,
            )

            linha_lugares = MDBoxLayout(
                orientation='horizontal',
                spacing=dp(8),
                padding=dp(6),
                size_hint=(1, 1),
            )

            sub_cards = []
            for _ in range(slots_por_coluna):
                BoxLugares = MDCard(
                    size_hint=(1 / slots_por_coluna, 1),
                    radius=[12, 12, 12, 12],
                    md_bg_color=(0, 0, 0, 0.12),
                    elevation=-5,
                )
                BoxLugares.bind(on_release=self.ClickLugar)
                linha_lugares.add_widget(BoxLugares)
                sub_cards.append(BoxLugares)

            FundoCor.add_widget(linha_lugares)
            BoxCor.add_widget(FundoCor)
            SubCardsPorColuna.append(sub_cards)
            CardFundo.add_widget(BoxCor)

        # === Cria os cards móveis ===
        objetos_para_posicionar = []
        for idx_col, cor_rgba in enumerate(CorLista):
            if cor_rgba == (1, 1, 1, 1):
                continue

            cor_escura = tuple(max(c - 0.2, 0) for c in cor_rgba[:3]) + (1,)

            for _ in range(slots_por_coluna):
                obj = MDCard(
                    size_hint=(1, 1),
                    radius=[10, 10, 10, 10],
                    md_bg_color=cor_escura,
                    elevation=3,
                )
                obj.col_origem = idx_col
                obj.bind(on_release=self.ClickCard)
                objetos_para_posicionar.append(obj)

        # === Posicionamento inicial ===
        for obj in objetos_para_posicionar:
            possiveis_cols = [i for i in range(len(SubCardsPorColuna)) if i != obj.col_origem]
            random.shuffle(possiveis_cols)
            colocado = False
            for col_dest in possiveis_cols:
                subcards_livres = [s for s in SubCardsPorColuna[col_dest] if len(s.children) == 0]
                if subcards_livres:
                    random.choice(subcards_livres).add_widget(obj)
                    colocado = True
                    break
            if not colocado:
                random.choice(random.choice(SubCardsPorColuna)).add_widget(obj)

        self.CorLista = CorLista
        self.SubCardsPorColuna = SubCardsPorColuna
        self.ids.JogoOrganizarCores.add_widget(CardFundo)

    # === Clique no card ===
    def ClickCard(self, card):
        if self.card_selecionado is None:
            self.card_selecionado = card
            Animation(size_hint=(1.15, 1.15), duration=0.12, t="out_back").start(card)
            return

        if self.card_selecionado is card:
            Animation(size_hint=(1, 1), duration=0.12, t="out_back").start(card)
            self.card_selecionado = None
            return

        Animation(size_hint=(1, 1), duration=0.12).start(self.card_selecionado)
        self.card_selecionado = card
        Animation(size_hint=(1.15, 1.15), duration=0.12, t="out_back").start(card)

    # === Clique em local de destino ===
    def ClickLugar(self, lugar):
        if self.card_selecionado is None:
            return

        if len(lugar.children) == 0:
            card = self.card_selecionado
            if card.parent:
                card.parent.remove_widget(card)
            lugar.add_widget(card)
            Animation(size_hint=(1, 1), duration=0.18, t="out_back").start(card)

        if self.card_selecionado:
            Animation(size_hint=(1, 1), duration=0.12).start(self.card_selecionado)
        self.card_selecionado = None

        self.VerificarAcerto()

    # === Verifica acerto da fase ===
    def VerificarAcerto(self):
        todas_certas = True
        total = 0
        certos = 0

        for i, subcards in enumerate(self.SubCardsPorColuna):
            cor_coluna = self.CorLista[i]
            if cor_coluna == (1, 1, 1, 1):
                continue

            cor_esperada = tuple(max(c - 0.2, 0) for c in cor_coluna[:3])

            for lugar in subcards:
                total += 1
                if not lugar.children:
                    todas_certas = False
                    continue

                card = lugar.children[0]
                cor_card = card.md_bg_color[:3]
                if all(abs(c1 - c2) < 0.15 for c1, c2 in zip(cor_card, cor_esperada)):
                    certos += 1
                else:
                    todas_certas = False

        self.acertos = certos
        self.erros = total - certos
        self.pontuacao = certos
        self.porcentagem_completada = (certos / total) * 100 if total else 0

        if todas_certas:
            self.tempo_gasto = round(time.time() - self.tempo_inicial, 2)

            # === Coleta dados ===
            dados_jogo = {
                "ID_FASE": self.fase_atual,
                "ID_NIVEL": self.id_nivel,
                "PONTUACAO": self.pontuacao,
                "PORCENTAGEM_COMPLETADA": self.porcentagem_completada,
                "TEMPO_GASTO": self.tempo_gasto,
                "ACERTOS": self.acertos,
                "ERROS": self.erros,
                "TENTATIVAS": self.tentativas
            }

            print("\n📊 DADOS COLETADOS (Organize as Cores):")
            for k, v in dados_jogo.items():
                print(f"{k}: {v}")

            self.salvar_dados(dados_jogo)

            # === Diálogo de acerto ===
            self.dialog_acerto = MDDialog(
                md_bg_color=(1, 1, 1, 0.7),
                title="🎉 Parabéns!",
                text=f"Fase {self.fase_atual} completa! Deseja continuar?",
                type="custom",
                radius=[20, 20, 20, 20],
                auto_dismiss=False,
                buttons=[
                    MDFillRoundFlatIconButton(
                        icon="close",
                        text="Sair",
                        text_color="white",
                        md_bg_color=(0.7, 0, 0, 1),
                        on_release=self._sair_dialog_acerto
                    ),
                    MDFillRoundFlatIconButton(
                        icon="arrow-right",
                        text="Próxima",
                        text_color="white",
                        md_bg_color=(0, 0.6, 0.1, 1),
                        on_release=self._proxima_dialog_acerto
                    ),
                ],
            )
            self.dialog_acerto.title_align = "center"
            self.dialog_acerto.open()

    def _sair_dialog_acerto(self, *args):
        try:
            self.dialog_acerto.dismiss()
        except Exception:
            pass
        self.Voltar_Click()

    def _proxima_dialog_acerto(self, *args):
        try:
            self.dialog_acerto.dismiss()
        except Exception:
            pass
        self.ProximaFase()

    def ProximaFase(self):
        if self.fase_atual < 6:
            self.fase_atual += 1
            print(f"➡️ Indo para a fase {self.fase_atual}")
            self.tela_trila = self.manager.get_screen("PerfilAluno")
            self.tela_trila.atualizar_progresso()
            self.StartJogo()
        else:
            final = MDDialog(
                md_bg_color=(1, 1, 1, 0.7),
                title="🏁 Parabéns!",
                text="Você concluiu todas as fases!",
                size_hint=(0.8, None),
                radius=[20, 20, 20, 20],
                buttons=[MDFlatButton(text="OK", on_release=lambda *a: final.dismiss())],
            )
            final.open()

    # === Salvamento dos dados ===
    def salvar_dados(self, dados):
        Dados = []
        DadosJogosControle = DadosJogosController()
        self.ControleAluno
        Dados.append(self.ControleAluno.RE)
        Dados.append(self.ControleAluno.ProfissionalResponsavel)
        Dados.append('organizar cores')
        for k, v in dados.items():
            Dados.append(v)
        DadosJogosControle.setNewDadoJogo(Dados)
        DadosJogosControle.SalvarDado()

class TelaSilabaMix(MDScreen):

    # ========================================================
    # BOTÃO VOLTAR
    # ========================================================
    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"

    # ========================================================
    # ENTRADA NA TELA
    # ========================================================
    def on_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
        if tela_carregamento.ControleAluno:
            self.ControleAluno = tela_carregamento.ControleAluno
        else:
            self.ControleAluno = None

        # Controlador de dados
        self.controller_dados = DadosJogosController()

        # Variáveis principais do jogo
        self.jogo_nome = "silabamix"
        self.id_fase = 1
        self.id_nivel = 1
        self.pontuacao = 0
        self.acertos = 0
        self.erros = 0
        self.tentativas = 0
        self.porcentagem_completada = 0
        self.tempo_gasto = 0
        self.inicio_tempo = 0
        self.fim_tempo = 0

        # Lista de fases (mantida idêntica)
        self.fases = [
            # Nível 1
            {"palavra": "GATO", "silabas": ["GA", "TO"], "imagem": "Imagem1.png"},
            {"palavra": "BOLA", "silabas": ["BO", "LA"], "imagem": "Imagem2.png"},
            {"palavra": "CASA", "silabas": ["CA", "SA"], "imagem": "Imagem3.png"},
            {"palavra": "MALA", "silabas": ["MA", "LA"], "imagem": "Imagem4.png"},
            {"palavra": "MESA", "silabas": ["ME", "SA"], "imagem": "Imagem5.png"},
            {"palavra": "DADO", "silabas": ["DA", "DO"], "imagem": "Imagem6.png"},
            {"palavra": "FOCA", "silabas": ["FO", "CA"], "imagem": "Imagem7.png"},
            {"palavra": "RISO", "silabas": ["RI", "SO"], "imagem": "Imagem8.png"},

            # Nível 2
            {"palavra": "PIPOCA", "silabas": ["PI", "PO", "CA"], "imagem": "Imagem9.png"},
            {"palavra": "BONECA", "silabas": ["BO", "NE", "CA"], "imagem": "Imagem10.png"},
            {"palavra": "BANANA", "silabas": ["BA", "NA", "NA"], "imagem": "Imagem11.png"},
            {"palavra": "SORVETE", "silabas": ["SOR", "VE", "TE"], "imagem": "Imagem12.png"},
            {"palavra": "JANELA", "silabas": ["JA", "NE", "LA"], "imagem": "Imagem13.png"},
            {"palavra": "MOCHILA", "silabas": ["MO", "CHI", "LA"], "imagem": "Imagem14.png"},
            {"palavra": "ESCOLA", "silabas": ["ES", "CO", "LA"], "imagem": "Imagem15.png"},
            {"palavra": "CORAÇÃO", "silabas": ["CO", "RA", "ÇÃO"], "imagem": "Imagem16.png"},

            # Nível 3
            {"palavra": "CHOCOLATE", "silabas": ["CHO", "CO", "LA", "TE"], "imagem": "Imagem17.png"},
            {"palavra": "TELEFONE", "silabas": ["TE", "LE", "FO", "NE"], "imagem": "Imagem18.png"},
            {"palavra": "BORBOLETA", "silabas": ["BOR", "BO", "LE", "TA"], "imagem": "Imagem19.png"},
            {"palavra": "TELEVISÃO", "silabas": ["TE", "LE", "VI", "SÃO"], "imagem": "Imagem20.png"},
            {"palavra": "ELEFANTE", "silabas": ["E", "LE", "FAN", "TE"], "imagem": "Imagem21.png"},
            {"palavra": "ABACAXI", "silabas": ["A", "BA", "CA", "XI"], "imagem": "Imagem22.png"},
            {"palavra": "BICICLETA", "silabas": ["BI", "CI", "CLE", "TA"], "imagem": "Imagem23.png"},
            {"palavra": "ESTUDANTE", "silabas": ["ES", "TU", "DAN", "TE"], "imagem": "Imagem24.png"},
        ]

        self.fase_atual = 0
        self.silabas_escolhidas = []

        # ==== Diálogo inicial ====
        self.dialog_inicial = MDDialog(
            md_bg_color=(0, 0, 0, 0.7),
            title="🎯 Bem-vindo ao jogo SílabaMix!",
            type="custom",
            radius=[25, 25, 25, 25],
            auto_dismiss=False,
            buttons=[
                MDFillRoundFlatIconButton(
                    icon="close",
                    text="Sair",
                    text_color="white",
                    md_bg_color=(0, 0.5, 0, 1),
                    on_release=self.SairDoJogo
                ),
                MDFillRoundFlatIconButton(
                    icon="play",
                    text="Jogar",
                    text_color="white",
                    md_bg_color=(0, 0.6, 0.1, 1),
                    on_release=self.StartJogo
                ),
            ],
        )
        self.dialog_inicial.title_align = "center"
        self.dialog_inicial.open()

    # ========================================================
    # CONTROLE DE JOGO
    # ========================================================
    def StartJogo(self, *args):
        self.dialog_inicial.dismiss()
        self.inicio_tempo = time.time()
        self.CarregarFase(self.fase_atual)

    def SairDoJogo(self, *args):
        App.get_running_app().stop()

    # ========================================================
    # CARREGAMENTO DE FASE
    # ========================================================
    def CarregarFase(self, index):
        self.ids.JogoSilabaMiix.clear_widgets()
        self.silabas_escolhidas = []

        fase = self.fases[index]
        palavra = fase["palavra"]
        silabas = fase["silabas"]
        imagem_fase = fase["imagem"]

        silabas_embaralhadas = silabas.copy()
        while silabas_embaralhadas == silabas:
            random.shuffle(silabas_embaralhadas)

        BoxJogo = MDBoxLayout(orientation="vertical", padding=dp(25), spacing=dp(25))
        self.CardPrincipal = MDCard(
            size_hint=(1, 1),
            md_bg_color=(0.1, 0.4, 0.25, 1),
            radius=[35],
            elevation=15,
            orientation="vertical",
            padding=dp(20),
            spacing=dp(20),
        )

        BoxInteracao = MDBoxLayout(orientation="horizontal", spacing=dp(40), size_hint_y=0.7)
        imagem = Image(source=f"Imagens/SilabaMix/{imagem_fase}",
                       size_hint=(0.5, 0.7),
                       allow_stretch=True, keep_ratio=True)

        self.BoxCartas = MDBoxLayout(orientation="horizontal",
                                     spacing=dp(25),
                                     size_hint=(0.5, 1),
                                     padding=dp(10),
                                     pos_hint={"center_y": 0.5})

        for i, silaba in enumerate(silabas_embaralhadas):
            card = MDCard(size_hint=(0.45, 0.6),
                          md_bg_color=(1, 1, 1, 1),
                          radius=[25],
                          elevation=5,
                          orientation="vertical",
                          opacity=0)
            card.texto = silaba
            card.pos_original = i
            card.on_release = lambda c=card: self.ClickCard(c)

            with card.canvas.after:
                Color(0, 0, 0, 1)
                card.borda = Line(rounded_rectangle=(card.x, card.y, card.width, card.height, 25), width=2)
            card.bind(pos=self.AtualizarBorda, size=self.AtualizarBorda)

            card.add_widget(MDLabel(text=silaba, halign="center",
                                    theme_text_color="Custom",
                                    text_color=(0, 0, 0, 1),
                                    font_style="H3"))
            self.BoxCartas.add_widget(card)

            anim = Animation(opacity=1, elevation=10, duration=0.45, t="out_back")
            Clock.schedule_once(lambda dt, a=anim, c=card: a.start(c), 0.12 * i)

        BoxInteracao.add_widget(imagem)
        BoxInteracao.add_widget(self.BoxCartas)

        BoxResposta = MDBoxLayout(orientation="vertical", padding=dp(10), spacing=dp(10), size_hint_y=0.45)
        self.CardResposta = MDCard(size_hint=(1, 1), md_bg_color=(1, 1, 1, 0.95),
                                   radius=[30], elevation=12, orientation="vertical")

        self.LabelInstrucao = MDLabel(text="Monte a palavra correta!",
                                      halign="center",
                                      theme_text_color="Custom",
                                      text_color=(0, 0, 0, 1),
                                      font_style="H5",
                                      size_hint_y=None,
                                      height=dp(40))

        self.BoxPalavra = BoxLayout(orientation="horizontal", spacing=dp(10), padding=dp(10))
        self.CardResposta.add_widget(self.LabelInstrucao)
        self.CardResposta.add_widget(self.BoxPalavra)
        BoxResposta.add_widget(self.CardResposta)

        self.CardPrincipal.add_widget(BoxInteracao)
        self.CardPrincipal.add_widget(BoxResposta)
        BoxJogo.add_widget(self.CardPrincipal)
        self.ids.JogoSilabaMiix.add_widget(BoxJogo)

        self.palavra_correta = palavra.upper()

    # ========================================================
    # MOVIMENTO DAS CARTAS
    # ========================================================
    def ClickCard(self, card):
        self.tentativas += 1
        if card.parent == self.BoxCartas:
            self.BoxCartas.remove_widget(card)
            self.BoxPalavra.add_widget(card)
            self.silabas_escolhidas.append(card.texto)
        elif card.parent == self.BoxPalavra:
            self.BoxPalavra.remove_widget(card)
            self.silabas_escolhidas.remove(card.texto)
            children = list(self.BoxCartas.children)
            insert_index = len(children) - card.pos_original
            self.BoxCartas.add_widget(card, index=max(0, insert_index))

        Animation(opacity=1, size_hint=(0.45, 0.6), duration=0.3, t="out_cubic").start(card)
        self.VerificarPalavra()

    # ========================================================
    # VERIFICAÇÃO
    # ========================================================
    def VerificarPalavra(self):
        palavra_formada = "".join(self.silabas_escolhidas)
        if palavra_formada.upper() == self.palavra_correta:
            self.LabelInstrucao.text = "✅ Parabéns! Palavra correta!"
            self.LabelInstrucao.text_color = (0, 0.6, 0, 1)
            self.acertos += 1
            self.pontuacao += 10

            self.fim_tempo = time.time()
            self.tempo_gasto = round(self.fim_tempo - self.inicio_tempo, 2)
            self.porcentagem_completada = round((self.fase_atual + 1) / len(self.fases) * 100, 2)

            dados_jogo = {
                "ID_FASE": self.fase_atual,
                "ID_NIVEL": self.id_nivel,
                "PONTUACAO": self.pontuacao,
                "PORCENTAGEM_COMPLETADA": self.porcentagem_completada,
                "TEMPO_GASTO": self.tempo_gasto,
                "ACERTOS": self.acertos,
                "ERROS": self.erros,
                "TENTATIVAS": self.tentativas
            }

            print(f"\n📊 DADOS COLETADOS ({self.jogo_nome})")
            print(json.dumps(dados_jogo, indent=4, ensure_ascii=False))

            self.salvar_dados(dados_jogo)

            self.dialog_acerto = MDDialog(
                md_bg_color=(0, 0, 0, 0.7),
                title="🎉 Muito bem!",
                text="Você acertou! Deseja continuar jogando?",
                type="custom",
                radius=[25, 25, 25, 25],
                auto_dismiss=False,
                buttons=[
                    MDFillRoundFlatIconButton(
                        icon="close",
                        text="Sair",
                        text_color="white",
                        md_bg_color=(0, 0.5, 0, 1),
                        on_release=self.SairDoJogo
                    ),
                    MDFillRoundFlatIconButton(
                        icon="arrow-right",
                        text="Próxima",
                        text_color="white",
                        md_bg_color=(0, 0.6, 0.1, 1),
                        on_release=self.ProximaFase
                    ),
                ],
            )
            self.dialog_acerto.title_align = "center"
            self.dialog_acerto.open()
        else:
            self.LabelInstrucao.text = "Monte a palavra correta!"
            self.LabelInstrucao.text_color = (0, 0, 0, 1)

    # ========================================================
    # PRÓXIMA FASE
    # ========================================================
    def ProximaFase(self, *args):
        self.dialog_acerto.dismiss()
        self.fase_atual += 1
        self.tela_trila = self.manager.get_screen("PerfilAluno")
        self.tela_trila.atualizar_progresso()
        if self.fase_atual < 8:
            self.id_nivel = 1
        elif self.fase_atual < 16:
            self.id_nivel = 2
        else:
            self.id_nivel = 3

        if self.fase_atual >= len(self.fases):
            self.fase_atual = 0
            self.id_nivel = 1
            self.id_fase += 1

        self.inicio_tempo = time.time()
        self.CarregarFase(self.fase_atual)

    # ========================================================
    # ATUALIZAÇÃO DAS BORDAS
    # ========================================================
    def AtualizarBorda(self, instance, *args):
        if hasattr(instance, "borda"):
            instance.borda.rounded_rectangle = (instance.x, instance.y, instance.width, instance.height, 25)

    # ========================================================
    # SALVAMENTO DOS DADOS
    # ========================================================
    def salvar_dados(self, dados):
        Dados = []
        DadosJogosControle = DadosJogosController()
        Dados.append(self.ControleAluno.RE)
        Dados.append(self.ControleAluno.ProfissionalResponsavel)
        Dados.append('silabamix')
        for k, v in dados.items():
            Dados.append(v)
        DadosJogosControle.setNewDadoJogo(Dados)
        DadosJogosControle.SalvarDado()

class TelaJogoDaMemoria(MDScreen):

    def on_pre_enter(self, *args):
        # Pega controle do aluno (como na outra classe)
        self.ControleAluno = self.manager.get_screen("CarregamentoInicialAluno").ControleAluno
        self.iniciar_tempo()

    def iniciar_tempo(self):
        self.tempo_inicio = Clock.get_time()
        self.acertos = 0
        self.erros = 0
        self.tentativas = 0

    def tempo_gasto(self):
        return round(Clock.get_time() - self.tempo_inicio, 2)

    def salvar_dados(self, dados):
        Dados = []
        DadosJogosControle = DadosJogosController()
        Dados.append(self.ControleAluno.RE)
        Dados.append(self.ControleAluno.ProfissionalResponsavel)
        Dados.append('jogo da memória')  # Nome interno do jogo
        for k, v in dados.items():
            Dados.append(v)
        DadosJogosControle.setNewDadoJogo(Dados)
        DadosJogosControle.SalvarDado()

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"

    class FlipCard(MDCard):
        is_front = BooleanProperty(False)
        matched = BooleanProperty(False)
        front_text = StringProperty("Front")
        back_text = StringProperty("?")
        image_source = StringProperty("")
        scale_x = NumericProperty(1)

        def __init__(self, front_text="Front", image_source="", back_text="?", on_click=None, **kwargs):
            super().__init__(**kwargs)
            self.size_hint = (None, None)
            self.size = (120, 160)
            self.radius = [12, 12, 12, 12]
            self.md_bg_color = (0, 0.5, 0, 1)
            self.front_text = front_text
            self.back_text = back_text
            self.image_source = image_source
            self.on_click_callback = on_click

            # Container geral
            self.container = AnchorLayout()
            self.add_widget(self.container)

            # Lado frente
            self.front_layout = BoxLayout(
                orientation='vertical', padding=6, spacing=4, size_hint=(1, 1)
            )

            with self.front_layout.canvas.before:
                from kivy.graphics import Color, RoundedRectangle
                self.front_color = Color(1, 1, 1, 1)
                self.front_rect = RoundedRectangle(radius=self.radius)
                self.front_layout.bind(pos=self._update_front_bg, size=self._update_front_bg)

            self.front_image = Image(
                source=self.image_source,
                allow_stretch=True,
                keep_ratio=True,
                size_hint=(1, 0.7)
            )
            self.front_label = Label(
                text=self.front_text,
                halign="center",
                valign="middle",
                font_size=18,
                color=(0, 0, 0, 1),
                size_hint=(1, 0.3)
            )
            self.front_label.bind(size=self.front_label.setter('text_size'))
            self.front_layout.add_widget(self.front_image)
            self.front_layout.add_widget(self.front_label)
            self.front_layout.opacity = 0

            # Lado trás
            self.back_label = Label(
                text=self.back_text,
                halign="center",
                valign="middle",
                font_size=28,
                color=(1, 1, 1, 1),
                opacity=1
            )
            self.back_label.bind(size=self.back_label.setter('text_size'))

            self.container.add_widget(self.front_layout)
            self.container.add_widget(self.back_label)

        def _update_front_bg(self, *args):
            self.front_rect.pos = self.front_layout.pos
            self.front_rect.size = self.front_layout.size
            self.front_rect.radius = self.radius

        def on_touch_down(self, touch):
            if self.collide_point(*touch.pos):
                if self.matched:
                    return True
                if self.on_click_callback:
                    self.on_click_callback(self)
                return True
            return super().on_touch_down(touch)

        def reveal(self):
            if self.matched or self.is_front:
                return
            anim = Animation(scale_x=0, duration=0.15)
            anim.bind(on_complete=lambda *a: self._reveal_switch())
            anim.start(self)

        def _reveal_switch(self):
            self.is_front = True
            self.front_layout.opacity = 1
            self.back_label.opacity = 0
            self.md_bg_color = (1, 1, 1, 1)
            Animation(scale_x=1, duration=0.15).start(self)

        def hide(self):
            if self.matched or not self.is_front:
                return
            anim = Animation(scale_x=0, duration=0.15)
            anim.bind(on_complete=lambda *a: self._hide_switch())
            anim.start(self)

        def _hide_switch(self):
            self.is_front = False
            self.front_layout.opacity = 0
            self.back_label.opacity = 1
            self.md_bg_color = (0, 0.5, 0, 1)
            Animation(scale_x=1, duration=0.15).start(self)

        def lock_matched(self):
            self.matched = True
            self.is_front = True
            self.front_layout.opacity = 1
            self.back_label.opacity = 0
            self.md_bg_color = (1, 1, 1, 1)

        def on_scale_x(self, instance, value):
            self.width = 120 * value


    # ======= MÉTODOS PRINCIPAIS =======
    def on_enter(self):
        self.fase_atual = 0
        self.fases = [
            {"pares": [("Organizar os brinquedos", "Imagens/JogoDaMemoria/Imagem1.png"),
                       ("Guardar os materiais", "Imagens/JogoDaMemoria/Imagem2.png")]},
            {"pares": [("Dobrar as roupas", "Imagens/JogoDaMemoria/Imagem4.png"),
                       ("Alimentar o cachorro", "Imagens/JogoDaMemoria/Imagem3.png")],},
            {"pares": [("Organizar os brinquedos", "Imagens/JogoDaMemoria/Imagem1.png"),
                       ("Guardar os materiais", "Imagens/JogoDaMemoria/Imagem2.png"),
                       ("Alimentar o cachorro", "Imagens/JogoDaMemoria/Imagem3.png")]},
            {"pares": [("Organizar os brinquedos", "Imagens/JogoDaMemoria/Imagem1.png"),
                       ("Guardar os materiais", "Imagens/JogoDaMemoria/Imagem2.png"),
                       ("Alimentar o cachorro", "Imagens/JogoDaMemoria/Imagem3.png"),
                       ("Dobrar as roupas", "Imagens/JogoDaMemoria/Imagem4.png")]},
            {"pares": [("Organizar os brinquedos", "Imagens/JogoDaMemoria/Imagem1.png"),
                       ("Guardar os materiais", "Imagens/JogoDaMemoria/Imagem2.png"),
                       ("Alimentar o cachorro", "Imagens/JogoDaMemoria/Imagem3.png"),
                       ("Dobrar as roupas", "Imagens/JogoDaMemoria/Imagem4.png"),
                       ("Arrumar a cama", "Imagens/JogoDaMemoria/Imagem5.png")]},
            {"pares": [("Organizar os brinquedos", "Imagens/JogoDaMemoria/Imagem1.png"),
                       ("Guardar os materiais", "Imagens/JogoDaMemoria/Imagem2.png"),
                       ("Alimentar o cachorro", "Imagens/JogoDaMemoria/Imagem3.png"),
                       ("Dobrar as roupas", "Imagens/JogoDaMemoria/Imagem4.png"),
                       ("Arrumar a cama", "Imagens/JogoDaMemoria/Imagem5.png"),
                       ("Separar o lixo", "Imagens/JogoDaMemoria/Imagem6.png")]}
        ]
        self.carregar_fase(self.fase_atual)

    def carregar_fase(self, index):
        self.ids.JogoDaMemoria.clear_widgets()
        self.cards = []
        self.cards_virados = []

        fase = self.fases[index]
        pares = fase["pares"]

        cards_data = []
        for letra, img in pares:
            cards_data.append((letra, img))
            cards_data.append((letra, img))
        random.shuffle(cards_data)

        main_layout = BoxLayout(orientation='vertical', spacing=20, size_hint=(None, None))
        cols = min(4, len(cards_data))
        main_layout.width = cols * 120 + (cols - 1) * 20
        rows = (len(cards_data) + cols - 1) // cols
        main_layout.height = rows * 160 + (rows - 1) * 20

        row_layout = BoxLayout(spacing=20, size_hint_y=None, height=160)
        for i, (letra, img) in enumerate(cards_data):
            card = self.FlipCard(front_text=letra, image_source=img, back_text="", on_click=self.card_clicado)
            self.cards.append(card)
            row_layout.add_widget(card)
            if (i + 1) % cols == 0:
                main_layout.add_widget(row_layout)
                row_layout = BoxLayout(spacing=20, size_hint_y=None, height=160)
        if len(row_layout.children) > 0:
            main_layout.add_widget(row_layout)

        anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        anchor.add_widget(main_layout)
        self.ids.JogoDaMemoria.add_widget(anchor)

    def card_clicado(self, card):
        if card.matched or card in self.cards_virados or len(self.cards_virados) >= 2:
            return
        card.reveal()
        self.cards_virados.append(card)
        if len(self.cards_virados) == 2:
            self.tentativas += 1
            Clock.schedule_once(self.check_pair, 0.3)

    def check_pair(self, dt=0):
        c1, c2 = self.cards_virados
        if c1.front_text == c2.front_text:
            c1.lock_matched()
            c2.lock_matched()
            self.acertos += 1
            self.cards_virados = []
            if all(card.matched for card in self.cards):
                Clock.schedule_once(self.fase_completa, 0.5)
        else:
            self.erros += 1
            Clock.schedule_once(self.reset_cards, 0.7)

    def reset_cards(self, dt):
        for card in list(self.cards_virados):
            card.hide()
        self.cards_virados = []

    def fase_completa(self, dt):
        # Calcular desempenho
        tempo = self.tempo_gasto()
        total_pares = len(self.cards) // 2
        porcentagem = round((self.acertos / total_pares) * 100, 2)

        dados = {
            "ID_FASE": self.fase_atual + 1,
            "ID_NIVEL": 1,
            "PONTUACAO": self.acertos * 10,
            "PORCENTAGEM_COMPLETADA": porcentagem,
            "TEMPO_GASTO": tempo,
            "ACERTOS": self.acertos,
            "ERROS": self.erros,
            "TENTATIVAS": self.tentativas
        }
        self.salvar_dados(dados)

        dialog = MDDialog(
            title="🎉 Parabéns!",
            text=f"Você completou esta fase!\nPontuação: {self.acertos * 10}\nTempo: {tempo}s",
            radius=[25, 25, 25, 25],
            auto_dismiss=False,
            buttons=[
                MDFillRoundFlatIconButton(
                    icon="close",
                    text="Sair",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDFillRoundFlatIconButton(
                    icon="arrow-right",
                    text="Próxima Fase",
                    on_release=lambda x: self.proxima_fase(dialog)
                )
            ]
        )
        dialog.open()

    def proxima_fase(self, dialog):
        dialog.dismiss()
        self.fase_atual += 1
        if self.fase_atual >= len(self.fases):
            self.fase_atual = 0
        self.tela_trila = self.manager.get_screen("PerfilAluno")
        self.tela_trila.atualizar_progresso()
        self.carregar_fase(self.fase_atual)
        self.iniciar_tempo()

class TelaJogoMemoriaDasCores(MDScreen):
    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"

    class CardClicavel(MDCard):
        cor_normal = ListProperty([1, 1, 1, 1])
        cor_clara = ListProperty([1, 1, 1, 1])
        nome_cor = StringProperty("")

        def __init__(self, cor_normal, cor_clara, nome_cor, on_click, **kwargs):
            super().__init__(**kwargs)
            self.cor_normal = cor_normal
            self.cor_clara = cor_clara
            self.nome_cor = nome_cor
            self.md_bg_color = cor_normal
            self.radius = [20]
            self.size_hint = (0.9, 0.9)
            self.on_click = on_click
            self.bind(on_release=lambda x: self.on_click(self))

        def piscar(self, tempo=0.3):
            anim = Animation(md_bg_color=self.cor_clara, duration=tempo)
            anim += Animation(md_bg_color=self.cor_normal, duration=tempo)
            anim.start(self)

    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
        if tela_carregamento.ControleAluno:
            self.ControleAluno = tela_carregamento.ControleAluno
        else:
            self.ControleAluno = None
            
        self.ids.JogoMemoriaDosCores.clear_widgets()

        self.nivel_atual = 1
        self.sequencia_atual_index = 0
        self.posicao_seq = 0
        self.erro_box = None
        self.bloquear_clicks = False

        # === Dados do jogo ===
        self.tempo_inicio = time.time()
        self.acertos = 0
        self.erros = 0
        self.tentativas = 0

        # Criar linhas de cards
        linha1 = BoxLayout(spacing=10, size_hint=(1, 0.5))
        linha2 = BoxLayout(spacing=10, size_hint=(1, 0.5))

        self.card_vermelho = self.CardClicavel([1, 0, 0, 1], [1, 0.5, 0.5, 1], "vermelho", self.on_card_click)
        self.card_verde = self.CardClicavel([0, 0.6, 0, 1], [0.5, 1, 0.5, 1], "verde", self.on_card_click)
        self.card_amarelo = self.CardClicavel([0.8, 0.7, 0, 1], [1, 1, 0.5, 1], "amarelo", self.on_card_click)
        self.card_azul = self.CardClicavel([0, 0, 1, 1], [0.5, 0.5, 1, 1], "azul", self.on_card_click)

        linha1.add_widget(self.card_vermelho)
        linha1.add_widget(self.card_verde)
        linha2.add_widget(self.card_amarelo)
        linha2.add_widget(self.card_azul)

        BoxJogo = MDBoxLayout(
            orientation='vertical',
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            padding=dp(10),
            spacing=dp(10),
            size_hint=(0.9, 0.8),
        )

        BoxJogo.add_widget(linha1)
        BoxJogo.add_widget(linha2)

        if hasattr(self.ids, "JogoMemoriaDosCores"):
            self.ids.JogoMemoriaDosCores.add_widget(BoxJogo)

        self.cards = {
            "vermelho": self.card_vermelho,
            "verde": self.card_verde,
            "amarelo": self.card_amarelo,
            "azul": self.card_azul
        }

        # Sequências por nível
        self.niveis = {
            1: [["vermelho"],
                ["vermelho", "azul"],
                ["vermelho", "azul", "amarelo"],
                ["vermelho", "azul", "amarelo", "verde"],
                ["vermelho", "azul", "amarelo", "verde", "vermelho"],
                ["vermelho", "azul", "amarelo", "verde", "vermelho", "azul"],
                ["vermelho", "azul", "amarelo", "verde", "vermelho", "azul", "amarelo"]],
            2: [["azul"],
                ["azul", "verde"],
                ["azul", "verde", "vermelho"],
                ["azul", "verde", "vermelho", "amarelo"],
                ["azul", "verde", "vermelho", "amarelo", "verde"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde","azul"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde","azul", "vermelho"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde","azul", "vermelho", "amarelo"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde","azul", "vermelho", "amarelo", "verde"],
                ["azul", "verde", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde","azul", "vermelho", "amarelo", "verde", "azul"]],
            3: [["verde"],
                ["verde", "amarelo"],
                ["verde", "amarelo", "azul"],
                ["verde", "amarelo", "azul", "vermelho"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo","azul"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo","azul", "vermelho"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo","azul", "vermelho", "amarelo"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo","azul", "vermelho", "amarelo", "verde"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo","azul", "vermelho", "amarelo", "verde", "azul"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo","azul", "vermelho", "amarelo", "verde", "azul", "vermelho"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo", "azul", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo","azul", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde"],
                ["verde", "amarelo", "azul", "vermelho", "amarelo", "azul", "vermelho", "verde", "amarelo", "azul", "vermelho", "amarelo", "verde", "azul", "vermelho", "amarelo", "verde", "azul"]
                ]
        }
        self.mostrar_dialogo_play()

    # ======= DIÁLOGOS =======
    def mostrar_dialogo_play(self):
        self.dialog = MDDialog(
            title="🎮 Jogo da Memória das Cores",
            text="Clique em Play para começar!",
            radius=[25, 25, 25, 25],
            auto_dismiss=False,
            buttons=[
                MDFillRoundFlatIconButton(
                    icon="play",
                    text="Play",
                    on_release=self.iniciar_jogo
                )
            ]
        )
        self.dialog.open()

    def iniciar_jogo(self, *args):
        self.dialog.dismiss()
        self.tempo_inicio = time.time()
        self.mostrar_sequencia_atual()

    def mostrar_dialogo_nivel_completo(self):
        tempo_total = round(time.time() - self.tempo_inicio, 2)
        porcentagem = round((self.acertos / max(1, self.tentativas)) * 100, 2)
        pontuacao = self.acertos * 10

        dados = {
            "ID_FASE": 1,
            "ID_NIVEL": self.nivel_atual,
            "PONTUACAO": pontuacao,
            "PORCENTAGEM_COMPLETADA": porcentagem,
            "TEMPO_GASTO": tempo_total,
            "ACERTOS": self.acertos,
            "ERROS": self.erros,
            "TENTATIVAS": self.tentativas
        }

        self.salvar_dados(dados)

        self.dialog = MDDialog(
            title="🎉 Nível concluído!",
            text=f"Você completou o nível {self.nivel_atual}!",
            radius=[25, 25, 25, 25],
            auto_dismiss=False,
            buttons=[
                MDFillRoundFlatIconButton(
                    icon="close",
                    text="Sair",
                    on_release=lambda x: setattr(self.manager, 'current', 'PerfilAluno')
                ),
                MDFillRoundFlatIconButton(
                    icon="arrow-right",
                    text="Próxima Fase",
                    on_release=self.proxima_fase
                )
            ]
        )
        self.dialog.open()

    # ======= MÉTODOS PRINCIPAIS =======
    def mostrar_sequencia_atual(self):
        sequencia = self.niveis[self.nivel_atual][self.sequencia_atual_index]
        self.bloquear_clicks = True
        self.piscar_sequencia(sequencia)
        self.posicao_seq = 0

    def piscar_sequencia(self, sequencia, intervalo=0.5):
        tempo_inicial = 0
        for cor in sequencia:
            Clock.schedule_once(lambda dt, c=cor: self.cards[c].piscar(), tempo_inicial)
            tempo_inicial += intervalo
        Clock.schedule_once(lambda dt: self.liberar_clicks(), tempo_inicial)

    def liberar_clicks(self):
        self.bloquear_clicks = False

    def on_card_click(self, card):
        if self.bloquear_clicks:
            return
        card.piscar(tempo=0.15)
        self.tentativas += 1
        if self.Verificar(card):
            self.acertos += 1
            sequencia_corrente = self.niveis[self.nivel_atual][self.sequencia_atual_index]
            if self.posicao_seq >= len(sequencia_corrente):
                self.sequencia_atual_index += 1
                if self.sequencia_atual_index >= len(self.niveis[self.nivel_atual]):
                    self.mostrar_dialogo_nivel_completo()
                else:
                    Clock.schedule_once(lambda dt: self.mostrar_sequencia_atual(), 0.5)
        else:
            self.erros += 1

    def Verificar(self, card):
        cor_esperada = self.niveis[self.nivel_atual][self.sequencia_atual_index][self.posicao_seq]
        if card.nome_cor == cor_esperada:
            self.posicao_seq += 1
            return True
        else:
            self.mostrar_aviso_erro()
            self.posicao_seq = 0
            self.sequencia_atual_index = 0
            Clock.schedule_once(lambda dt: self.mostrar_sequencia_atual(), 0.5)
            return False

    def proxima_fase(self, *args):
        self.dialog.dismiss()
        self.nivel_atual += 1
        if self.nivel_atual > len(self.niveis):
            self.nivel_atual = 1
        self.sequencia_atual_index = 0
        self.posicao_seq = 0
        self.tela_trila = self.manager.get_screen("PerfilAluno")
        self.tela_trila.atualizar_progresso()
        self.mostrar_dialogo_play()

    # ======= AVISO DE ERRO =======
    def mostrar_aviso_erro(self):
        if self.erro_box:
            self.remove_widget(self.erro_box)

        self.erro_box = MDBoxLayout(
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            md_bg_color=(1, 0, 0, 0.8),
            radius=[15, 15, 15, 15],
            padding=10
        )
        label = MDLabel(
            text="❌ Errou! Tente novamente",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6"
        )
        self.erro_box.add_widget(label)
        self.add_widget(self.erro_box)
        Clock.schedule_once(lambda dt: self.remove_aviso_erro(), 1.5)

    def remove_aviso_erro(self):
        if self.erro_box:
            self.remove_widget(self.erro_box)
            self.erro_box = None

    # ======= SALVAR DADOS =======
    def salvar_dados(self, dados):
        Dados = []
        DadosJogosControle = DadosJogosController()
        Dados.append(self.ControleAluno.RE)
        Dados.append(self.ControleAluno.ProfissionalResponsavel)
        Dados.append('memoria das cores')  # Nome interno do jogo
        for k, v in dados.items():
            Dados.append(v)
        DadosJogosControle.setNewDadoJogo(Dados)
        DadosJogosControle.SalvarDado()

from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, NumericProperty, ListProperty
from Controllers.DadosJogosController import DadosJogosController  # ajuste o caminho se necessário
import time
import traceback

class TelaJogoSomSilaba(MDScreen):
    Tecla1Texto = StringProperty("")
    Tecla2Texto = StringProperty("")
    Tecla3Texto = StringProperty("")
    Tecla4Texto = StringProperty("")
    Tecla5Texto = StringProperty("")
    Tecla6Texto = StringProperty("")
    Tecla7Texto = StringProperty("")
    Tecla8Texto = StringProperty("")

    Nivel = NumericProperty(1)
    Fase = NumericProperty(0)
    SilabaCorreta = StringProperty("")
    PalavraCorreta = StringProperty("")
    PalavraFormada = ListProperty([])

    # Controle de tempo e estatísticas
    tempo_inicio = NumericProperty(0)
    acertos = NumericProperty(0)
    erros = NumericProperty(0)
    tentativas = NumericProperty(0)

    def Voltar_Click(self):
        if self.manager:
            self.manager.current = "PerfilAluno"

    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicialAluno")
        if tela_carregamento.ControleAluno:
            self.ControleAluno = tela_carregamento.ControleAluno
        else:
            self.ControleAluno = None

        self.tempo_inicio = time.time()
        self.acertos = 0
        self.erros = 0
        self.tentativas = 0

        # Estrutura: níveis -> fases -> sílabas da fase
        self.niveis = {
            1: [  # Nível 1 – sílabas únicas
                ['PA', 'DA', 'CO', 'NE', 'FI', 'ZE', 'CHI', 'RO'],
                ['BA', 'TE', 'CU', 'MA', 'VA', 'SI', 'JA', 'LI'],
                ['LU', 'RA', 'PO', 'ME', 'DI', 'FE', 'NO', 'TI'],
                ['GA', 'RE', 'SU', 'NA', 'VI', 'PI', 'JO', 'LE'],
                ['CA', 'MU', 'DO', 'SA', 'TA', 'KI', 'VO', 'XE']
            ],
            2: [  # Nível 2 – palavras de 2 sílabas
                ['PA', 'BA', 'CA', 'SA', 'TO', 'LA', 'GA', 'TA'],  # pato
                ['BA', 'PA', 'LO', 'MA', 'RI', 'PO', 'BO', 'NO'],  # bolo
                ['GA', 'TO', 'BE', 'BE', 'LU', 'PA', 'PI', 'CA'],  # gato
                ['MA', 'CA', 'CO', 'PI', 'BA', 'SA', 'LA', 'SO'],  # casa
                ['BO', 'LE', 'CA', 'RO', 'LE', 'LA', 'SO', 'PA']   # bola
            ],
            3: [  # Nível 3 – palavras de 3 sílabas
                ['BO', 'NE', 'RA', 'PI', 'LI', 'CA', 'TA', 'RA'],  # boneca
                ['CA', 'MA', 'PE', 'RA', 'PI', 'PO', 'CO', 'NA'],  # macaco
                ['GA', 'PE', 'XI', 'TA', 'TO', 'PA', 'RA', 'LA'],  # pétala
                ['PA', 'COL', 'SOL', 'LU', 'TO', 'MOL', 'RA', 'ME'],  # parasol
                ['BA', 'FI', 'NA', 'TI', 'ME', 'RA', 'SO', 'NA']   # banana
            ]
        }

        self.palavras_por_nivel = {
            1: ['PA', 'TE', 'LU', 'GA', 'SA'],
            2: ['PATO', 'BOLO', 'GATO', 'CASA', 'BOLA'],
            3: ['BONECA', 'MACACO', 'PETALA', 'PARASOL', 'BANANA']
        }

        self.AtualizarFase()

    def AtualizarFase(self):
        """Atualiza as sílabas e define a palavra correta"""
        silabas_fase = self.niveis[self.Nivel][self.Fase]

        (
            self.Tecla1Texto,
            self.Tecla2Texto,
            self.Tecla3Texto,
            self.Tecla4Texto,
            self.Tecla5Texto,
            self.Tecla6Texto,
            self.Tecla7Texto,
            self.Tecla8Texto,
        ) = silabas_fase

        self.PalavraCorreta = self.palavras_por_nivel[self.Nivel][self.Fase]
        self.PalavraFormada = []

        print(f"Nível: {self.Nivel} | Fase: {self.Fase + 1} | Palavra correta: {self.PalavraCorreta}")

    def TocarSilaba(self, silaba):
        sound = SoundLoader.load(f"Audios/SomSilaba/{silaba}.mp3")
        if sound:
            sound.play()

    def MostrarDialogo(self, titulo, mensagem, proxima_fase=False):
        botoes = [
            MDFlatButton(
                text="PRÓXIMO" if proxima_fase else "OK",
                on_release=lambda x: self.FecharDialogo(proxima_fase)
            )
        ]
        self.dialog = MDDialog(
            title=titulo,
            text=mensagem,
            buttons=botoes,
        )
        self.dialog.open()

    def FecharDialogo(self, proxima_fase=False):
        self.dialog.dismiss()
        if proxima_fase:
            self.AvancarFase()

    def AvancarFase(self):
        """Avança de fase e muda de nível se necessário"""
        self.Fase += 1
        total_fases = len(self.niveis[self.Nivel])
        self.tela_trila = self.manager.get_screen("PerfilAluno")
        self.tela_trila.atualizar_progresso()
        if self.Fase >= total_fases:
            self.Fase = 0
            self.Nivel += 1
            if self.Nivel > 3:
                self.Nivel = 1
                self.MostrarDialogo("Fim do jogo!", "Você completou todos os níveis!", proxima_fase=False)
                return

        self.AtualizarFase()

    def CliqueTecla(self, tecla):
        mapping = {
            1: self.Tecla1Texto,
            2: self.Tecla2Texto,
            3: self.Tecla3Texto,
            4: self.Tecla4Texto,
            5: self.Tecla5Texto,
            6: self.Tecla6Texto,
            7: self.Tecla7Texto,
            8: self.Tecla8Texto
        }
        silaba = mapping.get(tecla)
        if not silaba:
            return

        self.tentativas += 1
        print(f"Clicou: {silaba}")

        if self.Nivel == 1:
            if silaba == self.PalavraCorreta:
                self.acertos += 1
                self.salvar_dados()
                self.MostrarDialogo("Acertou!", f"Você escolheu corretamente: {silaba}", proxima_fase=True)
            else:
                self.erros += 1
                self.MostrarDialogo("Errou!", "Tente novamente!")
            return

        # Nível 2 e 3 – formar palavras
        self.PalavraFormada.append(silaba)
        palavra_atual = "".join(self.PalavraFormada)

        if not self.PalavraCorreta.startswith(palavra_atual):
            self.erros += 1
            self.PalavraFormada = []
            self.MostrarDialogo("Errou!", "Você errou a sequência! Tente novamente!")
            return

        if palavra_atual == self.PalavraCorreta:
            self.acertos += 1
            self.salvar_dados()
            self.MostrarDialogo("Acertou!", f"Você formou corretamente: {self.PalavraCorreta}", proxima_fase=True)

    # ======================================================
    # === Função padronizada de salvamento de dados ========
    # ======================================================
    def salvar_dados(self):
        try:
            print(f"ControleAluno: {self.ControleAluno}")

            if not hasattr(self, "ControleAluno") or self.ControleAluno is None:
                print("⚠️ Nenhum ControleAluno carregado. Dados não foram salvos.")
                return

            tempo_total = round(time.time() - self.tempo_inicio, 2)
            total_tentativas = max(1, self.tentativas)
            porcentagem = round((self.acertos / total_tentativas) * 100, 2)

            dados = {
                "ID_FASE": self.Fase + 1,
                "ID_NIVEL": self.Nivel,
                "PONTUACAO": self.acertos * 10,
                "PORCENTAGEM_COMPLETADA": porcentagem,
                "TEMPO_GASTO": tempo_total,
                "ACERTOS": self.acertos,
                "ERROS": self.erros,
                "TENTATIVAS": self.tentativas,
            }

            Dados = []
            DadosJogosControle = DadosJogosController()
            Dados.append(self.ControleAluno.RE)
            Dados.append(self.ControleAluno.ProfissionalResponsavel)
            Dados.append('somsilaba')

            for k, v in dados.items():
                Dados.append(v)

            DadosJogosControle.setNewDadoJogo(Dados)
            print(f"➡️ Chamando salvamento em DadosJogosController...{DadosJogosControle.getDadoJogo()}")
            DadosJogosControle.SalvarDado()
            print(f"✅ Dados salvos com sucesso: {Dados}")

        except Exception as e:
            print("❌ Erro ao salvar dados:")
            traceback.print_exc()