# Fazer chamadas para API
import requests
import jason

# conexao com banco de dados
import mysql.connector
from mysql.connector import Error
import pandas as pd

# Para criar uma página na WEB
from flask import Flask

# Chamada inicial#
print("Olá Bem vindo ao nosso sistema de Consulta de Clientes")
print("Para obter os dados, por favor digite o nome do cliente: ")
user_name = input(str())

# tratamento de erros
try:
    user_name = input(str())
except ValueError:
    print('Digite um nome válido')
    exit()

# Retirando os espaços em branco do inicio e final da string e substituir
user_name = user_name.strip()

if len(user_name) == 1:
    user_name = user_name.replace(".", "")

# chamando a API
    def user_name():
    r = requests.get(f'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios?user_name={user_name}')
    print(r.json())

# Salvando os dados recebidos pela API em variáveis que serão utilizadas posteriormente
data_dict = jason.loads(r)
fec_alta = data_dict["fec_alta"]
user_name = data_dict["user_name"]
codigo_zip = data_dict["codigo_zip"]
# credit_card_num - dado nao sera armazenado em respeito a LGPD
# credit_card_ccv - dado nao sera armazenado em respeito a LGPD
cuenta_numero = data_dict["cuenta_numero"]
direccion = data_dict["direccion"]
geo_latitud = data_dict["geo_latitud"]
geo_longitud = data_dict["geo_longitud"]
color_favorito = data_dict["color_favorito"]
foto_dni = data_dict["foto_dni"]
# ip - dado nao sera armazenado em respeito a LGPD
auto = data_dict["auto"]
auto_modelo = data_dict["auto_modelo"]
auto_tipo = data_dict["auto_tipo"]
auto_color = data_dict["auto_color"]
cantidad_compras_realizadas = data_dict["cantidad_compras_realizadas"]
avatar = data_dict["avatar"]
fec_birthday = data_dict["fec_birthday"]
id = data_dict["id"]

# Dando a opcao de salvar num banco de dados
bd_save = (bool(input("Deseja salvar os dados no Banco? Digite Sim ou Nao")))

# tratamento de erros
try:
    bd_save = input(bool())
except ValueError:
    print('Digite apenas * Sim * ou * Nao *')
    exit()

Sim = True
Nao = False

if bd_save == Sim:
    bd_hostname = (str(input("Digite o hostname do banco de dados")))
    bd_username = (str(input("Digite o usuário de banco de dados")))
    bd_password = (str(input("Digite a senha do banco de dados")))

    # caso escolha a opcao de gravar no banco, a conexao sera iniciada
    def create_bd_connection(bd_hostname, bd_username, bd_password):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=bd_hostname,
                user=bd_username,
                passwd=bd_password
            )
            print("Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

        return connection

# criando a tabela com os dados recebidos
create_database = "CREATE DATABASE dados clientes ( " + id + " INT PRIMARY KEY, " + fec_alta + " VARCHAR(45) NOT NULL, " + user_name + " VARCHAR(40) NOT NULL, " + codigo_zip + " VARCHAR(10) NOT NULL, " + cuenta_numero + " NUMERIC(8)," + direccion + " VARCHAR(40)," + geo_latitud + " VARCHAR(40)," + geo_longitud + " VARCHAR(40)," + color_favorito + " VARCHAR(40)," + foto_dni + " VARCHAR(70)," + auto + " VARCHAR(40)," + auto_modelo + " VARCHAR(40)," + auto_tipo + " VARCHAR(40)," + auto_color + " VARCHAR(40)," + cantidad_compras_realizadas + " NUMERIC(30)," + avatar + " VARCHAR(40), " + fec_birthday + " VARCHAR(40))"
create_database(create_bd_connection(), create_database)

# inserindo os dados recebidos
def execute_query(connection, create_database):
    cursor = connection.cursor()
    try:
        cursor.execute(create_database)
        connection.commit()
        print(("Tabela criada e dados salvos com sucesso!")
    except Error as err:
        print(f"Error: '{err}'")
        return cursor