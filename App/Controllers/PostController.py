from Models.Post import Post
from Helpers.TratamentoErros import Erros as E
from Helpers.Requerimentos import Posts
import datetime
import random

class PostController:
    ID = None
    Usuario = None
    Arquivo = None
    Legenda = None
    Posts = None

    def __init__(self):
        self.Erros = E()
        self.Post = Post()
        self.Posts = Posts()


    def setNewPost(self, app):
        self.Usuario = app.ProfissionalControle.Usuario
        self.Arquivo = app.imagem_base64
        self.Legenda = app.LegendaPostarTextField.text

    def getPost(self):
        return [
            self.ID,
            self.Usuario,
            self.Arquivo,
            self.Legenda
        ]

    def setPost(self, condicao):
        post = self.Post.getPost(condicao)

        if not post:
            print("⚠️ Nenhum post encontrado.")
            return False

        (
            self.ID,
            self.Usuario,
            self.Arquivo,
            self.Legenda
        ) = post
        return True

    def Postar(self):
        try:
            self.Post.setPost(self.getPost())
            resultado = self.Post.Salvar()
            if resultado:
                self.ID = self.Post.Pesquisar('ID',f"USUARIO = '{self.Usuario}' ORDER BY DATA_POST DESC")[0][0]
                print(self.ID)
                self.Posts.Post(
                    self.ID,
                    self.Usuario,
                    self.Arquivo)
                return True
            return False
        except Exception as e:
            return e

    import datetime, random

    def ListarPosts(self):
        try:
            Resultado = self.Post.Pesquisar('*', '1 ORDER BY DATA_POST DESC')
            if not Resultado:
                print("⚠️ Nenhum resultado encontrado no banco.")
                return []

            lista = []
            for post in Resultado:
                lista.append({
                    "id": post[0],
                    "usuario": post[1],
                    "legenda": post[2],
                    "data_post": post[3] if len(post) > 3 else None
                })

            agora = datetime.datetime.now()
            intervalo_1h = datetime.timedelta(hours=1)
            intervalo_6h = datetime.timedelta(hours=6)

            posts_ultima_hora = []
            posts_ultimas_horas = []
            posts_hoje = []
            posts_antigos = []

            for post in lista:
                data = post["data_post"]

                # 🧩 Caso sem data: vai para os antigos
                if not data:
                    posts_antigos.append(post)
                    continue

                # 🔹 Converter string → datetime de forma robusta
                if isinstance(data, str):
                    formatos_possiveis = [
                        "%Y-%m-%d %H:%M:%S",
                        "%Y-%m-%dT%H:%M:%S",
                        "%Y/%m/%d %H:%M:%S",
                    ]
                    for fmt in formatos_possiveis:
                        try:
                            data = datetime.datetime.strptime(data, fmt)
                            break
                        except Exception:
                            continue
                    else:
                        print(f"⚠️ Formato de data desconhecido: {data}")
                        posts_antigos.append(post)
                        continue

                post["data_post"] = data
                diferenca = agora - data

                # 🔹 Classificação temporal
                if diferenca <= intervalo_1h:
                    posts_ultima_hora.append(post)
                elif diferenca <= intervalo_6h:
                    posts_ultimas_horas.append(post)
                elif data.date() == agora.date():
                    posts_hoje.append(post)
                else:
                    posts_antigos.append(post)

            # 🔹 Ordena cada grupo por data
            key_sort = lambda p: p["data_post"]
            for grupo in [posts_ultima_hora, posts_ultimas_horas, posts_hoje, posts_antigos]:
                grupo.sort(key=key_sort, reverse=True)
                random.shuffle(grupo)  # embaralha dentro do grupo

            # 🔹 Monta feed final (mantendo prioridade)
            lista_final = (
                    posts_ultima_hora +
                    posts_ultimas_horas +
                    posts_hoje +
                    posts_antigos
            )

            print(f"✅ Posts carregados: {len(lista_final)}")
            return lista_final

        except Exception as e:
            print(f"❌ Erro ao listar posts: {e}")
            return []

    def PesquisarPorUsuario(self, usuario):
        try:
            Resultado = self.Post.Pesquisar('*', f"USUARIO = '{usuario}' ORDER BY DATA_POST DESC")
            if not Resultado:
                return []

            lista = []
            for post in Resultado:
                lista.append({
                    "id": post[0] or "",
                    "usuario": post[1] or "",
                    "legenda": post[2] or ""
                })
            return lista

        except Exception as e:
            print(f"Erro ao pesquisar posts do usuário {usuario}: {e}")
            return []

    def PesquisarPorID(self,id):
        Resultado = self.Post.Pesquisar('*', f'ID = {id}')
        if not Resultado:
            return False
        return Resultado
    
    def ListarPostPorID(self, ids):
        lista = []
        for id in ids:
            Resultado = self.PesquisarPorID(id)
            if Resultado and isinstance(Resultado, list):
                for post in Resultado:
                    try:
                        lista.append({
                            "id": post[0],
                            "usuario": post[1],
                            "legenda": post[2]
                        })
                    except IndexError:
                        print(f"⚠️ Dados incompletos para o post com ID {id}.")
                        pass 
        return lista

    def ExcluirPost(self):
        try:
            self.Post.setPost(self.getPost())
            resultado = self.Post.Deletar()
            if resultado:
                return True
            print(self.Erros.GetErros(), 'teste')
            return False
        except Exception as e:
            print(e, self.Erros.GetErros())
            return e
        
