from Banco import Banco

class Login:
    def __init__(self,login):
        self.usuario = login[0]
        self.senha = login[1]

    def Logar(self):
        try:
            if not self.usuario:
                return print('Usuario obrigatório')
            elif self.usuario != Banco.consultar('USUARIO', 'PROFISSIONAIS', f"USUARIO ='{self.usuario}'")[0][0]:
                print(Banco.consultar('USUARIO', 'PROFISSIONAIS', f"USUARIO ='{self.usuario}'"))
                return print('Usuario não cadastrado! Cadastra-se')
            else:
                pass

            if not self .senha:
                return print('Senha obrigatória')
            elif self.senha != Banco.consultar('SENHA', 'PROFISSIONAIS', f"SENHA ='{self.senha}'")[0][0]:
                return print('Senha incorreta')
            else:
                pass

            return True
        except Exception as e:
            print(f'Erro ao logar:{e}')
