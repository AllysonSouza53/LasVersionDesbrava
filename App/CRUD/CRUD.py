import mysql.connector

class Banco:
    def __init__(self, host, usuario, senha, banco):
        self.host = host
        self.usuario = usuario
        self.senha = senha
        self.banco = banco

    def conectar(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )

    def inserir(self, tabela, colunas, valores):
        conexao = self.conectar()
        cursor = conexao.cursor()
        placeholders = ', '.join(['%s'] * len(valores))
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

    def consultar(self, colunas, tabela, condicao=None):
        conexao = self.conectar()
        cursor = conexao.cursor()
        sql = f"SELECT {colunas} FROM {tabela} WHERE {condicao};"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultado

    def editar(self,tabela, valores, condicao):
        conexao = self.conectar()
        cursor = conexao.cursor()
        query = f"UPDATE {tabela} SET {', '.join(valores)} WHERE {condicao}"
        print("DEBUG QUERY:", query)  # opcional para ver a SQL completa
        cursor.execute(query)
        conexao.commit()

    def excluir(self, tabela, condicao):
        conexao = self.conectar()
        cursor = conexao.cursor()
        sql = f"DELETE FROM {tabela} WHERE {condicao};"
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()