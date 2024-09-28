import os


def listar(Lista_Projetada):
    if not Lista_Projetada:
        print("Sem tarefas para listar.")
        print("")
    else:
        print("Tarefas:")
        for i, valor in enumerate(Lista_Projetada):
            print(f'{i+1} - {valor}')
        print("")


def refazer(ListaAtividade, ListaAcumulada):
    if not ListaAcumulada:
        print("Nada a refazer.")
    else:
        tarefa = ListaAcumulada.pop()
        ListaAtividade.append(tarefa)
        print()


def desfazer(ListaAtividade, ListaAcumulada):
    if not ListaAtividade:
        print("Nada para desfazer.")
    else:
        tarefa = ListaAtividade.pop()
        print(f'{tarefa=} removida na lista de tarefas.')
        ListaAcumulada.append(tarefa)
        print()


ListaAcumulada = []
ListaTarefas = []
while True:
    print("Comandos: listar, desfazer, refazer ou (clear)")
    comando = input("Digite uma tarefa ou comando: ").lower()
    if comando.strip() == "listar":
        listar(ListaTarefas)
    elif comando.strip() == "desfazer":
        desfazer(ListaTarefas, ListaAcumulada)
        listar(ListaTarefas)
    elif comando.strip() == "refazer":
        refazer(ListaTarefas, ListaAcumulada)
        listar(ListaTarefas)
    elif comando == "clear":
        os.system('cls')
    else:
        ListaTarefas.append(comando)
