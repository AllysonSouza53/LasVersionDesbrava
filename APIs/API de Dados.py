from flask import Flask, jsonify, request


App = Flask(__name__)
#funcinalidades
@App.route("/")
def home():
  return '<h1><center>Bem vindo ao Adm Desbrava</center></h1>'

#Perfis
Perfis = []

# GET todos perfis
@App.route("/Perfis", methods=['GET'])
def GetPerfis():
    return jsonify(Perfis)

# GET perfil por usuário
@App.route("/Perfis/<string:usuario>", methods=['GET'])
def GetPerfil(usuario):
    for perfil in Perfis:
        if perfil.get('usuario') == usuario:
            return jsonify(perfil)
    return jsonify({"erro": "Perfil não encontrado"}), 404

# POST adicionar perfil
@App.route("/Perfil", methods=['POST'])
def AddPerfil():
    novo_perfil = request.get_json()
    Perfis.append(novo_perfil)
    return jsonify(Perfis), 201

# PUT editar perfil
@App.route("/Perfis/<string:usuario>", methods=['PUT'])
def EditPerfil(usuario):
    perfil_alterado = request.get_json()
    for indice, perfil in enumerate(Perfis):
        if perfil.get('usuario') == usuario:
            Perfis[indice].update(perfil_alterado)
            return jsonify(Perfis[indice])
    return jsonify({"erro": "Perfil não encontrado"}), 404

# DELETE perfil
@App.route("/Perfis/<string:usuario>", methods=['DELETE'])
def DeletePerfil(usuario):
    for indice, perfil in enumerate(Perfis):
        if perfil.get('usuario') == usuario:
            del Perfis[indice]
            return jsonify({"mensagem": "Perfil deletado com sucesso"})
    return jsonify({"erro": "Perfil não encontrado"}), 404

#Posts
Posts = []

# GET todos posts
@App.route("/Posts", methods=['GET'])
def GetPosts():
    return jsonify(Posts)

# GET post por usuário (todos os posts desse usuário)
@App.route("/Posts/<string:usuario>", methods=['GET'])
def GetPostsUsuario(usuario):
    usuario_posts = [post for post in Posts if post.get('usuario') == usuario]
    if usuario_posts:
        return jsonify(usuario_posts)
    return jsonify({"erro": "Nenhum post encontrado para este usuário"}), 404

# POST adicionar novo post
@App.route("/Posts", methods=['POST'])
def AddPost():
    novo_post = request.get_json()
    Posts.append(novo_post)
    return jsonify(novo_post), 201

# PUT editar post por id
@App.route("/Posts/<int:id>", methods=['PUT'])
def EditPost(id):
    post_alterado = request.get_json()
    for indice, post in enumerate(Posts):
        if post.get('id') == id:
            Posts[indice].update(post_alterado)
            return jsonify(Posts[indice])
    return jsonify({"erro": "Post não encontrado"}), 404

# DELETE post por id
@App.route("/Posts/<int:id>", methods=['DELETE'])
def DeletePost(id):
    for indice, post in enumerate(Posts):
        if post.get('id') == id:
            del Posts[indice]
            return jsonify({"mensagem": "Post deletado com sucesso"})
    return jsonify({"erro": "Post não encontrado"}), 404

#Cidades
Escolas = []

# GET todas escolas de uma cidade
@App.route("/<string:uf>/municipios/<string:cidade>/escolas", methods=['GET'])
def GetEscolas(uf, cidade):
    cidade_escolas = [escola for escola in Escolas if escola.get('uf') == uf.upper() and escola.get('cidade') == cidade.upper()]
    return jsonify(cidade_escolas)

# GET escola específica por nome
@App.route("/<string:uf>/municipios/<string:cidade>/escolas/<string:nome_escola>", methods=['GET'])
def GetEscola(uf, cidade, nome_escola):
    for escola in Escolas:
        if escola.get('uf') == uf.upper() and escola.get('cidade') == cidade.upper() and escola.get('nome_escola') == nome_escola.upper():
            return jsonify(escola)
    return jsonify({"erro": "Escola não encontrada"}), 404

# POST adicionar nova escola
@App.route("/<string:uf>/municipios/<string:cidade>/escolas", methods=['POST'])
def AddEscola(uf, cidade):
    nova_escola = request.get_json()
    nova_escola['uf'] = uf.upper()
    nova_escola['cidade'] = cidade.upper()
    Escolas.append(nova_escola)
    return jsonify(nova_escola), 201

# PUT atualizar escola
@App.route("/<string:uf>/municipios/<string:cidade>/escolas/<string:nome_escola>", methods=['PUT'])
def EditEscola(uf, cidade, nome_escola):
    escola_alterada = request.get_json()
    for indice, escola in enumerate(Escolas):
        if escola.get('uf') == uf.upper() and escola.get('cidade') == cidade.upper() and escola.get('nome_escola') == nome_escola.upper():
            Escolas[indice].update(escola_alterada)
            return jsonify(Escolas[indice])
    return jsonify({"erro": "Escola não encontrada"}), 404

# DELETE escola
@App.route("/<string:uf>/municipios/<string:cidade>/escolas/<string:nome_escola>", methods=['DELETE'])
def DeleteEscola(uf, cidade, nome_escola):
    for indice, escola in enumerate(Escolas):
        if escola.get('uf') == uf.upper() and escola.get('cidade') == cidade.upper() and escola.get('nome_escola') == nome_escola.upper():
            del Escolas[indice]
            return jsonify({"mensagem": "Escola deletada com sucesso"})
    return jsonify({"erro": "Escola não encontrada"}), 404
#rodar
App.run(host='0.0.0.0')