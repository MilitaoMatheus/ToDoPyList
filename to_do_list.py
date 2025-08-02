#Importando as cores a serem usadas no código
from termcolor import colored

#Lista onde ficará armazenada as tarefas
tarefas = []

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
    #Método para inserir novos elementos na lista
    tarefas.append((nome_tarefa, status))
    #Imprimindo a última inserção
    print(colored(f"Tarefa adicionada: {tarefas[-1]}", "green"))

#Função para excluir uma tarefa da lista
def excluirTarefas():
    #Inserindo o indice da tarefa a ser excluída
    tarefa_excluir = int(input("Digite o indice da tarefa a excluir: "))
    #Verificando se o que foi inserido está presente na lista (maior ou igual a zero e menor ou igual a quantidade de itens na lista)
    if tarefa_excluir >= 0 and tarefa_excluir < len(tarefas):
        #Metodo para excluir um item da lista de acordo com um parametro
        tarefa_excluida = tarefas.pop(tarefa_excluir)
        #Imprimindo a tarefa exlcuida
        print(colored(f"Tarefa excluída: {tarefa_excluida[0]}", "red"))
    else:
        print(colored("Tarefa não encontrada", "yellow"))

#Função para alterar uma tarefa
def alterarTarefas():
    #Inserindo o indice da tarefa a ser alterada
    tarefa_alterar = int(input("Digite o indice da tarefa a se alterar: "))
    #Verificando se o que foi inserido está presente na lista (maior ou igual a zero e menor ou igual a quantidade de itens na lista)
    if tarefa_alterar >= 0 and tarefa_alterar < len(tarefas):
        #Digitando o novo nome da tarefa
        nome_tarefa = str(input("Digite o nome da tarefa: ")).strip()
        #Digitando o novo status da tarefa
        status = str(input("Qual o status dessa tarefa?: ")).strip()
        #Realizando a alteração na lista
        tarefas[tarefa_alterar] = (nome_tarefa, status)
    else:
        #Se o indice não for encontrado, imrpima:
        print(colored("Tarefa não encontrada", "yellow"))
    return

#Função para exibir todas as tarefas inseridas
def exibirTarefas():
    #Se a tarefa for diferente de 0, faça:
    if tarefas != []:
        #Looping que percorre a lista pegando os elementos e seus indices
        for indice, tarefa in enumerate(tarefas):
            #Exibindo os indices e os elementos
            print(f"{indice}: - {tarefa}")
    #Se a condição acima não for satisfeitam faça:
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