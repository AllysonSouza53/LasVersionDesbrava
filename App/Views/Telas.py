
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.fitimage import FitImage
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.image import Image as CoreImage
from kivy.core.window import Window
from App.Controllers.AlunosController import AlunoController
from App.Controllers.PostController import PostController
from App.Controllers.ProfissionalController import ProfissionalControler
from App.Controllers.ProfissionaisLoginController import LoginController
from App.Helpers.Requerimentos import Escolas,Perfis,Posts,Cidades
from App.Banco import Banco
from App.Controllers.FavoritosController import FavoritosController
import io, base64
import os

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
        if os.path.exists('App/Imagens/FotoPerfil.png'):
            os.remove('App/Imagens/FotoPerfil.png')
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
    def on_pre_enter(self, *args):
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.Profissional = tela_carregamento.Profissional
        else:
            self.Profissional = None

        self.MostrarDados()
        self.ListarPosts()

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
        self.file_manager = MDFileManager(
            exit_manager=self.fechar_file_manager,
            select_path=self.selecionar_imagem
        )

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
        self.ids.ProfissãoAlterarTextField.text = f'{self.ControlePerfil.Profissao}'
        self.ids.DataNascimentoAlterarTextField.text = f'{self.ControlePerfil.DataNascimento}'
        self.ids.EstadoAlterarTextField.text = f'{self.ControlePerfil.UF}'
        self.ids.CidadeAlterarTextField.text = f'{self.ControlePerfil.Cidade}'
        self.ids.EscolaAlterarTextField.text = f'{self.ControlePerfil.Escola}'
        self.ids.BiografiaAlterarTextField.text = f'{self.ControlePerfil.Biografia}'
        self.ids.SenhaAlterarTextField.text = f'{self.ControlePerfil.Senha}'

        from kivy.cache import Cache


        # Limpa cache da imagem
        Cache.remove('kv.image', 'Imagens/FotoPerfil.png')

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

    def ProfissãoAlterarTextField_Focus(self,instancia,focus):
        if focus:
            menu_items = self.ProfissãoAlterarTextField_AddItens(Banco.consultar('NOME', 'PROFISSOES', '1'))
            MDDropdownMenu(caller=instancia, items=menu_items).open()
        else:
            pass

    def ProfissãoAlterarTextField_AddItens(self, itens):
        menu_items = [
            {
                "text": f"{item[0].translate(str.maketrans("", "", "(),'"))}",
                "on_release": lambda
                    x=f"{item[0].translate(str.maketrans("", "", "(),'"))}": self.ProsissaoAlterarTextField_ItensClick(x),
            } for item in itens
        ]
        return menu_items

    def ProsissaoAlterarTextField_ItensClick(self, text_item):
        self.ids.ProsissaoCadastroTextField.text = text_item

    def TrocarImagem(self):
        initial_path = "/" if Window.system_size[0] > 0 else "."
        self.file_manager.show(initial_path)

    def fechar_file_manager(self, *args):
        self.file_manager.close()

    def selecionar_imagem(self, path):
        self.fechar_file_manager()
        with open(path, "rb") as f:
            imagem_bytes = f.read()
        self.imagem_base64 = base64.b64encode(imagem_bytes).decode("utf-8")
        self.ids.PerfilImagem.source = self.imagem_base64
        MDDialog(title="Imagem selecionada", text=f"Caminho: {path}").open()

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
    Favoritos = None
    def on_pre_enter(self, *args):
        self.Favoritos = FavoritosController()
        tela_carregamento = self.manager.get_screen("CarregamentoInicial")
        if tela_carregamento.Profissional:
            self.ControlePerfil = tela_carregamento.Profissional
        else:
            self.ControlePerfil = None
        if self.Favoritos.setFavorito(f"USUARIO = {self.ControlePerfil.Usuario}"):
            self.Favoritos.ID = FavoritosController

        self.ListarFavoritos()
        self.ListarAlbuns()

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

    def ListarAlbuns(self):
        Albuns = self.ids.AlbunsUsuario


    def ListarFavoritos(self):
        pass

#_________________________________________________________________________________________________________________________
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

    def ComunidadeMDTextButton_Click(self):
        if self.manager:
            self.manager.current = "ComunidadeProfissionais"

#_________________________________________________________________________________________________________________________
class TelaInformacoesJogosProfissionais(MDScreen):
    def on_enter(self, *args):
        pass

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