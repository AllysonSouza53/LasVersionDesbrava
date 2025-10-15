from App.Models.Post import Post
from App.Helpers.TratamentoErros import Erros as E
import datetime
import random

class PostController:
    ID = None
    Usuario = None
    Arquivo = None
    Legenda = None
    def __init__(self):
        self.Erros = E()
        self.Post = Post()


    def setNewPost(self, app):
        pass

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
                return True
            return False
        except Exception as e:
            return e

    import datetime
    import random

    def ListarPosts(self):
        try:
            # Busca todos os posts, do mais recente ao mais antigo
            Resultado = self.Post.Pesquisar('*', '1 ORDER BY DATA_POST DESC')
            if not Resultado:
                return []

            lista = []
            for post in Resultado:
                lista.append({
                    "id": post[0],
                    "usuario": post[1],
                    "arquivo": post[2],
                    "legenda": post[3],
                    "data_post": post[4] if len(post) > 4 else None
                })

            agora = datetime.datetime.now()
            intervalo_1h = datetime.timedelta(hours=1)
            intervalo_6h = datetime.timedelta(hours=6)  # 🔹 Ajuste se quiser mais ou menos

            posts_ultima_hora = []
            posts_ultimas_horas = []
            posts_hoje = []
            posts_antigos = []

            for post in lista:
                if not post["data_post"]:
                    posts_antigos.append(post)
                    continue

                data = post["data_post"]
                if isinstance(data, str):
                    data = datetime.datetime.fromisoformat(data)

                diferenca = agora - data

                # 🔸 Classificação de tempo
                if diferenca <= intervalo_1h:
                    posts_ultima_hora.append(post)
                elif diferenca <= intervalo_6h:
                    posts_ultimas_horas.append(post)
                elif data.date() == agora.date():
                    posts_hoje.append(post)
                else:
                    posts_antigos.append(post)

            # Embaralhar (opcional)
            random.shuffle(posts_ultima_hora)
            random.shuffle(posts_ultimas_horas)
            random.shuffle(posts_hoje)
            random.shuffle(posts_antigos)

            # 🔸 Ordem final: última hora → últimas horas → hoje → antigos
            lista_final = (
                    posts_ultima_hora +
                    posts_ultimas_horas +
                    posts_hoje +
                    posts_antigos
            )

            return lista_final

        except Exception as e:
            print(f"Erro ao listar posts: {e}")
            return []

    def PesquisarPorUsuario(self, usuario):
        try:
            Resultado = self.Post.Pesquisar('*', f"USUARIO = '{usuario}' ORDER BY DATA_POST DESC")
            if not Resultado:
                return []

            lista = []
            for post in Resultado:
                lista.append({
                    "CPF": post[0] or "",
                    "usuario": post[1] or "",
                    "arquivo": post[2] or "",
                    "legenda": post[3] or ""
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
