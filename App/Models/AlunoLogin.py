from Banco import Banco
from Helpers.TratamentoErros import Erros

class Login:
    usuario = None
    RA = None

    def __init__(self,login):
        self.usuario = login[0]
        self.RA = login[1]
        print(f'Login model - Usuario: {self.usuario} | RA: {self.RA}')
        self.Erros = Erros()

    def Logar(self):
        try:
            self.Erros.LimpeErros()
            if not self.usuario:
                self.Erros.SetErro('Usuario obrigatório')
            elif self.usuario != Banco.consultar('USUARIO', 'ALUNOS', f"USUARIO ='{self.usuario}'")[0][0]:
                self.Erros.SetErro('Usuario não cadastrado! peça para seu professor cadastra-lo')
                print('Usuario não cadastrado! peça para seu professor cadastra-lo')

            if not self.RA:
                self.Erros.SetErro('RA obrigatório!')
            elif self.RA != str(Banco.consultar('RE', 'ALUNOS', f"RE = {self.RA}")[0][0]):
                print(Banco.consultar('RE', 'ALUNOS', f"RE = {self.RA}")[0][0])
                self.Erros.SetErro('RA incorreto')
            
            print(self.Erros.GetErros())

            if self.Erros.TemErros():
                return False
            else:
                return True

        except Exception as e:
            self.Erros.SetErro(f'Error:{e}')
            return False