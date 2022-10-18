import mysql.connector

# Conectando ao banco de dados 'MySql'

conexao = mysql.connector.connect(
    host='localhost',
    user='Moreira',
    password='11c1011100',
    database='firstbd',
)

cursor = conexao.cursor()


# CREATE


def criar_produto():
    nome_produto = input('Digite o nome do produto para cadatro : ')
    unidade = int(input('Quantidade de produtos: '))
    valor = float(input('Digite o valor do produto: '))
    comando = f'INSERT INTO vendas (nome_produto, unidade, valor) VALUES ("{nome_produto}", {unidade}, {valor})'
    cursor.execute(comando)
    conexao.commit()


# READ

def ler_produto():
    comando = f'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()  # ler o banco de dados
    print(resultado)


# UPDATE

def editar_produto():
    nome_produto = input('Digite o nome do produto a ser EDITADO: ')
    valor = float(input(f'Digite o novo valor de {nome_produto}: '))
    comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()


# DELETE

def deletar_produto():
    nome_produto = input('Digite o nome do produto a ser DELETADO: ')
    comando = f'DELETE from vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()


# Entrada de dados

while True:
    crud_principal = int(
        input(
            'Digite:\n (1) para CRIAR novo produto\n (2) para EDITAR um produto\n (3) para DELETAR um produto\n (4) para ver produtos cadastrados '))


    def input_do_crud():
        if crud_principal == 1:
            ler_produto()
            criar_produto()
        elif crud_principal == 2:
            ler_produto()
            editar_produto()
        elif crud_principal == 3:
            ler_produto()
            deletar_produto()
        elif crud_principal == 4:
            ler_produto()
    while crud_principal > 5:
        crud_principal = int(
            input(
                'Por favor, escolha uma opção válida\n Digite:\n (1) para CRIAR novo produto\n (2) para EDITAR um produto\n (3) para DELETAR um produto\n (4) para ver produtos cadastrados '))
    input_do_crud()

