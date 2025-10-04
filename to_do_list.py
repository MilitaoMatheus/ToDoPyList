#Importando as cores a serem usadas no código
from termcolor import colored
import mysql.connector

conexao = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password= "12345678",
    database = "TDPListdb"
)
cursor = conexao.cursor()

#Menu de escolhas ao usuário
menu = """
    [1] - Adicionar tarefa     
    [2] - Excluir tarefa       
    [3] - Alterar tarefas         
    [4] - Exibir tarefas     
    [5] - Sair  
"""

#Função para adicionar uma tarefa a lista
def adicionarTarefa():
    #Declarando o nome da tarefa
    nome_tarefa = str(input("Digite o nome da tarefa: ")).strip()
    #Declarando o status da tarefa
    status = str(input("Qual o status dessa tarefa?: ")).strip()
    #Validação de campos vazios
    if nome_tarefa and status != "":
        cursor.execute("insert into tbl_tarefas(nome, status) values (%s, %s)", (nome_tarefa, status))
        conexao.commit()
        print(colored("Tarefa adicionada com sucesso!", "green"))
    else:
        print(colored("Insira os campos corretamente!", "red"))

#Função para excluir uma tarefa da lista
def excluirTarefas():
    #Inserindo o indice da tarefa a ser excluída
    id_tarefa = input("Digite o ID da tarefa a excluir: ")
   
    if id_tarefa.isdigit():
        cursor.execute("delete from tbl_tarefas where id = %s", (id_tarefa,))
        conexao.commit()
        print(colored("Tarefa excluída!", "red"))
    else:
        print(colored("ID inválido", "yellow"))

#Função para alterar uma tarefa
def alterarTarefas():
    #Inserindo o indice da tarefa a ser alterada
    id_tarefa = input("Digite o ID da tarefa a se alterar: ")
    
    if id_tarefa.isdigit():
        #Digitando o novo nome da tarefa
        nome_tarefa = str(input("Digite o nome da tarefa: ")).strip()
        #Digitando o novo status da tarefa
        status = str(input("Qual o status dessa tarefa?: ")).strip()
        if nome_tarefa != "" and status != "":
            cursor.execute("update tbl_tarefas set nome = %s, status = %s where id = %s", (nome_tarefa, status, id_tarefa))
            conexao.commit()
            print(colored("Tarefa alterada com sucesso!", "cyan"))
        else:
            print(colored("Insira os campos corretamente!", "red"))
    else:
        #Se o indice não for encontrado, imrpima:
        print(colored("ID inválido", "yellow"))

#Função para exibir todas as tarefas inseridas
def exibirTarefas():
    cursor.execute("select * from tbl_tarefas")
    tarefas = cursor.fetchall()

    #Se a tarefa for diferente de 0, faça:
    if tarefas:
        #Looping que percorre a lista pegando os elementos e seus indices
        for tarefa in tarefas:
            print(f"{tarefa[0]} - {tarefa[1]} - {tarefa[2]}")
    else:
        print(colored("Sem tarefas", "yellow"))

#Looping para fica rodando o código
while True:
    #Realizando a escolha de opções
    print("Escolha uma das opções abaixo: ")
    opcao = input(f"{menu} \n Escolha: ")
    
    if opcao == "1":
        #Chamando a função de adicionar tarefa
        adicionarTarefa()

    elif opcao == "2":
        #Chamando a função de excluir tarefa
        excluirTarefas()

    elif opcao == "3":
        #Chamando a função de alterar tarefa
        alterarTarefas()

    elif opcao == "4":
        #Chamando a função de exibir tarefa
        exibirTarefas()

    elif opcao == "5":
        #Encerrando o looping
        print(colored("Obrigado por usar o To Do PyList!", "cyan"))
        break

cursor.close()
conexao.close()