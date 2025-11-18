from Banco import Banco
from Helpers.TratamentoErros import Erros

class Profissional:
    CPF = None
    Nome = None
    Usuario = None
    Profissao = None
    DataNascimento = None
    UF = None
    Cidade = None
    Escola = None
    Senha = None
    Biografia = None
    FotoPerfil = None

    def __init__(self):
        self.TE = Erros()

    def setProfissional(self, dados):
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
        self.FotoPerfil = dados[10]

    def Alterar(self):
        if not self.Nome or not self.Nome.strip():
            print("Erro: Nome vazio")
            self.TE.SetErro('Nome vazio!')

        if not self.Usuario or not self.Usuario.strip():
            print("Erro: Usuario vazio")
            self.TE.SetErro('Usuario vazio!')
        elif self.Usuario != self.Pesquisar('USUARIO',f'CPF = {self.CPF}'):
            if self.Pesquisar('USUARIO',f'USUARIO = {self.Usuario}'):
                self.TE.SetErro('Erro: Usuario existente')

        if not self.Profissao or not self.Profissao.strip():
            print("Erro: Profissão vazio")
            self.TE.SetErro('Profissão vazio!')

        if not self.UF or not self.UF.strip():
            print("Erro: UF vazia")
            self.TE.SetErro('UF vazia!')
        elif len(self.UF) != 2:
            print("Erro: UF inválida, comprimento != 2")
            self.TE.SetErro('UF invalida!')

        if not self.Cidade or not self.Cidade.strip():
            print("Erro: Cidade vazia")
            self.TE.SetErro('Cidade vazia!')

        if not self.Escola or not self.Escola.strip():
            print("Erro: Escola vazia")
            self.TE.SetErro('Escola vazia!')

        if not self.Senha or not self.Senha.strip():
            print("Erro: Senha vazia")
            self.TE.SetErro('Senha vazia!')

        print("Erros acumulados até aqui:", self.TE.GetErros())

        if self.TE.TemErros():
            print("Abandonando Atualizar porque há erros")
            return False
        try:
            Banco.editar(
                'PROFISSIONAIS',
                [
                    f"Nome = '{self.Nome}'",
                    f"Usuario = '{self.Usuario}'",
                    f"Profissao = '{self.Profissao}'",
                    f"DataNascimento = '{self.DataNascimento}'",
                    f"UF = '{self.UF}'",
                    f"Cidade = '{self.Cidade}'",
                    f"Escola = '{self.Escola}'",
                    f"Senha = '{self.Senha}'",
                    f"Biografia = '{self.Biografia}'",
                    f"FotoPerfil = '{self.FotoPerfil}'"
                ],
                f"CPF = '{self.CPF}'")
            return True
        except Exception as e:
            print("Erro ao editar no banco:", e)
            self.TE.SetErro(f'Não foi possivel editar. Erro:{e}')
            return False
        
    def Salvar(self):
        print("== Iniciando Salvar ==")
        print("Dados recebidos:", self.CPF, self.Nome, self.Usuario, self.Profissao,
              self.DataNascimento, self.UF, self.Cidade, self.Escola, self.Senha)
        if not self.CPF or not self.Nome:
            print("Erro: CPF obrigatório!")
            self.TE.SetErro('CPF obrigatório!')
        else:
            if len(self.CPF) != 11 or not self.CPF.isdigit():
                print("Erro: CPF com quantidade de digitos inválido ou não numérico")
                self.TE.SetErro('CPF com quantidade de digitos invalido!')
            elif self.CPF == self.CPF[0] * 11:
                print("Erro: CPF com todos os dígitos iguais")
                self.TE.SetErro('CPF invalido! Digitos iguais')
            else:
                soma1 = sum(int(self.CPF[i]) * (10 - i) for i in range(9))
                digito1 = 11 - (soma1 % 11)
                digito1 = 0 if digito1 >= 10 else digito1

                soma2 = sum(int(self.CPF[i]) * (11 - i) for i in range(10))
                digito2 = 11 - (soma2 % 11)
                digito2 = 0 if digito2 >= 10 else digito2

                print("CPF:", self.CPF, "-> dígitos calculados:", digito1, digito2)
                print("CPF dígitos informados:", self.CPF[9], self.CPF[10])

                if digito1 != int(self.CPF[9]) or digito2 != int(self.CPF[10]):
                    print("Erro: dígitos verificadores não batem")
                    self.TE.SetErro('CPF invalido!')
                else:
                    print('passou')

        if not self.Nome or not self.Nome.strip():
            print("Erro: Nome vazio")
            self.TE.SetErro('Nome vazio!')

        if not self.Usuario or not self.Usuario.strip():
            print("Erro: Usuario vazio")
            self.TE.SetErro('Usuario vazio!')

        if not self.Profissao or not self.Profissao.strip():
            print("Erro: Profissão vazio")
            self.TE.SetErro('Profissão vazio!')

        if not self.UF or not self.UF.strip():
            print("Erro: UF vazia")
            self.TE.SetErro('UF vazia!')
        elif len(self.UF) != 2:
            print("Erro: UF inválida, comprimento != 2")
            self.TE.SetErro('UF invalida!')

        if not self.Cidade or not self.Cidade.strip():
            print("Erro: Cidade vazia")
            self.TE.SetErro('Cidade vazia!')

        if not self.Escola or not self.Escola.strip():
            print("Erro: Escola vazia")
            self.TE.SetErro('Escola vazia!')

        if not self.Senha or not self.Senha.strip():
            print("Erro: Senha vazia")
            self.TE.SetErro('Senha vazia!')

        print("Erros acumulados até aqui:", self.TE.GetErros())

        if self.TE.TemErros():
            print("Abandonando Salvar porque há erros")
            return False

        try:
            print("Tentando inserir no banco...")
            colunas = "CPF,Nome,Usuario,Profissao,DataNascimento,UF,Cidade,Escola,Senha,Biografia,FotoPerfil"
            valores = [
                self.CPF,
                self.Nome,
                self.Usuario,
                self.Profissao,
                self.DataNascimento,  # pode ser None
                self.UF,
                self.Cidade,
                self.Escola,
                self.Senha,
                self.Biografia,
                self.FotoPerfil
            ]
            print(valores)
            Banco.inserir("PROFISSIONAIS", colunas, valores)
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

    def getUsuario(self, condicao):
        Resultado = Banco.consultar('*',"PROFISSIONAIS", condicao)
        print(Resultado)
        # Se não houver resultado ou vier False, evita erro
        if not Resultado or Resultado is False:
            self.TE.SetErro(f'Não foi possivel encontar Aluno')
            return False

        try:
            self.CPF = Resultado[0][0]
            self.Nome = Resultado[0][1]
            self.Usuario = Resultado[0][2]
            self.Profissao = Resultado[0][3]
            self.DataNascimento = Resultado[0][4]
            self.UF = Resultado[0][5]
            self.Cidade = Resultado[0][6]
            self.Escola = Resultado[0][7]
            self.Senha = Resultado[0][8]
            self.Biografia = Resultado[0][9]
            self.FotoPerfil = Resultado[0][10]

            return [
                self.CPF, self.Nome, self.Usuario, self.Profissao, self.DataNascimento,
                self.UF, self.Cidade, self.Escola, self.Senha, self.Biografia, self.FotoPerfil
            ]

        except Exception as e:
            self.TE.SetErro(f'Não foi buscar aluno. Erro:{e}')
            return False


