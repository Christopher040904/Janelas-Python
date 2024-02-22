from pymongo import MongoClient

client = MongoClient("mongodb://root:senac123@127.0.0.1:37452")

# selecionando o banco de dados loja_db
db = client.loja_db

# Estamos obtendo os dados que estão cadastrados na
# tabela(coleção) usuario. Usamos db[""].find()
# O comando find localiza os dados e retorna com
# todos eles para a variável us. Depois fazemos
# a leitura de todas linha com o for e exibimos
# na tala
# for us db["usuario"].find():
#     print(us)

# Abaixo a consulta realiza o cadastro de um novo usuario e retorna o id do usuario cadastrado
# usuarior o_id = db["usuario"].insert_one({"nomeusuario":"martha","senha":"123","nivel":"usuario"}).inserted_id
# print(usuario_id)

# Localizar apenas um usuario no banco de dados
# rs = db["usuario"].find_one({"nivel":"usuario"})
# print(rs)

# Localizar todos os dados com o nivel de acesso usuario
# for rs in db["usuario"].find({"nivel":"usuario"}):
#     print(rs)