from database.conexao import conexao

cursor = conexao.cursor()

#Função para adicionar uma tarefa a lista
def adicionarTarefa(nome_tarefa, status):
    #Validação de campos vazios
    if nome_tarefa and status != "":
        cursor.execute("insert into tbl_tarefas(nome, status) values (%s, %s)", (nome_tarefa, status))
        conexao.commit()
        return True
    return False

#Função para excluir uma tarefa da lista
def excluirTarefas(id_tarefa):  
    if id_tarefa.isdigit():
        cursor.execute("delete from tbl_tarefas where id = %s", (id_tarefa,))
        conexao.commit()
        return True
    return False

#Função para alterar uma tarefa
def alterarTarefas(id_tarefa, nome_tarefa, status):
    if id_tarefa.isdigit() and nome_tarefa != "" and status != "":
        cursor.execute("update tbl_tarefas set nome = %s, status = %s where id = %s", (nome_tarefa, status, id_tarefa))
        conexao.commit()
        return True
    return False

#Função para exibir todas as tarefas inseridas
def exibirTarefas():
    cursor.execute("select * from tbl_tarefas")
    tarefas = cursor.fetchall()