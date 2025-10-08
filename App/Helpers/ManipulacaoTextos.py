def ler_caracter(texto, posicao):
  try:
      return texto[posicao]
  except IndexError:
      print(f"Posição {posicao} fora do intervalo.")
  except Exception as e:
      print(f"Erro ao ler caractere: {e}")

def sub_texto(texto, inicio, fim):
  return texto[inicio:fim]

def ler_linha(texto, num_linha):
  try:
      linhas = texto.splitlines()
      return linhas[num_linha]
  except IndexError:
      print(f"Linha {num_linha} não encontrada")
  except Exception as e:
      print(f"Erro ao ler linha: {e}")

def contar_caracteres(texto):
  return len(texto)

def contar_palavras(texto):
  return len(texto.split())

def contar_linhas(texto):
  return len(texto.splitlines())

def substituir_texto(texto, antigo, novo):
  return texto.replace(antigo, novo)

def contem_substring(texto, substring):
  return substring in texto

def remover_espacos(texto):
  return texto.strip()

def inverter_texto(texto):
  return texto[::-1]

def para_maiusculas(texto):
  return texto.upper()

def para_minusculas(texto):
  return texto.lower()

def capitalizar_texto(texto):
  return texto.capitalize()
