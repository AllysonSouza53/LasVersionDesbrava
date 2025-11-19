from Banco import Banco
from Helpers.TratamentoErros import Erros

class Login:
    usuario = None
    senha = None

    def __init__(self,login):
        self.usuario = login[0]
        self.senha = login[1]
        self.Erros = Erros()

    def Logar(self):
        try:
            usuario = None
            self.Erros.LimpeErros()
            usuario = Banco.consultar('USUARIO', 'PROFISSIONAIS', f"USUARIO ='{self.usuario}'")
            senha = Banco.consultar('SENHA', 'PROFISSIONAIS', f"USUARIO ='{self.usuario}' AND SENHA = '{self.senha}'")
            print(usuario , senha)
            if not self.usuario:
                self.Erros.SetErro('Usuario obrigatório')
            elif usuario == []:
                print(usuario)
                print(self.usuario)
                self.Erros.SetErro('Usuario não cadastrado! Cadastra-se')

            if not self.senha:
                self.Erros.SetErro('Senha obrigatória!')
            elif senha == []:
                self.Erros.SetErro('Senha incorreta')

            if self.Erros.TemErros():
                return False
            else:
                return True

        except Exception as e:
            self.Erros.SetErro(f'Erro no logar:{e}')
            return False
