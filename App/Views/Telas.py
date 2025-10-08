import io

from Demos.c_extension.setup import sources
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivymd.uix.carousel import MDCarousel
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from App.Controllers.AlunosController import AlunoController
from App.Controllers.PostController import PostController
from App.Controllers.ProfissionalController import ProfissionalControler
from App.Controllers.ProfissionaisLoginController import LoginController
from App.Helpers.Requerimentos import Escolas,Perfis,Posts,Cidades
from App.Banco import Banco
import base64

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
            controle = ProfissionalControler()
            controle.setCadastro(self.manager)
            if controle.Cadastar():
                self.manager.current = "LoginProfissional"
        else:
            print("root ainda não existe")

#-------------------------------------------------------------------------------------------------------
class TelaPerfilProfissional(MDScreen):

    def on_enter(self, *args):
        self.Sessao = LoginController()
        self.Sessao.setLogin(self.manager)
        self.Profissional = ProfissionalControler()
        self.Profissional.setUsuario(f'USUARIO = "{self.Sessao.usuario}"')
        self.GetFotoPerfil(self.Sessao.usuario)
        self.MostrarDados()
        self.ListarPosts()

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

    def GetArquivoPosts(self, usuario):
        try:
            ListaPosts = Posts()
            UsuarioPerfil = ListaPosts.GetPorUsuario(usuario)
            if not UsuarioPerfil:
                return []

            listaposts = []
            for post in UsuarioPerfil:
                imagem = post['imagem']

                if imagem:
                    try:
                        # Converte Base64 para uma imagem utilizável no Kivy
                        data = io.BytesIO(base64.b64decode(imagem))
                        imagem = CoreImage(data, ext='png').texture
                        listaposts.append({"imagem": imagem})
                    except Exception as e:
                        print(f"Erro ao decodificar imagem do post: {e}")

            return listaposts

        except Exception as e:
            print(f"Erro ao decodificar imagem do post: {e}")
            return []

    def MostrarDados(self):
        self.ids.UsuarioPerfilLabel.text = f'@{self.Profissional.Usuario}'
        self.ids.NomePerfilLabel.text = f'Nome:{self.Profissional.Nome}'
        self.ids.CPFPerfilLabel.text = f'CPF:{self.Profissional.CPF}'
        self.ids.ProfissaoPerfilLabel.text = f'Profissão:{self.Profissional.Profissao}'
        self.ids.EscolaPerfilLabel.text = f'Escola:{self.Profissional.Escola}'
        self.ids.BiografiaPerfilLabel.text = f'Biografia:{self.Profissional.Biografia}'

    def ListarPosts(self):
        Post = PostController()
        FeedPerfil = self.ids.feed_grid

        resposta = Post.PesquisarPorUsuario(self.Profissional.Usuario)
        imagens = self.GetArquivoPosts(self.Profissional.Usuario)

        FeedPerfil.clear_widgets()

        if not resposta or not imagens:
            FeedPerfil.cols = 1
            FeedPerfil.add_widget(
                MDLabel(
                    text='Sem posts. Poste algo!',
                    font_style="H6",
                    halign="center",
                    theme_text_color="Custom",  # permite cor personalizada
                    text_color=(1, 1, 1, 1)
                )
            )
            return

        FeedPerfil.cols = 2
        for i, post in enumerate(resposta):
            imagem = imagens[i]['imagem'] if i < len(imagens) else None

            card = MDCard(
                size_hint_y=None,
                height=dp(250),
                padding=dp(10),
                orientation="vertical",
                ripple_behavior=True
            )

            usuario = MDLabel(
                text=f'@{self.Profissional.Usuario}',
                font_style="H6"
            )
            card.add_widget(usuario)

            if imagem:
                imagem_widget = FitImage(texture=imagem, size_hint_y=0.8)
                card.add_widget(imagem_widget)

            legenda = MDLabel(
                text=post.get('descricao', ''),
                halign="center",
                theme_text_color="Secondary"
            )
            card.add_widget(legenda)

            FeedPerfil.add_widget(card)

    def AlterarPerfilButton_Click(self):
        if self.manager:
            self.manager.current = "AlterarPerfilProfissional"

    def FavoritosPerfilButton_Click(self):
        if self.manager:
            self.manager.current = "FavoritosProfissional"

    def PerfilMDTextButton_Click(self):
        pass

    def AlunosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "AlunosProfissional"

    def JogosMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "InformacoesJogosProfissionais"

class TelaAlterarPerfilProfissional(MDScreen):
    pass

class TelaFavoritosProfissional(MDScreen):
    pass

class TelaAlunosProfissional(MDScreen):
    Sessao = LoginController()
    ProfissionalControle = ProfissionalControler()
    AlunoControle = AlunoController()

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
            SemAluno = MDLabel(
                text='Sem alunos.',
                font_style="H6",
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1)
            )
            DataGrid.add_widget(SemAluno)
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
                    ("Escola", dp(30)),
                    ("Genero", dp(30)),
                    ("Turma", dp(30)),
                    ("Diagnostico", dp(30)),
                    ('DataNascimento', dp(30))
                ],
                row_data=Dados
            )


            DataGrid.add_widget(Widget())
            DataGrid.add_widget(tabela)
            DataGrid.add_widget(Widget())

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

class TelaInformacoesJogosProfissionais(MDScreen):
    def on_enter(self, *args):
        self.CarroselJogos()

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

    def CarroselJogos(self):
        BoxCarrossel = self.ids.CarrosselBox
        BoxCarrossel.clear_widgets()

        # Cria o carrossel
        carrosel = MDCarousel(
            direction='right',
            loop=True,
            size_hint=(1, 1)  # ocupar todo o BoxCarrossel
        )

        jogos = [
            {"nome": "Jogo 1", "imagem": "Imagens/CapaJogo1.png"},
            {"nome": "Jogo 2", "imagem": "Imagens/CapaJogo2.png"},
            {"nome": "Jogo 3", "imagem": "Imagens/CapaJogo3.png"},
            {"nome": "Jogo 4", "imagem": "Imagens/CapaJogo4.png"},
            {"nome": "Jogo 5", "imagem": "Imagens/CapaJogo5.png"},
            {"nome": "Jogo 6", "imagem": "Imagens/CapaJogo6.png"},
        ]

        for jogo in jogos:
            card = MDCard(size_hint=(None, None), size=(dp(300), dp(250)), elevation=8, radius=[15] * 4)
            card_layout = BoxLayout(orientation='vertical')

            img = FitImage(source=jogo["imagem"], size_hint=(1, 0.7), keep_ratio=True)
            label = MDLabel(text=jogo["nome"], halign="center", font_style="H5", size_hint=(1, 0.3))

            card_layout.add_widget(img)
            card_layout.add_widget(label)
            card.add_widget(card_layout)

            carrosel.add_widget(card)

        # Adiciona o carrossel ao layout
        BoxCarrossel.add_widget(carrosel)