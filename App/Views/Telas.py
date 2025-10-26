from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from kivy.uix.image import Image
from Controllers.AlunosController import AlunoController
from Controllers.ComentarioController import ComentarioController
from Controllers.DadosJogosController import DadosJogosController
from Controllers.FavoritosController import FavoritosController
from Controllers.PostController import PostController
from Controllers.ProfissionalController import ProfissionalControler
from Controllers.ProfissionaisLoginController import LoginController
from Helpers.Requerimentos import Escolas,Perfis,Posts,Cidades
from Banco import Banco
import io, base64
import os
from kivymd.uix.label import MDIcon
from functools import partial
from kivymd.uix.button import MDRoundFlatButton  # compatível
from Helpers.TratamentoErros import Erros
from Controllers.AlbumController import AlbumController
from kivymd.toast import toast
from kivymd.uix.textfield import MDTextField
from Controllers.AlunoControllerLogin import LoginAlunoController


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
                self.manager.current = "CarregamentoInicial"

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
            controle = ProfissionalControler()
            controle.setCadastro(self.manager)
            if controle.Cadastar():
                self.manager.current = "LoginProfissional"
        else:
            print("root ainda não existe")

#-------------------------------------------------------------------------------------------------------
class TelaCarregamentoInicial(MDScreen):
    Profissional = None
    def on_enter(self, *args):
        self.Sessao = LoginController()
        self.Sessao.setLogin(self.manager)
        self.Profissional = ProfissionalControler()
        self.Profissional.setUsuario(f'USUARIO = "{self.Sessao.usuario}"')
        if os.path.exists('Imagens/FotoPerfil.png'):
            os.remove('Imagens/FotoPerfil.png')
        else:
            pass
        self.GetFotoPerfil(self.Sessao.usuario)
        if self.manager:
            self.manager.current = "PerfilProfissional"

    def GetFotoPerfil(self, usuario):
        Perfil = Perfis()
        UsuarioPerfil = Perfil.GetPorUsuario(usuario)
        if UsuarioPerfil is None:
            UsuarioPerfilImagem = Perfil.GetPorUsuario('ADMIN')['imagem']
            imagem_bytes = base64.b64decode(UsuarioPerfilImagem)
            with open("Imagens/FotoPerfil.png", "wb") as f:
                f.write(imagem_bytes)
        else:
            UsuarioPerfilImagem = UsuarioPerfil['imagem']
            imagem_bytes = base64.b64decode(UsuarioPerfilImagem)
            with open("Imagens/FotoPerfil.png", "wb") as f:
                f.write(imagem_bytes)
#-------------------------------------------------------------------------------------------------------
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
        self.MostrarDados()
        self.ListarPosts()

    def MostrarDados(self):
        if not self.ControlePerfil:
            return
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
#_________________________________________________________________________________________________________________________
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
            select_path=self.selecionar_imagem,
            preview=True,  # Mostra miniaturas
        )
        # Inicia no diretório padrão (por exemplo, a pasta Imagens)
        import os
        start_dir = os.path.expanduser("~/Pictures")  # ou "~/" para pasta do usuário

    def fechar_file_manager(self, *args):
        """
        Fecha ou volta o diretório atual do file manager.
        """
        try:
            self.file_manager.close()
        except Exception as e:
            print(f"Erro ao fechar o FileManager: {e}")

    def on_pre_enter(self, *args):
        self.ids.FotoPerfil.background_normal = "Imagens/FotoPerfil.png"
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




        # Limpa cache da imagem

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

        self.ids.PerfilImagem.texture = textura
        self.ids.PerfilImagem.souce = ''

        MDDialog(title="Imagem selecionada", text=f"Caminho: {path}").open()
        from kivy.cache import Cache

        Cache.remove('kv.image', 'Imagens/FotoPerfil.png')

    def AlterarPerfilButton_Click(self):
        # Garante que já existe uma imagem convertida em base64
        if not hasattr(self, "imagem_base64"):
            MDDialog(title="Erro", text="Nenhuma imagem foi selecionada.").open()
            return

        # Atualiza o objeto de controle
        self.ControlePerfil.FotoPerfil = self.imagem_base64

        # Atualiza no banco/API
        Perfil = Perfis()
        if not Perfil.GetPorUsuario(self.ControlePerfil.Usuario):
            Perfil.Post(self.ControlePerfil.CPF, self.ControlePerfil.Usuario, self.ControlePerfil.FotoPerfil)
        else:
            Perfil.Update(self.ControlePerfil.CPF, self.ControlePerfil.Usuario, self.ControlePerfil.FotoPerfil)

        MDDialog(
            title="Sucesso",
            text="A imagem de perfil foi atualizada!"
        ).open()
        if self.manager:
            self.manager.current = "CarregamentoInicial"

    def GetFotoPerfil(self, usuario):
        Perfil = Perfis()
        UsuarioPerfil = Perfil.GetPorUsuario(usuario)
        if UsuarioPerfil is None:
            UsuarioPerfilImagem = Perfil.GetPorUsuario('ADMIN')['imagem']
            self.imagem_bytes = base64.b64decode(UsuarioPerfilImagem)
            with open("Imagens/FotoPerfil.png", "wb") as f:
                f.write(self.imagem_bytes)
        else:
            UsuarioPerfilImagem = UsuarioPerfil['imagem']
            self.imagem_bytes = base64.b64decode(UsuarioPerfilImagem)
            with open("Imagens/FotoPerfil.png", "wb") as f:
                f.write(self.imagem_bytes)
#_________________________________________________________________________________________________________________________

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
#_________________________________________________________________________________________________________________________
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

#_________________________________________________________________________________________________________________________
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

#_________________________________________________________________________________________________________________________
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

class TelaPerfilAluno(MDScreen):
    def PerfilMDTextButton_Click(self):
        pass
    
    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InicialAluno"

    def ConquistasMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "Conquistas"

class TelaConquistas(MDScreen):
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