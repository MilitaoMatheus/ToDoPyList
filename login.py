from database.conexao import conexao

def cadastro_usuario():
    cursor = conexao.cursor()

    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite seu senha: ")

    cursor.execute("insert into tbl_usuario (nome, email, senha) values(%s, %s, %s)", (nome, email, senha))
    conexao.commit()

    cursor.close()
    conexao.close()

cadastro_usuario()