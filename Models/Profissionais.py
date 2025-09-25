from Banco import Banco
from Helpers.TratamentoErros import Erros

class Profissionais:
    def __init__(self, dados):
        self.TE = Erros()
        self.CPF = dados[0]
        self.Nome = dados[1]
        self.Usuario = dados[2]
        self.Profissao = dados[3]
        self.DataNascimento = dados[4]
        self.UF = dados[5]
        self.Cidade = dados[6]
        self.Escola = dados[7]
        self.Senha = dados[8]
        self.Biografia = dados[9]
        self.Favorito = dados[10]
        self.Rua = dados[11]
        self.Bairro = dados[12]
        self.FotoPerfil = dados[13]

    def Salvar(self):
        print("== Iniciando Salvar ==")
        print("Dados recebidos:", self.CPF, self.Nome, self.Usuario, self.Profissao,
              self.DataNascimento, self.UF, self.Cidade, self.Escola, self.Senha)
        '''
        if not self.CPF:
            print("Erro: CPF obrigatório!")
            self.TE.SetErro('CPF obrigatório!')
        else:
            if len(self.CPF) != 11 or not self.CPF.isdigit():
                print("Erro: CPF com quantidade de digitos inválido ou não numérico")
                self.TE.SetErro('CPF com quantidade de digitos invalido!')
            elif self.CPF == self.CPF[0] * 11:
                print("Erro: CPF com todos os dígitos iguais")
                self.TE.SetErro('CPF invalido! Digitos diferentes')
            else:
                soma1 = sum(int(self.CPF[i]) * (10 - i) for i in range(9))
                digito1 = 11 - (soma1 % 11)
                digito1 = 0 if digito1 >= 10 else digito1

                soma2 = sum(int(self.CPF[i]) * (11 - i) for i in range(10))
                digito2 = 11 - (soma2 % 11)
                digito2 = 0 if digito2 >= 10 else digito2

                print("CPF:", self.CPF, "-> dígitos calculados:", digito1, digito2)
                print("CPF dígitos informados:", self.CPF[9], self.CPF[10])

                if digito1 != int(self.CPF[9]) and digito2 != int(self.CPF[10]):
                    print("Erro: dígitos verificadores não batem")
                    self.TE.SetErro('CPF invalido!')
                else:
                    print('passou')
        '''

        if not self.Nome:
            print("Erro: Nome vazio")
            self.TE.SetErro('Nome vazio!')

        if not self.Usuario:
            print("Erro: Usuario vazio")
            self.TE.SetErro('Usuario vazio!')
        else:
            resultado_consulta = Banco.consultar('USUARIO', 'PROFISSIONAIS', f'USUARIO = {self.Usuario}')
            print("Consulta usuário existente retornou:", resultado_consulta)
            if resultado_consulta == self.Usuario:
                print("Erro: usuário já existe")
                self.TE.SetErro('Usuario existente!')

        if not self.Profissao:
            print("Erro: Profissão vazio")
            self.TE.SetErro('Profissão vazio!')

        if not self.UF:
            print("Erro: UF vazia")
            self.TE.SetErro('UF vazia!')
        elif len(self.UF) != 2:
            print("Erro: UF inválida, comprimento != 2")
            self.TE.SetErro('UF invalida!')

        if not self.Cidade:
            print("Erro: Cidade vazia")
            self.TE.SetErro('Cidade vazia!')

        if not self.Escola:
            print("Erro: Escola vazia")
            self.TE.SetErro('Escola vazia!')

        if not self.Senha:
            print("Erro: Senha vazia")
            self.TE.SetErro('Senha vazia!')

        print("Erros acumulados até aqui:", self.TE.GetErros())

        if self.TE.TemErros():
            print("Abandonando Salvar porque há erros")
            return False

        try:
            print("Tentando inserir no banco...")
            valores = [
                self.CPF, self.Nome, self.Usuario, self.Profissao, self.DataNascimento,
                self.UF, self.Cidade, self.Escola, self.Senha, self.Biografia,
                self.Favorito, self.Rua, self.Bairro, self.FotoPerfil
            ]
            print("Valores para inserção:", valores)
            Banco.inserir(
                'PROFISSIONAIS',
                'CPF,Nome,Usuario,Profissao,DataNascimento,UF,Cidade,Escola,Senha,Biografia,Favorito,Rua,Bairro,FotoPerfil',
                valores
            )
            print("Inserção bem-sucedida")
            return True
        except Exception as e:
            print("Erro ao inserir no banco:", e)
            self.TE.SetErro(f'Não foi possivel salvar. Erro:{e}')
            return False

    def Pesquisar(self, rotulo, condicao):
        try:
            return Banco.consultar(f'{rotulo}', 'PROFISSIONAIS', f'{condicao}')
        except Exception as e:
            self.TE.SetErro(f'Não foi possivel encontar. Erro:{e}')
            return False

    def Deletar(self):
        try:
            Banco.excluir('PROFISSIONAIS', f'CPF = {self.CPF}')
            return True
        except Exception as e:
            self.TE.SetErro(f'Não foi possivel encontar. Erro:{e}')
            return False

