"""TaskTracker - Gerenciador de tarefas via linha de comando (CLI).

Bootcamp II - Fase 2 (Etapa Intermediária).
"""

PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


def ler_titulo():
    """Solicita o título até que um valor não vazio seja informado."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título é obrigatório e não pode ficar vazio. Tente novamente.")


def ler_prioridade():
    """Solicita a prioridade até que seja Alta, Média (ou Media) ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade inválida. Digite apenas Alta, Média ou Baixa.")


def cadastrar_tarefa(tarefas):
    """Lê os dados de uma nova tarefa e a adiciona à lista."""
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }
    tarefas.append(tarefa)
    print(f"\nTarefa '{titulo}' cadastrada com sucesso!")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas cadastradas ou avisa que a lista está vazia."""
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{numero}")
        print(f"  Título      : {tarefa['titulo']}")
        print(f"  Descrição   : {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade  : {tarefa['prioridade']}")
        print(f"  Data limite : {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status      : {tarefa['status']}")
    print(f"\nTotal: {len(tarefas)} tarefa(s).")


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
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    main()
