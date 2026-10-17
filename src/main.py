"""TaskTracker - Gerenciador de tarefas via linha de comando (CLI).

Bootcamp II - Fase 2 (Etapa Intermediária).
"""


def exibir_menu():
    print("\n========== TASKTRACKER ==========")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")
    print("=================================")


def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("Cadastro de tarefas em construção...")
        elif opcao == "2":
            print("Listagem de tarefas em construção...")
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
