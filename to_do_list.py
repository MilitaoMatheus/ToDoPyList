#Importando as cores a serem usadas no código
from termcolor import colored
from models.crud_tarefas import adicionarTarefa, excluirTarefas, exibirTarefas, alterarTarefas

#Menu de escolhas ao usuário
menu = """
    [1] - Adicionar tarefa     
    [2] - Excluir tarefa       
    [3] - Alterar tarefas         
    [4] - Exibir tarefas     
    [5] - Sair  
"""

#Looping para fica rodando o código
while True:
    #Realizando a escolha de opções
    print("Escolha uma das opções abaixo: ")
    opcao = input(f"{menu} \n Escolha: ")
    
    if opcao == "1":
        #Declarando o nome da tarefa
        nome_tarefa = str(input("Digite o nome da tarefa: ")).strip()
        #Declarando o status da tarefa
        status = str(input("Qual o status dessa tarefa?: ")).strip()
        if adicionarTarefa(nome_tarefa, status):
            print(colored("Tarefa adicionada com sucesso!", "green"))
        else:
            print(colored("Insira os campos corretamente!", "red"))
        #Chamando a função de adicionar tarefa
        adicionarTarefa()

    elif opcao == "2":
        #Inserindo o indice da tarefa a ser excluída
        id_tarefa = input("Digite o ID da tarefa a excluir: ")
        #Chamando a função de excluir tarefa
        if excluirTarefas(id_tarefa):
            print(colored("Tarefa excluída!", "red"))
        else:
            print(colored("ID inválido", "yellow"))
        
    elif opcao == "3":
        #Inserindo o indice da tarefa a ser alterada
        id_tarefa = input("Digite o ID da tarefa a se alterar: ")
        #Digitando o novo nome da tarefa
        nome_tarefa = str(input("Digite o nome da tarefa: ")).strip()
        #Digitando o novo status da tarefa
        status = str(input("Qual o status dessa tarefa?: ")).strip()
        #Chamando a função de alterar tarefa
        if alterarTarefas(id_tarefa, nome_tarefa, status):
            print(colored("Tarefa alterada com sucesso!", "cyan"))
        else:
            print(colored("ID inválido", "yellow"))

    elif opcao == "4":
        tarefas = exibirTarefas()
        #Se a tarefa for diferente de 0, faça:
        if tarefas:
            print(colored("\nLista de tarefas", "yellow"))
            #Looping que percorre a lista pegando os elementos e seus indices
            for tarefa in tarefas:
                print(f"{tarefa[0]} - {tarefa[1]} - {tarefa[2]} - Criado em: {tarefa[3]}")
        else:
            print(colored("Sem tarefas", "yellow"))
    
    elif opcao == "5":
        #Encerrando o looping
        print(colored("Obrigado por usar o To Do PyList!", "cyan"))
        break