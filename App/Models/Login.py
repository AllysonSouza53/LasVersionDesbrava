from App.Banco import Banco
from App.Helpers.TratamentoErros import Erros

class Login:
    usuario = None
    senha = None

    def __init__(self,login):
        self.usuario = login[0]
        self.senha = login[1]
        self.Erros = Erros()

    def Logar(self):
        try:
            if not self.usuario:
                self.Erros.SetErro('Usuario obrigatório')
            elif self.usuario != Banco.consultar('USUARIO', 'PROFISSIONAIS', f"USUARIO ='{self.usuario}'")[0][0]:
                self.Erros.SetErro('Usuario não cadastrado! Cadastra-se')

            if not self .senha:
                self.Erros.SetErro('Senha obrigatória!')
            elif self.senha != Banco.consultar('SENHA', 'PROFISSIONAIS', f"SENHA ='{self.senha}'")[0][0]:
                self.Erros.SetErro('Senha incorreta')

            if self.Erros.TemErros():
                return False
            else:
                return True

        except Exception as e:
            self.Erros.SetErro(f'Error:{e}')
            return False
